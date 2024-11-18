# Control Lights and Read Inputs for CAN Devices

This project includes two Python scripts designed for interacting with CAN devices via a serial connection:
- **control_lights.py**: Sends commands to control lights connected to a CAN device.
- **read_inputs.py**: Reads and parses input states from a CAN device.

## Features
- Send CAN messages to control devices.
- Parse and display input states received from the CAN device.
- Flexible and customizable for different CAN setups.

---

## Installation

### Prerequisites
- Python 3.6 or later
- Serial communication library `pyserial`

Install dependencies using:

```bash
pip install pyserial