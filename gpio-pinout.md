# GPIO Pinout Reference

The Raspberry Pi has a 40-pin GPIO header (on all current models). This document explains how to read it safely.

## Two Numbering Systems

There are two common ways pins are referred to in code and diagrams:

- **BCM numbering**: Refers to the actual Broadcom chip pin number (for example GPIO17). Most Python libraries like `gpiozero` and `RPi.GPIO` use this by default.
- **Physical/Board numbering**: Refers to the pin's physical position on the 40-pin header, counting 1 to 40.

These two numbers are different for the same physical pin, which is a common source of beginner confusion. Always check which numbering scheme a tutorial or library expects before wiring.

## General Layout Notes

- Pin 1 is usually marked on the board near a small square pad or a white dot.
- Power pins (5V and 3.3V) and Ground (GND) pins are fixed and cannot be reprogrammed.
- Most other pins can be used as general-purpose input or output, and some have special functions (I2C, SPI, UART, PWM).

## Safety Rules

1. Never connect a GPIO pin directly to 5V. GPIO pins operate at 3.3V logic level and can be damaged by higher voltages.
2. Always use a current-limiting resistor with LEDs.
3. Double check polarity before connecting sensors or modules.
4. Power off the Pi before wiring or rewiring circuits when possible.
5. When in doubt, search for the official pinout diagram for your exact Raspberry Pi model before starting a new project.

## Recommended Reference

Search for "Raspberry Pi GPIO pinout" along with your exact model name (for example "Raspberry Pi 4 GPIO pinout") to get an accurate, up-to-date diagram, since pin layouts can vary slightly between models.
