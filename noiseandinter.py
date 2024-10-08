import numpy as np
import matplotlib.pyplot as plt

# Generate a clean signal
time = np.linspace(0, 1, 500)
clean_signal = np.sin(2 * np.pi * 10 * time)

# Adding noise to the signal (simulating interference)
noise = np.random.normal(0, 0.3, clean_signal.shape)
noisy_signal = clean_signal + noise

# Plotting clean and noisy signals
plt.figure(figsize=(8, 4))

plt.plot(time, clean_signal, label='Clean Signal', color='blue', linewidth=2)
plt.plot(time, noisy_signal, label='Noisy Signal (Interference)', color='red', linestyle='--', linewidth=2)

# Labeling and formatting
plt.title("Noise and Interference on Signal", fontsize=14, weight='bold')
plt.xlabel("Time (s)", fontsize=12)
plt.ylabel("Amplitude", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
