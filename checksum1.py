import socket
import struct
import threading

def compute_complement(value, bits=8):
    """Return one's complement of a value with specified bit length."""
    return value ^ ((1 << bits) - 1)

def wrap_sum(value, bits=8):
    """Return a wrapped sum within a specified bit size."""
    while value >= (1 << bits):
        value = (value & ((1 << bits) - 1)) + (value >> bits)
    return value

def calculate_checksum(data):
    """Compute checksum as one's complement of 8-bit wrapped sum."""
    total = sum(data)
    wrapped = wrap_sum(total)
    return compute_complement(wrapped)

def is_checksum_valid(data, checksum):
    """Verify checksum by ensuring sum of data and checksum results in zero."""
    total = sum(data) + checksum
    wrapped = wrap_sum(total)
    return compute_complement(wrapped) == 0

def create_connection(host, port, is_server=False):
    """Create a socket connection; bind if server, otherwise connect as client."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if is_server:
        s.bind((host, port))
        s.listen()
    else:
        s.connect((host, port))
    return s

def send_message(data, host='localhost', port=12345):
    """Send data with checksum to receiver, waiting for verification feedback."""
    # Assuming `data` is already a list of integers like [7, 11, 12, 0, 6]
    checksum = calculate_checksum(data)
    payload = data + [checksum]  # Append checksum to data
    
    try:
        with create_connection(host, port) as s:
            print("Sender: Connected to receiver.")
            # Packing integers as bytes
            packed_data = struct.pack(f'{len(payload)}B', *payload)
            s.sendall(packed_data)
            print(f"Sender: Sent data with checksum {checksum}")

            # Await receiver response
            response = s.recv(1024).decode()
            if response == "VALID":
                print("Sender: Transmission successful; checksum validated.")
            else:
                print("Sender: Checksum invalid, transmission error.")
    except socket.error as e:
        print(f"Sender: Connection error - {e}")

def receive_message(host='localhost', port=12345):
    """Receive data from sender, verify checksum, and respond with validation status."""
    try:
        with create_connection(host, port, is_server=True) as s:
            print("Receiver: Waiting for connection from sender.")
            conn, addr = s.accept()
            with conn:
                print(f"Receiver: Connected by {addr}")
                data = conn.recv(1024)
                unpacked_data = list(struct.unpack(f'{len(data)}B', data))
                print(f"Receiver: Received data: {unpacked_data}")

                # Separate message and checksum
                data_content, received_checksum = unpacked_data[:-1], unpacked_data[-1]
                print(f"Receiver: Extracted checksum: {received_checksum}")

                # Validate checksum
                if is_checksum_valid(data_content, received_checksum):
                    print("Receiver: Checksum valid.")
                    conn.sendall(b"VALID")
                else:
                    print("Receiver: Checksum invalid.")
                    conn.sendall(b"INVALID")
    except socket.error as e:
        print(f"Receiver: Connection error - {e}")

if __name__ == "__main__":
    # Example input: list of integers [7, 11, 12, 0, 6]
    message = [7, 11, 12, 0, 6]
    print(f"Original Message: {message}")

    # Start receiver in a daemon thread
    receiver_thread = threading.Thread(target=receive_message, daemon=True)
    receiver_thread.start()

    # Execute sender
    send_message(message)

    # Wait for receiver thread to complete (only if it's not a daemon)
    receiver_thread.join()
