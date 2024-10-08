import matplotlib.pyplot as plt

# Data representing different schemes
encoding_schemes = ['Low Complexity', 'Moderate Complexity', 'High Complexity']
bandwidth = [50, 75, 100]  # Bandwidth usage
error_rate = [15, 8, 2]    # Error rate for each scheme

fig, ax1 = plt.subplots()

# Plotting bandwidth usage
ax1.bar(encoding_schemes, bandwidth, color='cyan', label='Bandwidth Usage')
ax1.set_ylabel('Bandwidth (MHz)', color='cyan', fontsize=12)
ax1.set_ylim(0, 120)

# Overlaying error rates on the same plot
ax2 = ax1.twinx()
ax2.plot(encoding_schemes, error_rate, color='red', marker='o', linestyle='--', label='Error Rate')
ax2.set_ylabel('Error Rate (%)', color='red', fontsize=12)
ax2.set_ylim(0, 20)

# Title and formatting
plt.title('Trade-off Between Complexity, Bandwidth and Error Rate', fontsize=14, weight='bold')
plt.grid(True)
plt.show()
