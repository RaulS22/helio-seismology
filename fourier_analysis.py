import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft

# Load data
path = 'Dossier_project_data_articles/'

time_series_1_1 = np.genfromtxt(path+'data2_calib1_pm1_960411_961010.dat')
time_series_1_2 = np.genfromtxt(path+'data2_calib1_pm2_960411_961010.dat')
time_series_2_1 = np.genfromtxt(path+'data2_calib2_pm1_960411_961010.dat')
time_series_2_2 = np.genfromtxt(path+'data2_calib2_pm2_960411_961010.dat')

time_series_1_1 = time_series_1_1.flatten()
time_series_1_2 = time_series_1_2.flatten()
time_series_2_1 = time_series_2_1.flatten()
time_series_2_2 = time_series_2_2.flatten()


# Performing the Fourier Transform

fft_1_1 = fft.fft(time_series_1_1)
fft_1_2 = fft.fft(time_series_1_2)
fft_2_1 = fft.fft(time_series_2_1)
fft_2_2 = fft.fft(time_series_2_2)

# Frequency array
N = len(time_series_1_1)
f = np.fft.fftfreq(N)


#Only plotting the positive frequencies

mask = f > 0
f = f[mask]
fft_1_1 = fft_1_1[mask]
fft_1_2 = fft_1_2[mask]
fft_2_1 = fft_2_1[mask]
fft_2_2 = fft_2_2[mask]


# Plotting the Fourier Transform
plt.figure(figsize=(18, 10))

plt.subplot(2, 2, 1)
plt.plot(f, np.abs(fft_1_1))
plt.title('Fourier Transform of Time Series 1 Calib 1')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(2, 2, 2)
plt.plot(f, np.abs(fft_1_2))
plt.title('Fourier Transform of Time Series 2 Calib 1')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(2, 2, 3)
plt.plot(f, np.abs(fft_2_1))
plt.title('Fourier Transform of Time Series 1 Calib 2')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(2, 2, 4)
plt.plot(f, np.abs(fft_2_2))
plt.title('Fourier Transform of Time Series 2 Calib 2')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()

plt.tight_layout()
plt.savefig('Fourier_Transform.png')
plt.close()
