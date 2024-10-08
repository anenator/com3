import matplotlib.pyplot as plt
import numpy as np

# Update time steps to match the lengths of the signals
time_steps_sent = np.arange(len(np.array([1, 0, 1, 1, 0, 0, 0, 1])) + 1)  # Add 1 to include the end of the signal
time_steps_received = np.arange(len(np.array([1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1])) + 1)  # Add 1 here too

sent_signal = np.append(np.array([1, 0, 1, 1, 0, 0, 0, 1]), 0)  # Append 0 to make the line go down at the end
received_signal = np.append(np.array([1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1]), 0)  # Same for the received signal

# Plot the figure with two subplots to replicate the original image with binary y-axis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

# Plot 'Sent' signal with binary y-axis
ax1.step(time_steps_sent, sent_signal, where='post', color='magenta', linewidth=2)
ax1.set_title("a. Sent")
ax1.set_xlabel("Time")
ax1.set_ylabel("Amplitude")
ax1.set_yticks([0, 1])
ax1.set_yticklabels([0, 1])
ax1.set_xticks([]) 
ax1.grid(False)

# Add dashed vertical lines and bit value annotations in the center for 'Sent' signal
for i in range(len(time_steps_sent) - 1):
    ax1.axvline(time_steps_sent[i], color='black', linestyle='--', linewidth=0.8)
    ax1.text((time_steps_sent[i] + time_steps_sent[i+1]) / 2, 0.5, str(sent_signal[i]), 
             fontsize=12, color='black', ha='center')

# Plot 'Received' signal with binary y-axis
ax2.step(time_steps_received, received_signal, where='post', color='magenta', linewidth=2)
ax2.set_title("b. Received")
ax2.set_xlabel("Time")
ax2.set_ylabel("Amplitude")
ax2.set_yticks([0, 1])
ax2.set_yticklabels([0, 1])
ax2.set_xticks([]) 
ax2.grid(False)

# Add dashed vertical lines and bit value annotations in the center for 'Received' signal
for i in range(len(time_steps_received) - 1):
    ax2.axvline(time_steps_received[i], color='black', linestyle='--', linewidth=0.8)
    ax2.text((time_steps_received[i] + time_steps_received[i+1]) / 2, 0.5, str(received_signal[i]), 
             fontsize=12, color='black', ha='center')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
