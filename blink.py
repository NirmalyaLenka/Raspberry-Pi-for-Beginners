"""
Basic LED blink example for Raspberry Pi.

Wiring:
    LED anode (long leg)  -> GPIO17 (through a 330 ohm resistor)
    LED cathode (short leg) -> GND

Run with:
    python3 blink.py
Stop with Ctrl+C
"""

from gpiozero import LED
from time import sleep

led = LED(17)

try:
    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)
except KeyboardInterrupt:
    print("Stopped by user")
