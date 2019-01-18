from picamera import PiCamera
from time import sleep

camera = PiCamera()
# Vertically flip the camera
camera.rotation = 180

go_count = 0

while True:
    camera.capture('./images/go{}.jpg'.format(go_count))
    go_count += 1
    sleep(1)
