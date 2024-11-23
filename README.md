# Control Lights and Read Inputs for CAN Devices

This project contains a custom Python library designed for interacting with CAN devices via a serial connection, mainly designed to be a POC(Proof Of Concept) in the topic:
- **control_lights.py**: Sends commands to control connected CAN device.
- **read_inputs.py**: Reads and parses input states from a CAN device.
- **visualize_floorplan.py**: Visualizes a home with smart devices.
- **temperature_controller.py**: An example file for Node-RED https communication, used to send a random temperature value to a custom HTTP end-point.

As a proof of concept project, the scripts currently uses hard coded default values for BIT and BAUD-RATE settings, also using the COM3 port. 
- Bits per second: 115200
- Baud-Rate: 125k

## Features
- Send CAN messages to control devices.
- Parse and display input states received from the CAN device.
- View the state of connected devices using a matplotlib visualization
- Flexible and customizable for different CAN setups.

---

## Installation
- Navigate to the root folder of the project using your preferred terminal
- Install requirements using **pip install -r requirements.txt**
- Install the library using **pip install .** (the . is part of the command too)

### Prerequisites
- Python 3.6 or later with pip
- Hardware to communicate with, my setup insisted of a CANUSB device, a CANopen GCAN4032 with two switches as input dummies and a power supply.

---

## Using of the library

After installation, the following commands can be executed from your preferred terminal:

### Commands:

1. **control_devices arg:command** Use this command to control connected devices.
**Example:** control_devices t20220000
2. **read_data** Reads the DI states on the GCAN device
3. **visualize_floorplan** Using the read_data commmand, visualizes the input states using a dummy matplotlib home visualization.
4. **set_temp**  Sends a dummy value for Node-RED https communication, used to send a random temperature value to a custom HTTP end-point.