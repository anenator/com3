import matplotlib.pyplot as plt
import numpy as np

max_freq = 4000
bits = 8

freqs = np.linspace(0, max_freq, 400)
sampling_rates = 2 * freqs
bit_rates = sampling_rates * bits

plt.figure(figsize=(10, 6))
plt.plot(freqs, sampling_rates, label='Sampling Rate', color='c')
plt.plot(freqs, bit_rates, label='Bit Rate', color='m')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Rate')
plt.title('Frequency, Sampling Rate, and Bit Rate')
plt.ylim(0, max(bit_rates) * 1.2)
plt.legend()
plt.margins(x=0)
plt.yticks(np.arange(0, 66000, 5000))
plt.grid()

plt.show()
