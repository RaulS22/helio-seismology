import numpy as np
import matplotlib.pyplot as plt

"""
The time series data has two calibrations: calib1 and calib2. 
Further information can be found in the README file.
The data should be read across then down.
"""

# Load data

path = 'Dossier_project_data_articles/'

time_series_1_1 = np.genfromtxt(path+'data2_calib1_pm1_960411_961010.dat')
time_series_1_2 = np.genfromtxt(path+'data2_calib2_pm1_960411_961010.dat')
time_series_2_1 = np.genfromtxt(path+'data2_calib1_pm2_960411_961010.dat')
time_series_2_2 = np.genfromtxt(path+'data2_calib2_pm2_960411_961010.dat')

time_series_1_1 = time_series_1_1.flatten()
time_series_1_2 = time_series_1_2.flatten()
time_series_2_1 = time_series_2_1.flatten()
time_series_2_2 = time_series_2_2.flatten()

#print(time_series_1_1)
#print(time_series_1_2)
#print(time_series_2_1)
#print(time_series_2_2)

#print(len(time_series_1_1))

# Generate time arrays
time_array_1_1 = np.arange(0, len(time_series_1_1))
time_array_1_2 = np.arange(0, len(time_series_1_2))
time_array_2_1 = np.arange(0, len(time_series_2_1))
time_array_2_2 = np.arange(0, len(time_series_2_2))


'''
Concerting the time arrays to days
since there were 183 days of data
'''

time_array_1_1 = time_array_1_1 /4320
time_array_1_2 = time_array_1_2 /4320
time_array_2_1 = time_array_2_1 /4320
time_array_2_2 = time_array_2_2 /4320


# Plot the single time series
plt.figure(figsize=(18, 10))

plt.subplot(2, 2, 1)
plt.plot(time_array_1_1, time_series_1_1)
plt.title('PM1 Calib 1')
plt.xlabel('Time (days)')
plt.ylabel('Velocity dispersion $(m/s)$')
plt.grid()

plt.subplot(2, 2, 2)
plt.plot(time_array_1_2, time_series_1_2)
plt.title('PM1 Calib 2')
plt.xlabel('Time (days)')
plt.ylabel('Velocity dispersion $(m/s)$')
plt.grid()

plt.subplot(2, 2, 3)
plt.plot(time_array_2_1, time_series_2_1)
plt.title('PM2 Calib 1')
plt.xlabel('Time (days)')
plt.ylabel('Velocity dispersion $(m/s)$')
plt.grid()

plt.subplot(2, 2, 4)
plt.plot(time_array_2_2, time_series_2_2)
plt.title('PM2 Calib 2')
plt.xlabel('Time (days)')
plt.ylabel('Velocity dispersion $(m/s)$')
plt.grid()

plt.tight_layout()
plt.savefig('Time_series.png')
plt.close()



