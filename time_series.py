import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft
import pandas as pd

"""
The time series data has two calibrations: calib1 and calib2. 
Further information can be found in the README file.
The data should be read across then down.
"""

# Load data

path = 'Dossier_project_data_articles/'

data1_calib1 = pd.read_csv(path+'data2_calib1_pm1_960411_961010.dat')
data2_calib1 = pd.read_csv(path+'data2_calib1_pm2_960411_961010.dat')
data1_calib2 = pd.read_csv(path+'data2_calib2_pm1_960411_961010.dat')
data1_calib2 = pd.read_csv(path+'data2_calib2_pm2_960411_961010.dat')

# Plotting the head of the data
'''
csv_files = [data1_calib1, data2_calib1, data1_calib2, data1_calib2]
for file in csv_files:
    print(file.head())
    print('\n')
'''


# Plotting the data

# Reshape the data to create a single continuous time series
# Flatten the DataFrame into a 1D array to read across rows and down


time_series_1_1 = data1_calib1.values.flatten()
time_series_1_2 = data1_calib1.values.flatten()

time_series_2_1 = data1_calib1.values.flatten()
time_series_2_2 = data1_calib1.values.flatten()

# Plot the single time series
plt.figure(figsize=(20, 12))

plt.subplot(2, 2, 1)
plt.plot(time_series_1_1)
plt.title('Time Series 1 Calib 1')
plt.xlabel('Time')
plt.ylabel('Value')
plt.grid()

plt.subplot(2, 2, 2)
plt.plot(time_series_1_2)
plt.title('Time Series 2 Calib 1')
plt.xlabel('Time')
plt.ylabel('Value')
plt.grid()

plt.subplot(2, 2, 3)
plt.plot(time_series_2_1)
plt.title('Time Series 1 Calib 2')
plt.xlabel('Time')
plt.ylabel('Value')
plt.grid()

plt.subplot(2, 2, 4)
plt.plot(time_series_2_2)
plt.title('Time Series 2 Calib 2')
plt.xlabel('Time')
plt.ylabel('Value')
plt.grid()

plt.tight_layout()
plt.show()



