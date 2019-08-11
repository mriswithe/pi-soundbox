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
1. Compile and install Python 3.7 see [compile python][#Compile-Python]
1.
1. Clone the repo into /opt/soundbox
```bash
sudo git clone https://github.com/mriswithe/pi-soundbox.git /opt/soundbox
sudo ln -s /opt/soundbox/soundbox.service /lib/systemd/system/soundbox.service
sudo systemctl enable soundbox.service
```
 
 
 
## Compile Python
.

