"""Lab7.1: original CNV-W2A2 inference; no training or hardware reconstruction."""
import contextlib
import csv
import hashlib
import importlib
import importlib.util
import io
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import sys
import tempfile
from time import perf_counter
import urllib.request
import zipfile

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent
REVISION = 'd39c1c75403db571f54dd0f0cf27ae5104ac968e'
REPOSITORY = 'onigas/BNN-PYNQ'
CLASS_NAMES = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer',
               'Dog', 'Frog', 'Horse', 'Ship', 'Truck']
REFERENCE_SHA = '67a9b9e411d96725c170330073099269f9858ccc'
EXTENSIONS = {'.jpg', '.jpeg', '.png', '.bmp'}


def git_blob_sha(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def decode_cifar_record(data):
    if len(data) != 3073:
        raise ValueError('A CIFAR record must contain 3073 bytes.')
    return np.frombuffer(data, dtype=np.uint8, offset=1).reshape(3, 32, 32).transpose(1, 2, 0).copy()


def prepare_reference():
    binary = ROOT / 'images/reference/deer.bin'
    data = binary.read_bytes()
    if git_blob_sha(data) != REFERENCE_SHA:
        raise RuntimeError('deer.bin does not match the upstream reference.')
    png = binary.with_suffix('.png')
    Image.fromarray(decode_cifar_record(data)).save(str(png))
    (ROOT / 'images/own').mkdir(parents=True, exist_ok=True)
    (ROOT / 'results').mkdir(exist_ok=True)
    return png


def download_file(url, target, max_bytes=200 * 1024 * 1024):
    target = Path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    partial = target.with_name(target.name + '.part')
    request = urllib.request.Request(url, headers={'User-Agent': 'Edge-Computing-Lab7.1'})
    try:
        with urllib.request.urlopen(request, timeout=60) as response, partial.open('wb') as out:
            total = 0
            while True:
                block = response.read(1024 * 1024)
                if not block:
                    break
                total += len(block)
                if total > max_bytes:
                    raise RuntimeError('Download exceeds size limit.')
                out.write(block)
        partial.replace(target)
    finally:
        if partial.exists():
            partial.unlink()


def download_original_jpg():
    path = ROOT / 'images/reference/deer_original.jpg'
    if not path.exists():
        download_file('https://raw.githubusercontent.com/' + REPOSITORY + '/' + REVISION +
                      '/tests/Test_image/deer.jpg', path, 2 * 1024 * 1024)
    if git_blob_sha(path.read_bytes()) != '6aaa046c4d58d87cd76eca728ec160e0b7a28db5':
        raise RuntimeError('The reference JPG does not match upstream.')
    return path


def _fetch_local_runtime():
    """Extract existing W2A2 assets, without executing setup.py or pip."""
    vendor = ROOT / '_vendor'
    destination = vendor / 'BNN-PYNQ'
    if (destination / 'bnn/bnn.py').is_file():
        return destination
    vendor.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='prepare-', dir=str(vendor)) as tmp:
        tmp = Path(tmp)
        archive = tmp / 'source.zip'
        print('Downloading the existing BNN-PYNQ runtime; no compilation.')
        download_file('https://codeload.github.com/' + REPOSITORY + '/zip/' + REVISION, archive)
        extracted = tmp / 'snapshot'
        with zipfile.ZipFile(str(archive)) as zf:
            for member in zf.infolist():
                parts = PurePosixPath(member.filename).parts
                if member.is_dir() or len(parts) < 2:
                    continue
                rel = PurePosixPath(*parts[1:])
                name = rel.as_posix()
                selected = name in {'bnn/__init__.py', 'bnn/bnn.py', 'LICENSE', 'README.md'}
                selected |= name.startswith('bnn/params/cifar10/cnvW2A2/')
                selected |= name.startswith('bnn/bitstreams/pynqZ1-Z2/cnvW2A2-')
                selected |= (name.startswith('bnn/libraries/pynqZ1-Z2/python_') and '-cnvW2A2-' in name)
                if not selected:
                    continue
                if rel.is_absolute() or '..' in rel.parts or member.file_size > 32 * 1024 * 1024:
                    raise RuntimeError('Unexpected archive entry: ' + name)
                target = extracted.joinpath(*rel.parts)
                target.parent.mkdir(parents=True, exist_ok=True)
                with zf.open(member) as source, target.open('wb') as out:
                    shutil.copyfileobj(source, out)
        if not (extracted / 'bnn/bnn.py').is_file():
            raise RuntimeError('Archive does not contain bnn/bnn.py.')
        (extracted / 'LAB71_SOURCE.json').write_text(json.dumps(
            {'repository': REPOSITORY, 'revision': REVISION}, indent=2))
        if destination.exists():
            raise RuntimeError('Incomplete _vendor/BNN-PYNQ exists. Inspect it before retrying.')
        extracted.rename(destination)
    return destination


