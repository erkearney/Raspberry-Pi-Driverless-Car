# Raspberry-Pi Driverless Car
In the modern day many people approach the idea of self-driving vehicles with 
a feeling of suspicion. Many people are apprehensive about sharing the roads 
with fully autonomous vehicles. In order to move forward into a safer driving 
environment, the approval of the general public is necessary. We be using a 
Raspberry-Pi with a camera attached to a remote-controlled car to exhibit that 
autonomous vehicles can share the road with human drivers and are in fact 
dependable. We can demonstrate that an autonomous car is safer than a human 
driver.
# Prerequisites
[Python  3.7.1 or greater](https://www.python.org/downloads/)
### Getting Started
#### Setup your Raspberry Pi
* **Install an Operating System, we used [Raspbian](https://www.raspberrypi.org/downloads/raspbian/**
* **Mount Raspbian's boot partition**
* **Add a file called 'ssh' to the boot partition**
```
touch ssh
```
* **Use a text editor to create a file called 'wpa_supplicant.conf', this file should have the following lines (replace router_name and password with your WiFi login info):**
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
network={
    ssid="router_name"
    psk="password"
    key_mgmt=WPA-PSK
}
```
* **Discover your Pi's assigned IP address by logging into your router, using nmap, or another method**
* **SSH into the Pi**
```
ssh pi@Your.Pi's.IP
```
#### Clone the repository: 
```
git clone https://github.com/erkearney/Raspberry-Pi-Driverless-Car.git
```
#### Navigate to the project directory

```
cd Raspberry-Pi-Driverless-Car
```
#### Install dependencies

```
python setup.py
```
#### Run the project

```
python driverless_car.py
```
## Built With
### Software
[![python](https://github.com/erkearney/Raspberry-Pi-Driverless-Car/blob/master/img/python_logo.png)](https://www.python.org/)[![NumPy](https://github.com/erkearney/Raspberry-Pi-Driverless-Car/blob/master/img/NumPy_logo.png)](http://www.numpy.org/)[![TensorFlow](https://raw.githubusercontent.com/erkearney/Raspberry-Pi-Driverless-Car/master/img/Tensorflow_logo.png)](https://www.tensorflow.org/api_docs/)[![OpenCV (Python interface)](https://github.com/erkearney/Raspberry-Pi-Driverless-Car/blob/master/img/OpenCV_logo.png)](https://opencv.org/)[![Sphinx](https://github.com/erkearney/Raspberry-Pi-Driverless-Car/blob/master/img/Sphinx_logo.png)](http://www.sphinx-doc.org/en/master/)

* **[Python](https://www.python.org/) -- The Language this project is written in**
* **[NumPy](http://www.numpy.org/) -- For matrix/vector manipulation**
* **[TensorFlow (Python API)](https://www.tensorflow.org/api_docs/) -- For machine learning**
* **[OpenCV (Python API)](https://opencv.org/) -- For Image/Video processing**
* **[Sphinx](http://www.sphinx-doc.org/en/master/) -- For generating code documentation**

### Hardware
[![Raspberry Pi](https://github.com/erkearney/Raspberry-Pi-Driverless-Car/blob/master/img/Raspberry_pi_logo.png)](https://www.raspberrypi.org/)[![Webcam (Placeholder)](https://raw.githubusercontent.com/erkearney/Raspberry-Pi-Driverless-Car/master/img/Webcam_image.png)](https://www.amazon.com/dp/B01ER2SKFS/ref=cm_sw_r_cp_ep_dp_y0H8Bb1N6AZ89)[![Remote Control Cars (Placeholder)](https://raw.githubusercontent.com/erkearney/Raspberry-Pi-Driverless-Car/master/img/RC_cars.png)](https://amazon.com/Remote-Control-Lamborghini-Reventon-Scale/dp/B001TMBQYC/ref=sr_1_4?ie=UTF8&qid=1545527318&sr=8-4&keywords=rc+cars+lamborghini)[![ARDUINO UNO R3 [A000066]](https://raw.githubusercontent.com/erkearney/Raspberry-Pi-Driverless-Car/master/img/Arduino_logo.png)](https://amazon.com/Arduino-A000066-ARDUINO-UNO-R3/dp/B008GRTSV6/ref=sr_1_3?ie=UTF8&qid=1545527262&sr=8-3&keywords=ARDUINO+uno)

* **[Raspberry Pi Model 3A+](https://www.raspberrypi.org/) -- The hardware the code runs on**
* **[Camera (current model is placeholder)](https://www.amazon.com/dp/B01ER2SKFS/ref=cm_sw_r_cp_ep_dp_y0H8Bb1N6AZ89) -- Gets input video for the self-driving cars**
* **[Remote Control Cars (current model is placeholder)](https://amazon.com/Remote-Control-Lamborghini-Reventon-Scale/dp/B001TMBQYC/ref=sr_1_4?ie=UTF8&qid=1545527318&sr=8-4&keywords=rc+cars+lamborghini) -- Automatically driven by this project**
* **[ARDUINO](https://amazon.com/Arduino-A000066-ARDUINO-UNO-R3/dp/B008GRTSV6/ref=sr_1_3?ie=UTF8&qid=1545527262&sr=8-3&keywords=ARDUINO+uno) -- Serves as the interface between the Raspberry Pi and the RC car**


## Documentation
This project uses [NumPy Documentation Style](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard), it also uses [Sphinx](http://www.sphinx-doc.org/en/master/) to generate documentation.
The documentation can be viewed using the index.html file in the docs/_build directory



## Authors
* **Christopher Erickson** -- Hardware, -- [E-mail](cerick25@msudenver.edu)
* **Eric Kearney** -- Software -- [E-mail](ericrkearney@gmail.com), [GitHub](https://github.com/erkearney)

## License
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

## Acknowledgements
* **Dr. Megan Hughes-Zarzo, Director of the Honor's Program at Metropolitan State University of Denver -- [E-mail](mhughe47@msudenver.edu)**
* **Jennifer O'Dell, Coordinator of the Honor's Program at Metropolitan State Univerty of Denver -- Coordinated student travel -- [E-mail](jlutes1@msudenver.edu)**
* **[2019 Western Regional Honor's Conference](https://wrhcouncil.org/conferences/)**
* **Metropolitan State University of Denver Student Activities -- Funded student travel**
