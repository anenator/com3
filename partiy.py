from tabulate import tabulate

def calculate_parity_bit(binary_sequence, parity_type='even'):
    """
    Calculate the parity bit for a given binary sequence.
    Returns 0 or 1 depending on the parity type (even or odd).
    """
    ones_count = sum(binary_sequence)
    is_even = (ones_count % 2 == 0)
    return 0 if (parity_type == 'even' and is_even) or (parity_type == 'odd' and not is_even) else 1

def append_parity_bit(binary_sequence, parity_type='even'):
    """
    Appends the appropriate parity bit to the binary sequence.
    """
    parity_bit = calculate_parity_bit(binary_sequence, parity_type)
    return binary_sequence + [parity_bit]

def check_parity(binary_sequence, parity_type='even'):
    """
    Checks the parity of the binary sequence and returns True if it matches the expected parity, False otherwise.
    """
    expected_parity_bit = calculate_parity_bit(binary_sequence[:-1], parity_type)
    actual_parity_bit = binary_sequence[-1]
    return expected_parity_bit == actual_parity_bit

def simulate_error(binary_sequence, error_type='flip_middle'):
    """
    Simulates an error in the binary sequence.
    - 'flip_middle' swaps the middle two bits if length is even.
    - 'flip_last' flips the last bit.
    """
    sequence = binary_sequence.copy()
    if error_type == 'flip_middle' and len(sequence) % 2 == 0:
        mid1, mid2 = len(sequence) // 2 - 1, len(sequence) // 2
        sequence[mid1], sequence[mid2] = sequence[mid2], sequence[mid1]
    elif error_type == 'flip_last':
        sequence[-1] ^= 1  # Flip the last bit
    return sequence

def main():
    data = [1, 0, 1, 1, 0, 0, 0]
    parity_type = 'even'

    # Scenario 1: No Error
    sent_sequence = append_parity_bit(data, parity_type)
    no_error_received = sent_sequence.copy()
    is_error_free = check_parity(no_error_received, parity_type)

    # Scenario 2: Error Undetected (flip middle)
    undetected_error_received = simulate_error(sent_sequence, 'flip_middle')
    is_undetected_error = check_parity(undetected_error_received, parity_type)

    # Scenario 3: Error Detected (flip last)
    detected_error_received = simulate_error(sent_sequence, 'flip_last')
    is_detected_error = check_parity(detected_error_received, parity_type)

    # Display results in a table
    table_data = [
        ["Original Data", data],
        ["Sent Sequence with Parity", sent_sequence],
        ["Received (No Error)", no_error_received, "Error-Free" if is_error_free else "Error Detected"],
        ["Received (Undetected Error)", undetected_error_received, "Error-Free" if is_undetected_error else "Error Detected"],
        ["Received (Detected Error)", detected_error_received, "Error-Free" if is_detected_error else "Error Detected"]
    ]

    print(tabulate(table_data, headers=["Description", "Sequence", "Status"], tablefmt="grid"))

if __name__ == "__main__":
    main()
