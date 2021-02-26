#!/bin/bash
gst-launch-1.0 -v tcpclientsrc host=10.0.1.18 port=5000  ! gdpdepay ! rtph264depay ! h264parse ! avdec_h264 ! autovideosink sync=false
