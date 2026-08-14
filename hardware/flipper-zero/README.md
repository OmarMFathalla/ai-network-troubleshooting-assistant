# Flipper Zero Hardware Lab

This directory documents my hands-on experimentation with the Flipper Zero and external development hardware as part of my Network Troubleshooting Assistant project.

## Current Objectives

- Learn serial communication between Python and physical hardware
- Detect and identify connected devices through USB/serial
- Interact with the Flipper Zero CLI
- Read device and system information programmatically
- Explore hardware diagnostics and troubleshooting
- Integrate hardware observations with Python-based diagnostic tools

## Lab Progress

### USB / Serial Communication

Successfully detected the Flipper Zero from Windows using Python and PySerial.

The device appeared as a USB serial device and communication with the serial port was successfully established.

### Flipper Zero CLI

Established communication with the Flipper Zero command-line interface and retrieved system/device information.

This demonstrates communication between:

Windows PC → Python/PySerial → USB Serial → Flipper Zero

## Hardware Backup Experiment

Performed read-only experiments with an external development board's flash memory and created a local firmware backup for recovery and research purposes.

Binary firmware dumps are intentionally excluded from this Git repository.

## Next Steps

- Automate serial device discovery with Python
- Parse Flipper Zero CLI responses
- Build structured hardware diagnostic results
- Connect hardware diagnostics to the Network Troubleshooting Assistant