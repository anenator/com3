import numpy as np
import matplotlib.pyplot as plt

fs = 8000
t_max = 0.01
t = np.linspace(0, t_max, int(fs * t_max), endpoint=False)

frequency = 4000
analog = np.sin(2 * np.pi * frequency * t)

sampled = analog[::int(fs/fs)]

t_sampled = np.linspace(0, t_max, len(sampled), endpoint=False)

plt.figure(figsize=(12, 6))

plt.plot(t, analog, 'b', label='Analog Signal')
plt.stem(t_sampled, sampled, label='Sampled Signal', linefmt='g--', basefmt=" ", markerfmt="go")

plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Analog vs Sampled Signal')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
