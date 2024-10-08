import matplotlib.pyplot as plt
import numpy as np

# Update time steps to match the lengths of the signals
time_steps_sent = np.arange(len(np.array([1, 0, 1, 1, 0])) + 1)  # Add 1 to include the end of the signal
sent_signal = np.append(np.array([1, 0, 1, 1, 0]), 0)  # Append 0 to make the line go down at the end

# Create a single subplot
fig, ax1 = plt.subplots(figsize=(8, 6))

# Plotting the sent signal
ax1.step(time_steps_sent, sent_signal, where='post', color='magenta', linewidth=2)
ax1.set_title("Unipolar NRZ")
ax1.set_ylabel("Amplitude")
ax1.set_xlabel("Time")
ax1.set_yticks([0, 1])  # Numeric y-ticks
ax1.set_yticklabels(['0', 'V'])  # Corresponding tick labels
ax1.set_xticks([])  # Hide x-axis tick labels
ax1.grid(False)

# Add vertical lines and bit value annotations
for i in range(len(sent_signal)):
    ax1.axvline(time_steps_sent[i], color='black', linestyle='--', linewidth=0.8)
    if i < len(sent_signal) - 1:  # Ensure we only label the segments where the signal changes
        ax1.text((time_steps_sent[i] + time_steps_sent[i + 1]) / 2, 0.5, str(sent_signal[i]), 
                 fontsize=12, color='black', ha='center', va='center')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
