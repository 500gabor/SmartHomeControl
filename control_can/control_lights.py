import serial
import sys

# Default serial port and baud rate
DEFAULT_PORT = "COM3"
DEFAULT_BAUD_RATE = 115200


def send_can_message(message):
    """
    Send a CAN message to the default serial port with predefined settings.
    """
    try:
        # pre-operational state: t00020202
        # operational state: t00020102
        with serial.Serial(DEFAULT_PORT, DEFAULT_BAUD_RATE, timeout=1) as ser:
            if message != 't00020202':
                ser.write('t00020102\r'.encode('utf-8'))  # Setting to operational state
                ser.write('S4\r'.encode('utf-8'))  # Setting BAUD rate of the CANUSB to 115200
                ser.write('O\r'.encode('utf-8'))  # Opens the CAN bus for communication.
            ser.write(message.encode('utf-8'))  # Send the message
            print(f"Message sent: {message.strip()}")

            # Read response if available
            response = ser.read(100).decode('utf-8')
            if response:
                print(f"Response: {response}")
            else:
                print("No response received.")
    except serial.SerialException as e:
        print(f"Error communicating with {DEFAULT_PORT}: {e}")


def main():
    # Ensure a message argument is provided
    if len(sys.argv) < 2:
        print("Usage: python control_lights.py <CAN_COMMAND>")
        print("Example: python control_lights.py t20220000")
        sys.exit(1)

    # Get the CAN command from the command-line arguments
    can_command = sys.argv[1]

    # Ensure it ends with a carriage return
    if not can_command.endswith('\r'):
        can_command += '\r'

    # Send the command
    send_can_message(can_command)


if __name__ == "__main__":
    main()
