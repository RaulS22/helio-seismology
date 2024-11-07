import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.fft as fft
from scipy.optimize import curve_fit


# Load data
path = 'Dossier_project_data_articles/'
time_series_2_2 = np.genfromtxt(path + 'data2_calib2_pm1_960411_961010.dat').flatten()

# Performing the Fourier Transform
fft_2_2 = fft.fft(time_series_2_2)

# Frequency array
N = len(time_series_2_2)
f = np.fft.fftfreq(N) / 2  # Adjust for frequency doubling issue

# Normalizing by total energy (sum of squared magnitudes)
fft_2_2_normalized_energy = np.abs(fft_2_2) / np.sqrt(np.sum(np.abs(fft_2_2)**2))

# Filter positive frequencies
positive_frequencies = f > 0
fft_2_2_normalized_energy_positive = fft_2_2_normalized_energy[positive_frequencies]
f_positive = f[positive_frequencies] * 1e6  # Convert to µHz

# Select frequency range between 
freq_range_mask = (f_positive >= 18000) & (f_positive <= 30000)
f_selected = f_positive[freq_range_mask]
fft_selected = fft_2_2_normalized_energy_positive[freq_range_mask]

# Plotting the normalized Fourier Transform (with respect to energy)
plt.figure(figsize=(12, 6))
plt.plot(f_selected, fft_selected)
plt.title('Normalized Fourier Transform of PM1 Calib 2')
plt.xlabel('Frequency (µHz)')
plt.ylabel('Normalized Power')
plt.savefig('FFT_normalized.png')
plt.close()



#Load data
path = 'a09/'

data = pd.read_csv(path+'freqs_summary.txt', delim_whitespace=True, header=None, usecols=[0, 2, 4],
                    names=['eigenfrequency', 'degree', 'radial_order'], skiprows=6)

data['eigenfrequency'] *= 1e1



# Filter data to include only frequencies in the interval 
filtered_data = data[(data['eigenfrequency'] >= 18000) & (data['eigenfrequency'] <= 30000)]


# Plotting the eigenfrequencies as vertical lines for the filtered data
plt.figure(figsize=(12, 6))

plt.plot(f_selected, fft_selected)

# Group by degree and plot a vertical line for each eigenfrequency
for degree in sorted(filtered_data['degree'].unique()):
    degree_data = filtered_data[filtered_data['degree'] == degree]
    
    # Plot a vertical line for each eigenfrequency
    for _, row in degree_data.iterrows():
        plt.axvline(x=row['eigenfrequency'], color=plt.cm.viridis(degree / max(filtered_data['degree'])),
                    label=f'l={degree}' if _ == degree_data.index[0] else "", linewidth=1)

# Customize the plot
plt.title('Vertical Lines Representing Scaled Eigenfrequencies for Each Degree (l)', fontsize=14)
plt.xlabel('Frequency (Hz)', fontsize=12)  # Updated units to µHz
plt.ylabel('Radial Order', fontsize=12)
plt.legend(title="Degree (l)", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)


plt.savefig('Eigenfrequencies.png')
plt.close()