def load_bnn(allow_download=True):
    """Prefer installed bnn; otherwise use a local snapshot. Never update packages."""
    if os.environ.get('BOARD') != 'Pynq-Z2':
        raise RuntimeError('Run on the actual PYNQ-Z2 board, with BOARD=Pynq-Z2.')
    if importlib.util.find_spec('pynq') is None:
        raise RuntimeError('Use the board Jupyter kernel containing PYNQ.')
    provenance = {'origin': 'existing bnn installation; commit not asserted'}
    if importlib.util.find_spec('bnn') is None:
        local = ROOT / '_vendor/BNN-PYNQ'
        if not (local / 'bnn/bnn.py').is_file():
            if not allow_download:
                raise RuntimeError('No bnn runtime. Enable ALLOW_DOWNLOAD or copy _vendor/BNN-PYNQ.')
            local = _fetch_local_runtime()
        sys.path.insert(0, str(local))
        importlib.invalidate_caches()
        provenance = {'origin': 'local source snapshot; see provenance', 'path': str(local)}
        marker = local / 'LAB71_SOURCE.json'
        if marker.is_file():
            provenance.update(json.loads(marker.read_text()))
    # Equivalent Pillow compatibility name; upstream preprocessing is unchanged.
    if not hasattr(Image, 'ANTIALIAS'):
        Image.ANTIALIAS = Image.Resampling.LANCZOS
    bnn = importlib.import_module('bnn')
    for attr in ('CnvClassifier', 'NETWORK_CNVW2A2', 'RUNTIME_HW'):
        if not hasattr(bnn, attr):
            raise RuntimeError('Unexpected bnn package: ' + str(bnn.__file__))
    core = importlib.import_module('bnn.bnn')
    lib = Path(core.BNN_LIB_DIR) / 'python_hw-cnvW2A2-pynqZ1-Z2.so'
    bit = Path(core.BNN_BIT_DIR) / 'cnvW2A2-pynqZ1-Z2.bit'
    params = Path(core.BNN_PARAM_DIR) / 'cifar10/cnvW2A2'
    for required in (lib, bit, bit.with_suffix('.hwh'), params / 'classes.txt'):
        if not required.is_file():
            raise FileNotFoundError('Missing model asset: ' + str(required))
    if (params / 'classes.txt').read_text().splitlines() != CLASS_NAMES:
        raise RuntimeError('Unexpected CIFAR-10 class order.')
    if not list(params.glob('*.bin')):
        raise RuntimeError('No pretrained parameter binaries found.')
    import pynq
    provenance.update(python=sys.version, python_executable=sys.executable,
                      pynq_version=getattr(pynq, '__version__', 'unknown'),
                      bnn_file=str(bnn.__file__), network='cnvW2A2', dataset='cifar10',
                      runtime='python_hw', board=os.environ['BOARD'])
    provenance['sha256'] = {str(p): hashlib.sha256(p.read_bytes()).hexdigest()
                           for p in [bit, bit.with_suffix('.hwh'), lib] + sorted(params.glob('*'))
                           if p.is_file()}
    (ROOT / 'results').mkdir(exist_ok=True)
    (ROOT / 'results/environment.json').write_text(json.dumps(provenance, indent=2))
    return bnn, provenance


def check_overlay(classifier):
    from pynq import PL
    actual = getattr(PL, 'bitfile_name', None)
    if not actual or Path(actual).resolve() != Path(classifier.bnn.bitstream_path).resolve():
        raise RuntimeError('Overlay changed. Restart this kernel and run Lab7.1 from the beginning.')


def quiet_call(function, *args):
    with contextlib.redirect_stdout(io.StringIO()):
        return function(*args)


def read_rgb(path):
    with Image.open(str(path)) as image:
        return image.convert('RGB')


def network_input(classifier, image):
    stream = io.BytesIO()
    classifier.image_to_cifar(image.copy(), stream)
    return decode_cifar_record(stream.getvalue())


def infer_file(classifier, path):
    check_overlay(classifier)
    path = Path(path)
    t0 = perf_counter()
    image = read_rgb(path)
    t1 = perf_counter()
    scores = np.asarray(quiet_call(classifier.classify_image_details, image.copy())).copy()
    t2 = perf_counter()
    if scores.shape != (10,):
        raise RuntimeError('Expected ten class scores, got ' + str(scores.shape))
    order = np.argsort(-scores, kind='stable')
    prediction = int(order[0])
    t3 = perf_counter()
    report = {'file': str(path.relative_to(ROOT)) if ROOT in path.parents else str(path),
              'prediction_id': prediction, 'prediction': classifier.classes[prediction],
              'top_score': int(scores[prediction]),
              'score_margin': int(scores[order[0]] - scores[order[1]]),
              'decode_ms': (t1-t0)*1000, 'api_ms': (t2-t1)*1000,
              'file_to_prediction_ms': (t3-t0)*1000,
              'library_reported_ms': float(classifier.usecPerImage)/1000}
    return report, image, scores


def load_labels(path):
    labels = {}
    if Path(path).exists():
        with Path(path).open(newline='', encoding='utf-8') as source:
            for row in csv.DictReader(source):
                text = row.get('class_id', '').strip()
                if not text:
                    continue
                value = int(text)
                key = row['file'].replace('\\', '/')
                if value not in range(10) or key in labels:
                    raise ValueError('Invalid or duplicate label: ' + key)
                labels[key] = value
    return labels


def expected_label(path, labels):
    key = Path(path).relative_to(ROOT / 'images').as_posix()
    if key in labels:
        return labels[key]
    parent = Path(path).parent.name.lower()
    names = [name.lower() for name in CLASS_NAMES]
    return names.index(parent) if parent in names else None


def save_csv(path, records):
    if not records:
        raise ValueError('No results to save.')
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(dict.fromkeys(key for row in records for key in row))
    with path.open('w', newline='', encoding='utf-8') as target:
        writer = csv.DictWriter(target, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)
