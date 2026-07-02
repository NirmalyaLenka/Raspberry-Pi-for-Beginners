# Raspberry Pi for Beginners
 
A simple, no-nonsense guide to setting up and using a Raspberry Pi for the first time. This repository is meant for students, hobbyists, and anyone who has never touched a Raspberry Pi before.
 
No prior experience with Linux or electronics is required.
 
## What is a Raspberry Pi
 
A Raspberry Pi is a small, low-cost computer about the size of a credit card. It runs a full operating system (usually a version of Linux called Raspberry Pi OS) and has pins along one edge called GPIO pins that let it control and read data from electronic components like LEDs, sensors, and motors.
 
People use it for:
 
- Learning programming and Linux
- Home automation projects
- Retro gaming consoles
- Media servers
- Robotics and IoT projects
- School and college electronics projects
## What You Will Need
 
| Item | Notes |
|---|---|
| Raspberry Pi board | Any model (Pi 3, Pi 4, Pi 5, Pi Zero, etc.) |
| microSD card | 16 GB or larger, Class 10 recommended |
| Power supply | Official Pi power adapter is best, avoid weak phone chargers |
| SD card reader | To flash the operating system from your computer |
| Monitor + HDMI cable | Optional if you plan to use SSH instead |
| USB keyboard and mouse | Optional if you plan to use SSH instead |
| Wi-Fi or Ethernet | For internet access |
 
You do not need a monitor and keyboard if you plan to control the Pi remotely (this is called a "headless setup" and is covered below).
 
## Step 1: Flash the Operating System
 
1. Download and install **Raspberry Pi Imager** from the official Raspberry Pi website onto your computer.
2. Insert your microSD card into your computer using the SD card reader.
3. Open Raspberry Pi Imager.
4. Choose your device (for example, Raspberry Pi 4).
5. Choose the operating system. For beginners, "Raspberry Pi OS (32-bit)" or "Raspberry Pi OS (64-bit)" is a good default.
6. Choose your storage device (the microSD card). Double check you have selected the correct drive, since this step will erase everything on it.
7. Click the settings/gear icon before writing. Here you can pre-configure:
   - Hostname
   - Username and password
   - Wi-Fi network name and password
   - Enabling SSH (important if you want a headless setup)
8. Click **Write** and wait for the process to finish and verify.
## Step 2: First Boot
 
1. Insert the microSD card into the Raspberry Pi.
2. Connect the power supply last, after everything else (monitor, keyboard, mouse if using them) is plugged in.
3. Wait for the Pi to boot. The first boot can take a minute or two.
4. If you used a monitor, you will see the Raspberry Pi OS desktop appear.
5. If you set up SSH and Wi-Fi during imaging, you can instead connect from your computer using SSH (see below).
## Step 3: Connecting via SSH (Headless Setup)
 
If you do not have a spare monitor and keyboard, you can control the Pi entirely from your computer.
 
1. Find the Pi's IP address. If you set a hostname during imaging (for example `raspberrypi`), you can often connect using:
```
ssh username@raspberrypi.local
```
 
2. If that does not work, find the IP address from your router's admin page, or by using a network scanning tool.
3. Connect using a terminal (Linux/Mac) or PowerShell/Command Prompt (Windows):
```
ssh username@<ip-address>
```
 
4. Enter the password you set during imaging.
5. You are now controlling the Pi from your computer's terminal.
## Step 4: Basic Linux Commands to Know
 
The Raspberry Pi runs Linux, so a few basic commands go a long way.
 
| Command | What it does |
|---|---|
| `pwd` | Shows your current folder |
| `ls` | Lists files in the current folder |
| `cd foldername` | Moves into a folder |
| `mkdir foldername` | Creates a new folder |
| `sudo apt update && sudo apt upgrade` | Updates installed software |
| `sudo reboot` | Restarts the Pi |
| `sudo shutdown now` | Safely shuts down the Pi |
 
Always shut the Pi down properly before unplugging power. Just pulling the plug can corrupt the SD card.
 
## Step 5: Enabling Interfaces (GPIO, Camera, I2C, SPI)
 
Many projects need hardware interfaces enabled first.
 
1. Open a terminal and run:
```
sudo raspi-config
```
 
2. Go to **Interface Options**.
3. Enable the interface you need, for example:
   - Camera
   - SSH
   - I2C
   - SPI
4. Select **Finish** and reboot if asked.
## Step 6: Your First GPIO Project (Blinking an LED)
 
This is the "Hello World" of Raspberry Pi hardware projects.
 
### Wiring
 
- Connect the LED's longer leg (anode) to GPIO pin 17 through a 330 ohm resistor.
- Connect the LED's shorter leg (cathode) to a Ground (GND) pin.
Always double check pin numbers using a GPIO pinout diagram for your specific Pi model before wiring anything.
 
### Code
 
Create a file called `blink.py`:
 
```python
from gpiozero import LED
from time import sleep
 
led = LED(17)
 
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
```
 
Run it with:
 
```
python3 blink.py
```
 
Press `Ctrl+C` to stop the script.
 
The `gpiozero` library comes pre-installed on Raspberry Pi OS, so no extra setup is usually needed.
 
## Step 7: Where to Go From Here
 
Once you are comfortable with the basics, here are natural next steps:
 
- Read a push button and light an LED based on its state
- Read temperature and humidity using a DHT11 or DHT22 sensor
- Control a small OLED display over I2C
- Set up a simple Python web server using Flask
- Turn your Pi into a basic home automation hub
- Explore camera modules for image capture or motion detection
See `docs/gpio-pinout.md` and `docs/troubleshooting.md` in this repository for more reference material.
 
## Common Beginner Mistakes to Avoid
 
- Using a weak or wrong power supply, which causes random crashes or a lightning bolt icon on screen
- Forgetting a resistor when wiring an LED directly to a GPIO pin
- Pulling the power cable instead of shutting down properly
- Mixing up GPIO numbering schemes (BCM vs physical/board numbering)
- Not updating the system after first boot
## License
 
This project is licensed under the MIT License. See the `LICENSE` file for details.
 
## Contributing
 
This is a learning-focused repository. If you find an error or want to add a beginner-friendly section, feel free to open an issue or a pull request. 
 
