#!/usr/bin/python3
import time

from picamera2.encoders import JpegEncoder
from picamera2 import Picamera2


picam2 = Picamera2()
video_config = picam2.video_configuration(main={"size": (1920, 1080)})
picam2.configure(video_config)

picam2.start_preview()
encoder = JpegEncoder(q=70)

picam2.start_recording(encoder, 'test.mjpeg')
time.sleep(10)
picam2.stop_recording()
