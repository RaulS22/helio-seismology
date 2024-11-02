import pandas as pd
import matplotlib.pyplot as plt

# Load the data, skipping initial non-data lines (comments and headers)
data = pd.read_csv('basu_09.txt', delim_whitespace=True, comment='#', header=None,
                   names=['r_Rsun', 'sound_speed', 'Sigma_c'], skiprows=9)

# Convert columns to numeric, coercing errors to NaN and dropping any rows with NaNs
data = data.apply(pd.to_numeric, errors='coerce').dropna()

A = 100  # Arbitrary scaling factor for error bars

# Plotting with error bars
plt.figure(figsize=(10, 6))
plt.errorbar(data['r_Rsun'], data['sound_speed'], yerr=data['Sigma_c']*A, color='blue',
             ecolor='k', elinewidth=2, capsize=2, label='Sound Speed Profile with Uncertainty')

# Labeling the plot
plt.xlabel('Radial Position (r / R_sun)')
plt.ylabel('Sound Speed (cm/s)')
plt.title('Sound Speed Profile with Uncertainty')
plt.grid()
plt.legend()
plt.show()
