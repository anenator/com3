def calculate_crc32(message, polynomial="100000100110000010001110110110111"):
    # Append 32 zero bits to the message for CRC-32 calculation
    message_padded = message + '0' * 32

    # Convert the message and polynomial to lists of bits (integers)
    message_bits = list(map(int, message_padded))
    polynomial_bits = list(map(int, polynomial))

    # Perform the division to calculate the CRC-32 remainder
    for i in range(len(message_bits) - 32):
        if message_bits[i] == 1:  # Perform XOR only if the bit is 1
            for j in range(len(polynomial_bits)):
                message_bits[i + j] ^= polynomial_bits[j]  # XOR in place

    # Extract the CRC-32 remainder (last 32 bits after division)
    remainder = ''.join(map(str, message_bits[-32:]))
    
    return remainder

def main():
    # Example binary message (32-bit CRC expects binary input)
    message = "11010110111111100011001100101110"  # Example binary message

    # Calculate the CRC-32 checksum
    crc32 = calculate_crc32(message)

    # Append the CRC-32 remainder to the original message
    transmitted_message = message + crc32

    print(f"Original Message: {message}")
    print(f"Polynomial (CRC-32): 0x04C11DB7")
    print(f"Message with appended zeros: {message + '0' * 32}")
    print(f"CRC-32 Remainder: {crc32}")
    print(f"Transmitted Message: {transmitted_message}")

if __name__ == "__main__":
    main()
