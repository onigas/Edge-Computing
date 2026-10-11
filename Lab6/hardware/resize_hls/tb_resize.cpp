// Test functional pentru AXI4-Stream Resize, Vitis HLS 2022.2.
// Verifica doua configuratii dinamice, numarul de pixeli si TLAST pe ultimul beat.
// Nu inlocuieste compararea imaginii cu OpenCV pe placa PYNQ-Z2.
#include "resize_accel.hpp"
#include <cstdio>
#include <cstdlib>

static bool check_case(int source_h, int source_w, int target_h, int target_w) {
    stream_t input, output;
    const unsigned int colour = 0x304050; // 3 canale de cate 8 biti
    const int num_in = source_h * source_w;
    const int num_out = target_h * target_w;

    for (int i = 0; i < num_in; ++i) {
        interface_t beat;
        beat.data = colour;
        beat.keep = 7;
        beat.strb = 7;
        beat.last = (i == num_in - 1) ? 1 : 0;
        beat.user = 0;
        beat.id = 0;
        beat.dest = 0;
        input.write(beat);
    }

    resize_accel(input, output, source_h, source_w, target_h, target_w);

    int nearly_constant = 0;
    for (int i = 0; i < num_out; ++i) {
        if (output.empty()) {
            std::printf("EROARE: doar %d din %d pixeli iesiti\n", i, num_out);
            return false;
        }

        interface_t beat = output.read();
        const bool expected_last = (i == num_out - 1);
        if (static_cast<bool>(beat.last) != expected_last) {
            std::printf("EROARE: TLAST la pixelul %d din %d\n", i, num_out);
            return false;
        }
        if (static_cast<unsigned>(beat.keep) != 7) {
            std::printf("EROARE: TKEEP la pixelul %d\n", i);
            return false;
        }

        const unsigned actual = static_cast<unsigned>(beat.data);
        const int ch0 = (actual & 255);
        const int ch1 = ((actual >> 8) & 255);
        const int ch2 = ((actual >> 16) & 255);
        if (std::abs(ch0 - 0x50) <= 4 &&
            std::abs(ch1 - 0x40) <= 4 &&
            std::abs(ch2 - 0x30) <= 4) {
            ++nearly_constant;
        }
    }
    if (!output.empty()) {
        std::printf("EROARE: pixeli suplimentari la iesire\n");
        return false;
    }
    if (nearly_constant < (num_out * 95) / 100) {
        std::printf("EROARE: numai %d din %d pixeli au culoarea asteptata\n",
                    nearly_constant, num_out);
        return false;
    }

    std::printf("OK: %dx%d -> %dx%d: %d pixeli, TLAST final, TKEEP corect\n",
                source_w, source_h, target_w, target_h, num_out);
    return true;
}

int main() {
    if (!check_case(48, 64, 24, 32)) return 1;
    if (!check_case(24, 32, 12, 16)) return 1;
    std::printf("SIMULARE C REUSITA: ambele rezolutii\n");
    return 0;
}
