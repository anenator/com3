import matplotlib.pyplot as plt
import numpy as np

# Constants
bandwidths = np.linspace(1000, 10000, 100)  # Bandwidth in Hz
signal_levels = [2, 4, 8, 16]  # Different signal levels M (2, 4, 8, 16 levels)

# Plotting
plt.figure(figsize=(8, 6))

for M in signal_levels:
    max_data_rate = 2 * bandwidths * np.log2(M)
    plt.plot(bandwidths, max_data_rate, label=f'M = {M} levels')

# Customizing the plot
plt.title('Maximum Data Rate vs. Bandwidth According to Nyquist\'s Theorem', fontsize=14, weight='bold')
plt.xlabel('Bandwidth (Hz)', fontsize=12)
plt.ylabel('Maximum Data Rate (bits per second)', fontsize=12)
plt.legend(title='Signal Levels (M)', fontsize=10)
plt.grid(True)

# Show plot
plt.show()
