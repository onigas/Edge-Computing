# Lab6 / Resize AXI4-Stream - Vitis HLS 2022.2
# Rulare in Vitis HLS Command Prompt, dupa setarea VITIS_VISION_INCLUDE.
# Etapa implicita: csim. Optional: LAB6_HLS_STAGE=csynth / export.
set folder [file dirname [file normalize [info script]]]

if {![info exists ::env(VITIS_VISION_INCLUDE)]} {
    puts stderr "EROARE: setati VITIS_VISION_INCLUDE la .../Vitis_Libraries/vision/L1/include (ramura 2022.2)."
    exit 1
}
set inc [file normalize $::env(VITIS_VISION_INCLUDE)]
if {![file exists [file join $inc imgproc xf_resize.hpp]]} {
    puts stderr "EROARE: nu gasesc [file join $inc imgproc xf_resize.hpp]"
    exit 1
}
if {![file exists [file join $inc common xf_common.hpp]]} {
    puts stderr "EROARE: nu gasesc [file join $inc common xf_common.hpp]"
    exit 1
}

set stage "csim"
if {[info exists ::env(LAB6_HLS_STAGE)]} {
    set stage $::env(LAB6_HLS_STAGE)
}

open_project -reset [file join $folder build resize_hls]
set_top resize_accel
set cflags "-I$inc -D__XF__AXI_SDATA__"
add_files [file join $folder xf_resize_accel_stream.cpp] -cflags $cflags
add_files -tb [file join $folder tb_resize.cpp] -cflags $cflags
open_solution -reset solution1 -flow_target vivado
set_part {xc7z020clg400-1}
create_clock -period 10 -name default

if {$stage eq "csim"} {
    csim_design
} elseif {$stage eq "csynth"} {
    csynth_design
} elseif {$stage eq "export"} {
    csynth_design
    export_design -format ip_catalog -rtl verilog -description "Lab6: streaming Resize" -display_name "resize_accel"
} else {
    puts stderr "EROARE: LAB6_HLS_STAGE trebuie sa fie csim, csynth sau export."
    exit 1
}
puts "ETAPA $stage FINALIZATA. Cititi logul pentru WARNINGS/ERRORS si verificati raportul."
exit
