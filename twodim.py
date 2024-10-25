from tabulate import tabulate
import re

# ANSI escape codes for color formatting
RED = "\033[91m"
ENDC = "\033[0m"  # To end the colored formatting

# Function to strip ANSI color codes from strings
def strip_color_codes(value):
    """
    Strip ANSI color codes from a string so it can be used in calculations.
    If the value is already an integer, return it as is.
    """
    if isinstance(value, str):
        ansi_escape = re.compile(r'(?:\x1B[@-_][0-?]*[ -/]*[@-~])')
        return ansi_escape.sub('', value)
    return value  # Return the value as-is if it's already an integer

def calculate_row_parity(matrix, parity_type='even'):
    """
    Add parity bits to each row in the matrix.
    """
    for row in matrix:
        parity_bit = 0
        for bit in row:
            parity_bit ^= bit
        if parity_type == 'even':
            row.append(f"{RED}{parity_bit}{ENDC}")
        elif parity_type == 'odd':
            row.append(f"{RED}{parity_bit ^ 1}{ENDC}")

def calculate_column_parity(matrix, parity_type='even'):
    """
    Add a parity row at the bottom of the matrix.
    """
    num_cols = len(matrix[0])
    parity_row = []
    for col in range(num_cols):
        parity_bit = 0
        for row in matrix:
            # Strip color codes before numeric calculation
            parity_bit ^= int(strip_color_codes(row[col]))
        if parity_type == 'even':
            parity_row.append(f"{RED}{parity_bit}{ENDC}")
        elif parity_type == 'odd':
            parity_row.append(f"{RED}{parity_bit ^ 1}{ENDC}")
    matrix.append(parity_row)

def two_dimensional_parity_check(matrix, parity_type='even'):
    """
    Generate a 2D parity matrix and verify its integrity.
    """
    # Copy matrix and add parity bits
    parity_matrix = [row[:] for row in matrix]
    calculate_row_parity(parity_matrix, parity_type)
    calculate_column_parity(parity_matrix, parity_type)

    return parity_matrix

def check_parity(matrix, parity_type='even'):
    """
    Check if a given 2D parity matrix has any errors.
    """
    # Verify row parity
    for row in matrix[:-1]:
        row_parity = sum(int(strip_color_codes(bit)) for bit in row[:-1]) % 2
        expected_parity = 0 if parity_type == 'even' else 1
        if int(strip_color_codes(row[-1])) != (expected_parity if row_parity == 0 else expected_parity ^ 1):
            return "Error detected in row parity"

    # Verify column parity
    num_cols = len(matrix[0])
    for col in range(num_cols - 1):
        col_parity = sum(int(strip_color_codes(matrix[row][col])) for row in range(len(matrix) - 1)) % 2
        expected_parity = 0 if parity_type == 'even' else 1
        if int(strip_color_codes(matrix[-1][col])) != (expected_parity if col_parity == 0 else expected_parity ^ 1):
            return "Error detected in column parity"

    return "No errors detected"

def main():
    # Example data matrix 
    data = [
        [1, 1, 0, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [0, 1, 1, 1, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 1]
    ]

    # Calculate 2D parity and display the matrix
    parity_matrix = two_dimensional_parity_check(data, 'even')
    print("2D Parity Matrix with Red Parity Bits:")
    print(tabulate(parity_matrix, tablefmt="grid"))

    # Check parity and print result
    result = check_parity(parity_matrix, 'even')
    print("\nParity Check Result:", result)

if __name__ == "__main__":
    main()
