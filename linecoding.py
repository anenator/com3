import matplotlib.pyplot as plt
import numpy as np

# Binary data sequence (1s and 0s)
binary_data = [0, 1, 0, 1, 1, 0, 1]

# Time points for each bit
t = np.arange(0, len(binary_data) * 2)  

# Voltage levels for the signal (+1 for "1", 0 for "0")
voltage_levels = [1 if bit == 1 else 0 for bit in binary_data]

# Repeat voltage levels to match step-like behavior
voltage_levels_repeated = np.repeat(voltage_levels, 2)

# Create the plot
fig, ax = plt.subplots()

# Plot the digital signal (step plot)
ax.step(t, voltage_levels_repeated, where='post', color='magenta', linewidth=2)

# Annotate "Encoder" and "Decoder"
ax.text(-0.5, 1.5, 'Encoder', fontsize=12, ha='center', bbox=dict(facecolor='yellow', alpha=0.5))
ax.text(-0.5, 2, 'Sender', fontsize=12, ha='center', bbox=dict(facecolor='gray', alpha=0.5))
ax.text(len(t) + 0.5, 1.5, 'Decoder', fontsize=12, ha='center', bbox=dict(facecolor='yellow', alpha=0.5))
ax.text(len(t) + 0.5, 2, 'Receiver', fontsize=12, ha='center', bbox=dict(facecolor='gray', alpha=0.5))

# Display binary data below the signal
ax.text(-0.8, 1.1, '0, 1, 0, 1, 1, 0, 1', fontsize=12, ha='center', color='magenta', bbox=dict(facecolor='white', alpha=0.5))
ax.text(len(t) + 0.8, 1.1, '0, 1, 0, 1, 1, 0, 1', fontsize=12, ha='center', color='magenta', bbox=dict(facecolor='white', alpha=0.5))

# Add arrows
ax.annotate('', xy=(-0.035, 0.990), xytext=(-0.035, 0.85), 
            arrowprops=dict(arrowstyle='<-', lw=1.5), 
            xycoords='axes fraction', textcoords='axes fraction')

ax.annotate('', xy=(1.035, 0.990), xytext=(1.035, 0.855), 
            arrowprops=dict(arrowstyle='->', lw=1.5), 
            xycoords='axes fraction', textcoords='axes fraction')

# Mark binary data below the signal
for i, bit in enumerate(binary_data):
    ax.text(i * 2 + 1, 0.5, str(bit), fontsize=12, ha='center')

# Extend the voltage levels to reach the end of the graph
voltage_levels_repeated = np.append(voltage_levels_repeated, voltage_levels[-1]) 
t_extended = np.arange(0, len(binary_data) * 2 + 1) 

# Add the extended signal (final step)
ax.step(t_extended, voltage_levels_repeated, where='post', color='magenta', linewidth=2)

# Add an arrow across the graph with text "Link"
ax.text(len(t) / 2, 1.6, 'Link', fontsize=20, ha='center', color='black')
ax.annotate('', xy=(len(t), 1.5), xytext=(0, 1.5),
            arrowprops=dict(arrowstyle='->', lw=1.5, color='black'))

# Adding labels
ax.set_ylim(-1, 2)
ax.set_xlim(0, 14) 
ax.set_yticks([0, 1])
ax.set_yticklabels(['Low (0) -V', 'High (1) +V'])
ax.set_xlabel('Time', fontsize=20)
ax.set_title('Line Coding', fontsize=20, weight='bold')

# Display the plot
plt.grid(True)
plt.show()
