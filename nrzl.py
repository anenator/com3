import matplotlib.pyplot as plt
import numpy as np

# Data for the sent signal (inverted where 0 goes up and 1 goes down)
sent_signal = np.array([0, 1, 0, 0, 1, 1, 1, 0])
time_steps_sent = np.arange(len(sent_signal) + 1)  # Add 1 to include the end of the signal
inverted_signal = np.array([1, 0, 1, 1, 0, 0, 0, 1])  # Inverted signal
inverted_signal_extended = np.append(inverted_signal, 1)  # Append 1 for better plotting at the end

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

# First subplot (inverted and shortened magenta signal)
ax1.step(time_steps_sent, 0.5 * inverted_signal_extended, where='post', color='magenta', linewidth=2)  # Shortened amplitude
ax1.set_title("Inverted Unipolar NRZ (Shortened)")
ax1.set_ylabel("Amplitude")
ax1.set_yticks([0, 0.5])  # Adjusted y-ticks for inverted signal
ax1.set_yticklabels(['V/2', '0'])  # Tick labels for inverted signal
ax1.grid(False)

# Add vertical lines, bit value annotations, and an arrow in the center
for i in range(len(inverted_signal)):
    ax1.axvline(time_steps_sent[i], color='black', linestyle='--', linewidth=0.8)
    ax1.text((time_steps_sent[i] + time_steps_sent[i + 1]) / 2, 0.25, str(inverted_signal[i]), 
             fontsize=12, color='black', ha='center', va='center')

# Add arrow at the center
ax1.annotate("", xy=(4, 0.5), xytext=(4, 0), arrowprops=dict(arrowstyle="<->", lw=1.5))

# Second subplot (inverted original signal)
ax2.step(time_steps_sent, inverted_signal_extended, where='post', color='magenta', linewidth=2)
ax2.set_title("Inverted Unipolar NRZ (Original)")
ax2.set_ylabel("Amplitude")
ax2.set_xlabel("Time")
ax2.set_yticks([0, 1])  # Original y-ticks
ax2.set_yticklabels(['V', '0'])  # Tick labels for inverted signal
ax2.grid(False)

# Add vertical lines, bit value annotations, and an arrow in the center
for i in range(len(inverted_signal)):
    ax2.axvline(time_steps_sent[i], color='black', linestyle='--', linewidth=0.8)
    ax2.text((time_steps_sent[i] + time_steps_sent[i + 1]) / 2, 0.5, str(inverted_signal[i]), 
             fontsize=12, color='black', ha='center', va='center')

# Add arrow at the center
ax2.annotate("", xy=(4, 1), xytext=(4, 0), arrowprops=dict(arrowstyle="<->", lw=1.5))

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
