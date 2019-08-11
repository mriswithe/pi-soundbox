# RPi Soundbox
This is made to assist in an easy setup of a Raspberry Pi into a little random sound player.

## Requirements
* Raspberry Pi 3/4/0
* [AIY Voice kit V1](https://aiyprojects.withgoogle.com/voice-v1/)
* Raspbian or the AIY Voice Kit image
* Some OGG/WAV/MP3 files that you want to play
* Python 3.7
  * This may not be REQUIRED, but is what I wrote/tested the code with. Likely 3.6 or above would be fine too.
  

## Usage Overview
1. Follow the base instructions for installing and configuring the AIY Voice Kit with your RPi
1. Compile and install Python 3.7 see [Compile Python](#compile-python)
1. Clone the repo into /opt/soundbox and enable systemd
    ```bash
    sudo git clone https://github.com/mriswithe/pi-soundbox.git /opt/soundbox
    sudo ln -s /opt/soundbox/soundbox.service /lib/systemd/system/soundbox.service
    sudo systemctl enable soundbox.service
    ```
1. Create a virtual environment and install requirements
    ```bash
   python3.7 -m venv /opt/soundbox/venv
   source /opt/soundbox/venv/bin/activate
   pip install -r /opt/soundbox/requirements.txt
   # Need to clone the aiyprojects repo to install it
   git clone https://github.com/google/aiyprojects-raspbian.git /tmp/aiyprojects
   pip install /tmp/aiyprojects/src/
   ``` 
1. Put sounds into the /opt/soundbox/sounds directory, use SCP or something
1. Restart the Raspberry Pi. 
 
## Compile Python
.

