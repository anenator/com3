import numpy as np
import matplotlib.pyplot as plt

# Constants
sampling_rate = 1000  # High sample rate for accurate sine wave
signal_frequency = 1  # Frequency of the sine wave

# Time vector covering 3 periods of the wave
wave_duration = 1 / signal_frequency * 3  
time_base = np.linspace(0, wave_duration, sampling_rate, endpoint=False)  # Time base for accurate sine wave

# Original sine wave
sine_wave = np.sin(2 * np.pi * signal_frequency * time_base)

# Different sampling rates
nyquist_rate = 2 * signal_frequency  # Nyquist rate
oversample_rate = 4 * signal_frequency  # Oversampling rate
undersample_rate = signal_frequency  # Undersampling rate

# Time points for different sampling rates
nyquist_time = np.arange(0.25, wave_duration, 1 / int(nyquist_rate))  # Sampled at Nyquist rate
oversample_time = np.arange(0, wave_duration, 1 / int(oversample_rate))  # Oversampled points
undersample_time = np.arange(0.25, wave_duration, 0.75 / int(undersample_rate))  # Undersampled points

# Sine values at sampled points
nyquist_samples = np.sin(2 * np.pi * signal_frequency * nyquist_time)
oversample_samples = np.sin(2 * np.pi * signal_frequency * oversample_time)
undersample_samples = np.sin(2 * np.pi * signal_frequency * undersample_time)


plt.figure(figsize=(12, 12))

# Nyquist Rate Sampling 
plt.subplot(6, 1, 1)
plt.plot(time_base, sine_wave, color='magenta', label='Original Sine Wave')  
plt.plot(nyquist_time, nyquist_samples, 'ko', label='Sampled Points')  
plt.title('Nyquist Rate Sampling (fs = 2f)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.margins(x=0)
plt.xticks(np.arange(0, 3.1, 0.25))

# Nyquist Rate Sampling 
plt.subplot(6, 1, 4)
plt.plot(nyquist_time, nyquist_samples, 'r--o', label='Sampled Points Connected', markerfacecolor='black')  
plt.title('Broken Line Nyquist Rate')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.margins(x=0)
plt.xticks(np.arange(0, 3.1, 0.25))

# Oversampling 
plt.subplot(6, 1, 2)
plt.plot(time_base, sine_wave, color='magenta', label='Original Sine Wave')  
plt.plot(oversample_time, oversample_samples, 'ko', label='Sampled Points')  
plt.title('Oversampling (fs = 4f)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.margins(x=0)
plt.xticks(np.arange(0, 3.1, 0.25))

# Oversampling 
plt.subplot(6, 1, 5)
plt.plot(oversample_time, oversample_samples, 'r--o', label='Sampled Points Connected', markerfacecolor='black')  
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.margins(x=0)
plt.xticks(np.arange(0, 3.1, 0.25))

# Undersampling 
plt.subplot(6, 1, 6)
plt.plot(undersample_time, undersample_samples, 'r--o', label='Sampled Points Connected', markerfacecolor='black')  
plt.title('Broken Line Undersampling (fs = f)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.margins(x=0)
plt.xticks(np.arange(0, 3.1, 0.25))

# Undersampling 
plt.subplot(6, 1, 3)
plt.plot(time_base, sine_wave, color='magenta', label='Original Sine Wave') 
plt.plot(undersample_time, undersample_samples, 'ko', label='Sampled Points') 
plt.title('Undersampling (fs = f)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.margins(x=0)
plt.xticks(np.arange(0, 3.1, 0.25))

# Tight layout to avoid overlap
plt.tight_layout()
plt.show()
