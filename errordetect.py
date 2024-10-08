import numpy as np
import matplotlib.pyplot as plt

# Simulated data with some errors
data = np.array([1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0])
received_data = np.array([1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0])  # Some errors in transmission

# Creating a plot to show errors
plt.figure(figsize=(8, 4))

# Original data line
plt.step(range(len(data)), data, where='mid', label='Original Data', color='blue', linewidth=2)
# Received data line with errors
plt.step(range(len(received_data)), received_data, where='mid', label='Received Data', color='red', linestyle='--', linewidth=2)

# Highlighting the error points
for i in range(len(data)):
    if data[i] != received_data[i]:
        plt.plot(i, received_data[i], 'ro', label='Error Detected' if i == 0 else "")  # Marking errors

# Labeling and formatting
plt.title("Error Detection in Transmission", fontsize=14, weight='bold')
plt.xlabel("Bit Index", fontsize=12)
plt.ylabel("Bit Value", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
