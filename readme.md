# Simple Wireless Rover for Raspberry Pi

![rover](images/IMG_3115.JPG)
Small robotic platform based on Raspberry Pi controlled by a remote PS4 game controller over a wireless network.

## TODOs (Feb. 2021): 
- [ ] Migration to motorkit
    https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/installing-software
    https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library.git
- [ ] Picture.
- [X] Support pan/tilt  
- [X] Refactor packages
- [X] Update doc.  
- [X] installation


## Kickstart Guide


### 1. Install requirements
`pip3 install -r requirements.txt`

### 1.5. Install dependencies in Ubuntu server machine:
`sudo apt-get install python3-smbus`  

### 2. Start server in Raspberry Pi:
`python3 robotServer.py`

### 3. Start the client on a remote machine
Connect game controller to remote machine. Configure the correct server IP on client and run `python3 client.py` on the remote machine.

`client.py -h <host> -p <port> [--verbose]`

### Controller
- **Right pad:** Speed, turning and steering
- **Left pad:** Look with camera
- **Hat pad:** Move camera center


## Current Hardware
- Raspberry Pi 3 with Ubuntu Server LTS 20.04
- Adafruit Motor Hat https://www.adafruit.com/product/2348 
- 4x 5-12V DC gear motors.
- 12V battery pack for motor power
- USB based battery pack for Raspberry Pi 3

