import matplotlib.pyplot as plt
import numpy as np

# Variables
c = 1  # Assume a constant case factor
data_rates = np.linspace(1000, 10000, 100)  # Data rate in bits per second
ratios = [1, 2, 4]  # Different r values (how many data elements per signal element)

# Plotting
plt.figure(figsize=(8, 6))

for r in ratios:
    baud_rate = c * data_rates * (1 / r)
    plt.plot(data_rates, baud_rate, label=f'r = {r}')

# Customizing the plot
plt.title('Baud Rate vs Data Rate for Different Ratios (r)', fontsize=14, weight='bold')
plt.xlabel('Data Rate (bits per second)', fontsize=12)
plt.ylabel('Baud Rate (bauds)', fontsize=12)
plt.legend(title='Data Elements per Signal Element (r)', fontsize=10)
plt.grid(True)

# Show plot
plt.show()
