import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

'''
First, we shall plot the theotetical sound speed profile of the Sun with error bars.
We also shaw compare it to our models.
'''

###############
# Theoretical #
###############

# Load data with relevant columns
data = pd.read_csv('basu_09.txt', delim_whitespace=True, comment='#', header=None,
                   names=['r_Rsun', 'sound_speed', 'Sigma_c'], skiprows=9)

# Convert columns to numeric, coercing errors to NaN and dropping any rows with NaNs
data = data.apply(pd.to_numeric, errors='coerce').dropna()

A = 100  # Arbitrary scaling factor for error bars









################
# Solar models #
################


# File paths for both sound speed profiles
file_path_a09 = 'a09/profile22.data'
file_path_gs98 = 'gs98/profile22.data'

def load_and_process_data(file_path, radial_col=9, sound_speed_col=10):
    # Read data file and load specified columns
    data = pd.read_csv(file_path, delim_whitespace=True, header=None, skiprows=5)
    radial_position = pd.to_numeric(data[radial_col], errors='coerce')  # Logarithmic radial position
    sound_speed = pd.to_numeric(data[sound_speed_col], errors='coerce')     # Sound speed

    # Exponentiate radial position and remove NaNs
    mask = ~np.isnan(radial_position) & ~np.isnan(sound_speed)
    return radial_position[mask], sound_speed[mask]

# Load and process data for both profiles
radial_position_a09, sound_speed_a09 = load_and_process_data(file_path_a09)
radial_position_gs98, sound_speed_gs98 = load_and_process_data(file_path_gs98)




'''

# Plotting the two graphs side by side
plt.figure(figsize=(18, 6))

# First subplot: Theoretical sound speed profile with uncertainty
plt.subplot(1, 2, 1)
plt.errorbar(data['r_Rsun'], data['sound_speed'], yerr=data['Sigma_c'] * A, color='blue',
             ecolor='k', elinewidth=2, capsize=2, label='Sound Speed Profile with Uncertainty')
plt.xlabel('Radial Position (r / R_sun)')
plt.ylabel('Sound Speed (cm/s)')
plt.title('Sound Speed Profile with Uncertainty')
plt.grid()
plt.legend()

# Second subplot: Comparison of sound speed profiles from A09 and GS98
plt.subplot(1, 2, 2)
plt.plot(radial_position_a09, sound_speed_a09, label="A09 Sound Speed")
plt.plot(radial_position_gs98, sound_speed_gs98, label="GS98 Sound Speed")
plt.xlabel("Radial Position (r / R_sun)")
plt.ylabel("Sound Speed (cm/s)")
plt.title("Comparison of Sound Speed Profiles")
plt.legend()
plt.grid(True)

# Adjust layout and show the plot
plt.tight_layout()
plt.show()

'''











########################
# \frac{\delta_{c}}{c} #
########################


# Interpolation for the models
f_exp = interp1d(data['r_Rsun'], data['sound_speed'], kind='cubic', fill_value='extrapolate')
f_gs98 = interp1d(radial_position_gs98, sound_speed_gs98, kind='cubic', fill_value='extrapolate')
f_a09 = interp1d(radial_position_a09, sound_speed_a09, kind='cubic', fill_value='extrapolate')

# Create radial positions for residual plots
r_vals = np.linspace(0, 1, 100)

# Calculate residuals
residuals_gs98 = (f_exp(r_vals) - f_gs98(r_vals)) / f_gs98(r_vals)
residuals_a09 = (f_exp(r_vals) - f_a09(r_vals)) / f_a09(r_vals)

## First Plot: Theoretical sound speed profile with uncertainty
plt.figure(figsize=(10, 6))
plt.errorbar(data['r_Rsun'], data['sound_speed'], yerr=data['Sigma_c'] * A,
             ecolor='k', elinewidth=2, capsize=2, label='Sound Speed Profile with Uncertainty (uncertainty x100)')
plt.plot(radial_position_a09, sound_speed_a09, label="A09 Sound Speed", linestyle='--')
plt.plot(radial_position_gs98, sound_speed_gs98, label="GS98 Sound Speed", linestyle='--')
plt.xlabel('Radial Position (r / R_sun)')
plt.ylabel('Sound Speed (cm/s)')
plt.title('Sound Speed Profile with Uncertainty')
plt.grid()
plt.legend()

plt.savefig('speed_of_sound_profile.png')  # Save the first plot
plt.close()  # Close the figure




# Second Plot: Comparison of residuals
plt.figure(figsize=(10, 6))
plt.plot(r_vals, residuals_gs98, label='Residuals GS98', color='orange')
plt.plot(r_vals, residuals_a09, label='Residuals A09', color='green')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  
plt.xlabel('Radial Position (r / R_sun)')
plt.ylabel(r'$\delta c / c$')
plt.title('Residuals Comparison')
plt.legend()
plt.grid()

plt.savefig('residuals_comparison.png')  # Save the second plot
plt.close()  # Close the figure





# Third plot: Delta for the range y=[−0.04, 0.04] and x=[0, 1]
plt.figure(figsize=(10, 6))
plt.plot(r_vals, residuals_gs98, label='Residuals GS98', color='orange')
plt.plot(r_vals, residuals_a09, label='Residuals A09', color='green')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Line at y=0
plt.ylim(-0.04, 0.04)  # Set y limits for this plot
plt.xlim(0, 1)  # Set x limits for this plot
plt.xlabel('Radial Position (r / R_sun)')
plt.ylabel(r'$\delta c / c$')
plt.title('Residuals Comparison for y=[-0.04, 0.04] and x=[0, 1]')
plt.legend()
plt.grid()

plt.savefig('residuals_delta_range1.png')  # Save the first plot
plt.close()




# Fourth plot: Delta for the range y=[−1, 1] and x=[0.8, 1]
plt.figure(figsize=(10, 6))
plt.plot(r_vals, residuals_gs98, label='Residuals GS98', color='orange')
plt.plot(r_vals, residuals_a09, label='Residuals A09', color='green')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Line at y=0
plt.ylim(-1, 1)  # Set y limits for this plot
plt.xlim(0.8, 1)  # Set x limits for this plot
plt.xlabel('Radial Position (r / R_sun)')
plt.ylabel(r'$\delta c / c$')
plt.title('Residuals Comparison for y=[-1, 1] and x=[0.8, 1]')
plt.legend()
plt.grid()

plt.savefig('residuals_delta_range2.png')  # Save the second plot
plt.close()