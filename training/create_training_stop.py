from picamera import PiCamera
from time import sleep

camera = PiCamera()
# Vertically flip the camera
camera.rotation = 180

stop_count = 0

while True:
    camera.capture('./images/stop{}.jpg'.format(stop_count))
    stop_count += 1
    sleep(1)
