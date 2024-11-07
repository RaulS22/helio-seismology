import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.fft as fft



# Load data
path = 'Dossier_project_data_articles/'

time_series_2_2 = np.genfromtxt(path+'data2_calib2_pm2_960411_961010.dat') #Only the one that matters
time_series_2_2 = time_series_2_2.flatten()

# Performing the Fourier Transform

fft_2_2 = fft.fft(time_series_2_2)

# Frequency array
N = len(time_series_2_2)
f = np.fft.fftfreq(N)

# Normalizing by total energy (sum of squared magnitudes)
fft_2_2_normalized_energy = np.abs(fft_2_2) / np.sqrt(np.sum(np.abs(fft_2_2)**2))

# Filter positive frequencies
positive_frequencies = f > 0
fft_2_2_normalized_energy_positive = fft_2_2_normalized_energy[positive_frequencies]
f_positive = f[positive_frequencies]


# Select frequency range between 
freq_range_mask = (f_positive >= 0.03) & (f_positive <= 0.07)
f_selected = f_positive[freq_range_mask]
fft_selected = fft_2_2_normalized_energy_positive[freq_range_mask]


# Plotting the normalized Fourier Transform (with respect to energy) 
plt.figure(figsize=(12, 6))
plt.plot(f_selected, fft_selected)
plt.title('Normalized Fourier Transform of PM2 Calib 2 (0.03-0.07 Hz)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Normalized Power')
plt.savefig('FFT_normalized.png')
plt.close()
