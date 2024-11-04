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

#Only plotting the positive frequencies
mask = (f > 0.03) & (f < 0.09)
f = f[mask]
fft_2_2 = fft_2_2[mask]

# Plotting the Fourier Transform
# We're only interested in the frequencies between 0.03 and 0.09 Hz

plt.figure(figsize=(12, 6))
plt.plot(f, np.abs(fft_2_2))
plt.title('Fourier Transform of PM2 Calib 2')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()


