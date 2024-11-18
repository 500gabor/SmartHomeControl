import serial

# Default serial port and baud rate
DEFAULT_PORT = "COM3"
DEFAULT_BAUD_RATE = 115200


def parse_input_states(response):
    """
    Parse input states from a CAN response message.
    """
    if len(response) < 7 or not response.startswith('t'):
        return False


    can_id = response[1:4]  # Extract CAN ID
    data = response[5:]     # Extract data payload

    print(f"CAN ID: {can_id}, Data: {data}")
    # Parse input states from data (e.g., binary representation of bytes)
    if len(data) >= 2:
        byte0 = int(data[:2], 16)
        byte1 = int(data[2:4], 16) if len(data) >= 4 else 0

        inputs = {}
        for i in range(8):
            inputs[f"DI{i}"] = (byte0 >> i) & 1  # Extract bit for DI0-DI7
        for i in range(8, 16):
            inputs[f"DI{i}"] = (byte1 >> (i - 8)) & 1  # Extract bit for DI8-DI15

        return inputs


def read_input_states():
    """
    Continuously read and parse input states from the CAN device.
    """
    try:
        with serial.Serial(DEFAULT_PORT, DEFAULT_BAUD_RATE, timeout=1) as ser:
            print(f"Listening for input states on {DEFAULT_PORT} at {DEFAULT_BAUD_RATE} baud...")
            try:
                # Read CAN message from serial port
                response = ser.read(100).decode('utf-8').strip()
                if response:
                    print(f"Received from CAN: {response}")
                    return parse_input_states(response)
            except KeyboardInterrupt:
                print("Stopped listening for input states.")
    except serial.SerialException as e:
        print(f"Error communicating with {DEFAULT_PORT}: {e}")


if __name__ == "__main__":
    read_input_states()
