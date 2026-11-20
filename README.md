# Raspberry Pi for Beginners

A practical first-boot and GPIO introduction for students and hobbyists. This repository contains a general Raspberry Pi setup guide plus one small Python LED-blink example and two reference documents.

## What is in this repository

| Path | Purpose |
|---|---|
| `README.md` | OS setup, SSH, basic Linux commands, interfaces, and first GPIO example |
| `blink.py` | GPIO Zero LED blink program using BCM GPIO17 |
| `gpio-pinout.md` | BCM versus physical pin numbering and electrical safety notes |
| `troubleshooting.md` | Common boot, SSH, Wi-Fi, GPIO, and SD-card issues |
| `LICENSE (7)` | Checked-in MIT license text; the filename is non-standard |

The reference files are at the repository root. There is no `docs/` directory in the current tree.

## What you need

- A Raspberry Pi model supported by a current Raspberry Pi OS image
- A microSD card appropriate for the board and workload
- A power supply suitable for the exact Pi model
- Network access for updates and optional SSH
- A monitor/keyboard for initial setup, or a correctly configured headless setup

Use [Raspberry Pi Imager](https://www.raspberrypi.com/software/) to write the OS. **Select the target storage carefully:** writing an image erases the selected device. Configure a username, password, network, hostname, and SSH only as needed. Do not publish passwords or Wi-Fi credentials.

## First boot and SSH

1. Insert the imaged microSD card.
2. Connect the monitor, keyboard, network, and other peripherals before applying power.
3. Complete the initial OS setup.
4. Update the package lists and installed packages:

   ```bash
   sudo apt update
   sudo apt full-upgrade
   sudo reboot
   ```

5. If SSH was enabled and networking is configured, connect from another computer using the configured username and hostname or IP address:

   ```bash
   ssh username@raspberrypi.local
   ```

   Replace the example username and hostname with your actual settings. If name resolution fails, find the Pi's IP address in your router or use the address assigned to the device.

Shut the Pi down cleanly with `sudo shutdown now` before disconnecting power; abrupt removal can corrupt the SD card.

## Basic Linux commands

| Command | Purpose |
|---|---|
| `pwd` | Print the current directory |
| `ls` | List files |
| `cd foldername` | Change directory |
| `mkdir foldername` | Create a directory |
| `sudo apt update` | Refresh package metadata |
| `sudo reboot` | Restart the Pi |
| `sudo shutdown now` | Shut down cleanly |

Use `sudo raspi-config` only when you need to change an available system option such as SSH, I²C, or SPI. Current camera support is generally auto-detected on modern Raspberry Pi OS; an old tutorial's camera-enable menu may not exist on your OS version.

## First GPIO project: blink an LED

### Hardware and wiring

- One LED
- One 330 Ω current-limiting resistor
- Breadboard and jumper wires

Connect **BCM GPIO17** (physical header pin 11 on the standard 40-pin header) through the resistor to the LED anode (long leg). Connect the LED cathode (short leg) to a GND pin. Verify the pinout for your exact board before wiring.

Raspberry Pi GPIO uses **3.3 V logic**. Never connect a GPIO pin directly to 5 V, and never connect an LED without a current-limiting resistor. Power off the Pi before changing wiring.

### Run the checked-in script

From the repository root, the existing `blink.py` program uses `gpiozero.LED(17)` and toggles the LED once per second:

```bash
python3 blink.py
```

Press **Ctrl+C** to stop. The script catches a keyboard interrupt and prints a stop message.

On Raspberry Pi OS, `gpiozero` is often available already. If the import fails, install the distribution package:

```bash
sudo apt install -y python3-gpiozero
```

The example is intended for a Raspberry Pi with the LED connected as described; it is not a desktop simulation.

## Troubleshooting and pin references

- See [GPIO pinout reference](gpio-pinout.md) for BCM versus physical numbering and electrical safety.
- See [troubleshooting guide](troubleshooting.md) for boot, power, SSH, Wi-Fi, GPIO, and SD-card checks.
- If the LED stays off, check the selected numbering scheme, GPIO17 wiring, resistor, LED polarity, and ground.
- If SSH fails, confirm both devices are on the same network and use the current IP address.
- If the Pi restarts or freezes, check the power supply against the specification for your board.

## License and verification status

The checked-in file is [`LICENSE (7)`](./LICENSE%20(7)); its text names **Shubham** as copyright holder. Confirm provenance and permission before redistributing this repository or its contents. The file has not been renamed.

The README and linked root-level documents were reviewed against the visible tree and `blink.py`. No Pi boot, package installation, SSH session, or physical GPIO test was performed.

## Maintenance & Audit

- **Audit date:** 20 November 2026
- **Documentation status:** README paths and first GPIO instructions aligned with the actual root-level files.
- **Verification boundary:** Documentation only; no OS or hardware test is claimed.
