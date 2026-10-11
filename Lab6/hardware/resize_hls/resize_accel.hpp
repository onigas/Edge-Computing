// Interfata acceleratorului Resize AXI4-Stream, compatibila cu Vitis HLS 2022.2.
// Bazata pe Xilinx/PYNQ-HelloWorld (BSD-3-Clause).
#pragma once
#include "hls_stream.h"
#include "ap_axi_sdata.h"

typedef ap_axiu<24, 1, 1, 1> interface_t;
typedef hls::stream<interface_t> stream_t;

void resize_accel(stream_t& src, stream_t& dst,
                  int src_rows, int src_cols,
                  int dst_rows, int dst_cols);
