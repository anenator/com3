def calculate_crc_with_steps(message, polynomial):
    # Append zero bits to the message (length of polynomial - 1)
    message_padded = message + '0' * (len(polynomial) - 1)

    # Convert to lists of integers for easier manipulation
    message_bits = list(map(int, message_padded))
    polynomial_bits = list(map(int, polynomial))
    
    # Perform the division to get the CRC remainder
    print(f"Initial message with appended zeros: {''.join(map(str, message_bits))}")
    
    for i in range(len(message)):
        # Only divide if the current bit is 1
        if message_bits[i] == 1:
            print(f"\nStep {i+1}:")
            print(f"Current bits being divided: {''.join(map(str, message_bits[i:i+len(polynomial_bits)]))}")
            
            # XOR with the polynomial and update the message_bits
            for j in range(len(polynomial_bits)):
                message_bits[i + j] ^= polynomial_bits[j]
                
            print(f"Message after XOR: {''.join(map(str, message_bits))}")
    
    # Extract the remainder (last bits after division)
    remainder = ''.join(map(str, message_bits[-(len(polynomial) - 1):]))

    print(f"\nFinal Remainder: {remainder}")
    
    return remainder

def main():
    # Example usage
    message = "1101011011"
    polynomial = "10011"

    # Calculate the CRC
    crc = calculate_crc_with_steps(message, polynomial)

    # Append the CRC to the original message
    transmitted_message = message + crc

    print(f"\nOriginal Message: {message}")
    print(f"Polynomial: {polynomial}")
    print(f"Message with appended zeros: {message + '0' * (len(polynomial) - 1)}")
    print(f"CRC Remainder: {crc}")
    print(f"Transmitted Message: {transmitted_message}")

if __name__ == "__main__":
    main()
