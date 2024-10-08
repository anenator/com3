import matplotlib.pyplot as plt
import numpy as np

# Define parameters
time_kbps = np.arange(0, 10, 1)  # Time in seconds for 1 kbps
data_rate_kbps = 1000  # Data rate in bits per second
received_bits_kbps = data_rate_kbps * (1 + 0.001) * time_kbps  # Extra bits received due to faster clock

time_mbps = np.arange(0, 10, 1)  # Time in seconds for 1 Mbps
data_rate_mbps = 1_000_000  # Data rate in bits per second
received_bits_mbps = data_rate_mbps * (1 + 0.001) * time_mbps  # Extra bits received due to faster clock

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Plot for 1 kbps
ax1.plot(time_kbps, received_bits_kbps, label='Received Bits at 1 kbps', color='blue', linewidth=2)
ax1.set_title("Impact of Clock Speed Variance at 1 kbps")
ax1.set_xlabel("Time (seconds)")
ax1.set_ylabel("Number of Bits Received")
ax1.grid()
ax1.axhline(data_rate_kbps * time_kbps[-1], color='red', linestyle='--', label='Sent Bits at 1 kbps')
ax1.legend()
ax1.set_xlim(0, 10)  # Show only the first 10 seconds

# Plot for 1 Mbps
ax2.plot(time_mbps, received_bits_mbps, label='Received Bits at 1 Mbps', color='green', linewidth=2)
ax2.set_title("Impact of Clock Speed Variance at 1 Mbps")
ax2.set_xlabel("Time (seconds)")
ax2.set_ylabel("Number of Bits Received")
ax2.grid()
ax2.axhline(data_rate_mbps * time_mbps[-1], color='orange', linestyle='--', label='Sent Bits at 1 Mbps')
ax2.legend()
ax2.set_xlim(0, 10)  # Show only the first 10 seconds

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
