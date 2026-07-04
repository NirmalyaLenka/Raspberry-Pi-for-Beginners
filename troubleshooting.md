# Troubleshooting Guide

Common problems beginners run into, and how to fix them.

## Pi Does Not Boot / No Display Output

- Confirm the SD card was flashed correctly and was not ejected too early.
- Try a different HDMI cable or port.
- Make sure the power supply provides enough current (check the official specification for your Pi model).
- Look for a colored status light pattern near the power LED, which can indicate specific boot errors.

## Pi Boots but Keeps Restarting or Freezing

- This is often a power supply issue. Use the official Raspberry Pi power adapter if possible.
- Check for a lightning bolt icon on screen, which indicates undervoltage.
- Remove any unnecessary USB devices that may be drawing too much power.

## Cannot Connect via SSH

- Confirm SSH was enabled during imaging or via `sudo raspi-config`.
- Confirm the Pi and your computer are on the same network.
- Try connecting using the Pi's IP address instead of its hostname.
- Restart the Pi and try again after it has fully booted.

## Wi-Fi Not Connecting

- Double check the Wi-Fi name and password entered during imaging.
- Some Pi models only support 2.4GHz Wi-Fi, not 5GHz networks.
- Try running `sudo raspi-config` and re-entering Wi-Fi details manually.

## GPIO Code Runs but Nothing Happens

- Confirm you are using the correct pin numbering scheme (BCM vs physical).
- Double check wiring, especially the resistor and LED polarity.
- Run the script with `sudo` if you get a permissions error, though this is usually not required with `gpiozero`.
- Test the LED and resistor on their own with a simple battery to confirm the LED itself is not faulty.

## SD Card Corruption

- Always shut down properly using `sudo shutdown now` before removing power.
- Consider using a higher endurance microSD card if you are logging data frequently.
- Keep a backup image of a working SD card setup once your environment is configured.

## Still Stuck

Search the exact error message you are seeing along with "Raspberry Pi" on a search engine. The Raspberry Pi community is large, and most beginner issues have already been documented somewhere.
