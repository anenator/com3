import matplotlib.pyplot as plt
import numpy as np

def plot_stem_signal(t, sampled_times, sampled_values, original_values, D):
    fig, ax = plt.subplots(figsize=(10, 6))
    markerline, stemlines, baseline = ax.stem(sampled_times, sampled_values, basefmt='k-', linefmt='r', markerfmt='mo')
    plt.setp(stemlines, 'linewidth', 1)

    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude (D)')
    ax.set_title('Ideal Sampling')

    y_ticks = [-4*D, -3*D, -2*D, -D, 0, D, 2*D, 3*D, 4*D]
    ax.set_yticks(y_ticks)
    y_tick_labels = [f'{int(tick / D)}D' if tick != 0 else '0' for tick in y_ticks]
    ax.set_yticklabels(y_tick_labels)
    ax.set_ylim(-5*D, 5*D)

    for i, y in enumerate(np.arange(-4*D, 5*D, D)):
        color = 'blanchedalmond' if i % 2 == 0 else 'cornflowerblue'
        ax.fill_between([sampled_times[0], sampled_times[-1]], y - D, y + D, color=color, alpha=0.5, zorder=0)

    for x, y, orig_value in zip(sampled_times, sampled_values, original_values):
        ax.annotate(f'{orig_value:.2f}', (x, y), textcoords="offset points", xytext=(10, 0), ha='left')

    indices = np.where(np.isclose(sampled_values, -6.0))[0]
    time_of_minus_6 = sampled_times[indices[0]] if indices.size > 0 else sampled_times[-1]
    ax.set_xlim(0, time_of_minus_6)
    plt.show()

D = 1.0
original_values = [-6.1, 7.5, 16.2, 19.7, 11.0, -5.5, -11.3, -9.4, -6.0]
scaled_sampled_values = [value / 5 for value in original_values]
t = np.linspace(0, 2 * np.pi, 100)
Ts = (2 * np.pi) / len(original_values)
sampled_times = np.arange(0, 2 * np.pi, Ts)

plot_stem_signal(t, sampled_times, scaled_sampled_values, original_values, D)

sampled_values = [-6.1, 7.5, 16.2, 19.7, 11.0, -5.5, -11.3, -9.4, -6.0]
D = 5
normalized_pam_values = [value / D for value in sampled_values]
quantization_levels = np.array([-4, -3, -2, -1, 0, 1, 2, 3, 4])
midpoints = (quantization_levels[:-1] + quantization_levels[1:]) / 2
quantization_level_map = {midpoint: i for i, midpoint in enumerate(midpoints)}
normalized_quantized_values = []

for value in normalized_pam_values:
    floor_index = np.searchsorted(quantization_levels, value, side='right') - 1
    ceiling_index = floor_index + 1
    floor_value = quantization_levels[floor_index] if floor_index >= 0 else quantization_levels[0]
    ceiling_value = quantization_levels[ceiling_index] if ceiling_index < len(quantization_levels) else quantization_levels[-1]
    normalized_quantized_value = (floor_value + ceiling_value) / 2
    normalized_quantized_values.append(normalized_quantized_value)

normalized_error = [quant - pam for pam, quant in zip(normalized_pam_values, normalized_quantized_values)]
quantization_codes = [quantization_level_map[value] for value in normalized_quantized_values]
encoded_words = [format(code, '03b') for code in quantization_codes]

for i, (pam, quant, error, code, word) in enumerate(zip(normalized_pam_values, normalized_quantized_values, normalized_error, quantization_codes, encoded_words)):
    print(f"{i+1:5} | {pam:14.4f} | {quant:20.4f} | {error:15.4f} | {code:16} | {word}")
