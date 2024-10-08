import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Defining the data and signal
time = np.linspace(0, 3, 600)
signal = np.where(time < 1, 1, np.where(time > 2, 0.5, 0))

# Recreating the plot with vertical lines going up
fig, ax = plt.subplots()

# Plotting the signal
ax.plot(time, signal, color='magenta', linewidth=2)

# Adding extended vertical lines upwards only
ax.vlines([1, 2], ymin=0, ymax=[1, 0.5], color='magenta', linewidth=2)

# Marking the data elements
ax.text(1.5, 1.3, '1101', fontsize=15, ha='center', fontweight='semibold')


# Adding dashed vertical lines for separation with controlled height
ax.vlines(x=0, ymin=1.06, ymax=1.5, color='black', linestyle='--', linewidth=1)
ax.vlines(x=3, ymin=0.56, ymax=1.5, color='black', linestyle='--', linewidth=1)

# Adding additional text elements
ax.text(1.5, 1.15, '4 data elements', fontsize=13, ha='center')
ax.text(1.5, -0.3, '3 signal elements', fontsize=12, ha='center')

# Adding a double-headed arrow between the data elements
ax.annotate('', xy=(0, 1.1), xytext=(3, 1.1),
            arrowprops=dict(facecolor='black', arrowstyle='<->', linewidth=1))

# Adding a blue rectangle around the line at y=0
# Rectangle coordinates: (1, ymin), width=1, height=1
rect = patches.Rectangle((0, 1.05), 1, -0.1, linewidth=2, edgecolor='blue', facecolor='blue', alpha=0.3)
rect2 = patches.Rectangle((1, 0.05), 1, -0.1, linewidth=2, edgecolor='blue', facecolor='blue', alpha=0.3)
rect3 = patches.Rectangle((2, 0.55), 1, -0.1, linewidth=2, edgecolor='blue', facecolor='blue', alpha=0.3)
ax.add_patch(rect)
ax.add_patch(rect2)
ax.add_patch(rect3)

# Formatting the plot
ax.set_ylim(-0.5, 1.5)
ax.set_yticks([])
ax.set_xticks([0.5, 1.5, 2.5])
ax.set_xticklabels(['', '', ''])
ax.axhline(0.5, color='black', linewidth=1)

# Removing axis for a cleaner look
ax.set_axis_off()

# Displaying the plot
plt.show()
