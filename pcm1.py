import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

def plot_stem_signal(t, sampled_times, sampled_values):
    fig, ax = plt.subplots(figsize=(10, 6))
    markerline, stemlines, baseline = ax.stem(sampled_times, sampled_values, basefmt='k-', linefmt='m', markerfmt='mo')
    plt.setp(stemlines, 'linewidth', 1)

    f = interp1d(sampled_times, sampled_values, kind='cubic')
    t_new = np.linspace(sampled_times[0], sampled_times[-1], 300)
    y_smooth = f(t_new)

    ax.plot(t_new, y_smooth, 'k--', linewidth=1)
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_title('a. Ideal Sampling')
    ax.set_yticks([-1, 0, 1])
    ax.set_ylim(-1.5, 1.5)

    middle_x = (sampled_times[1] + sampled_times[2]) / 2
    ax.annotate('', xy=(sampled_times[1], 0.5), xytext=(sampled_times[2], 0.5), arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(middle_x, 0.55, 'Tₛ', ha='center', fontsize=12)

    ax.annotate('Analog Signal', xy=(t_new[150], y_smooth[150]), xytext=(t_new[150] + 0.5, y_smooth[150] + 0.5), 
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

    plt.show()

sampled_values = [-0.4, 0.4, 0.9, 1, 0.6, -0.15, -0.5, -0.4, -0.2]
t = np.linspace(0, 2 * np.pi, 100)
Ts = (2 * np.pi) / len(sampled_values)
sampled_times = np.arange(0, 2 * np.pi, Ts)

plot_stem_signal(t, sampled_times, sampled_values)
