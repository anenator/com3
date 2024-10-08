import matplotlib.pyplot as plt
import numpy as np

# Parameters
time_kbps = np.arange(0, 10, 1)
data_rate_kbps = 1000
received_bits_kbps = data_rate_kbps * (1 + 0.001) * time_kbps

time_mbps = np.arange(0, 10, 1)
data_rate_mbps = 1_000_000
received_bits_mbps = data_rate_mbps * (1 + 0.001) * time_mbps

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# 1 kbps Plot
ax1.plot(time_kbps, received_bits_kbps, label='Received Bits at 1 kbps', color='blue', linewidth=2)
ax1.set_title("Impact of Clock Speed Variance at 1 kbps")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Bits Received")
ax1.axhline(data_rate_kbps * time_kbps[-1], color='red', linestyle='--', label='Sent Bits at 1 kbps')
ax1.legend()
ax1.set_xlim(0, 10)
ax1.grid()

# 1 Mbps Plot
ax2.plot(time_mbps, received_bits_mbps, label='Received Bits at 1 Mbps', color='green', linewidth=2)
ax2.set_title("Impact of Clock Speed Variance at 1 Mbps")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Bits Received")
ax2.axhline(data_rate_mbps * time_mbps[-1], color='orange', linestyle='--', label='Sent Bits at 1 Mbps')
ax2.legend()
ax2.set_xlim(0, 10)
ax2.grid()

plt.tight_layout()
plt.show()
