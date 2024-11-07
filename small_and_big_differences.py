import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.fft as fft

# Comparing the data with the frequencies obtained from GYRE

path = 'gs98/'
print('gs98:')

# Load data with relevant columns
data = pd.read_csv(path+'freqs_summary.txt', delim_whitespace=True, header=None, usecols=[0, 2, 4],
                                    names=['eigenfrequency', 'degree', 'radial_order'], skiprows=6)



data['eigenfrequency'] = data['eigenfrequency'] * 1e-6  # Convert to Hz
#print(data)

"""
To calculate the large separation we need to keep l constant and vary n.
$ \Delta\nu=\nu_{n+1,l} -\nu_{n,l} $

And to calculate the small separation we need to vary both n and vary l.
$  \delta\nu=\nu_{n,l} - \nu_{n-1, l+2} $
"""

# Large separation
l = 0
n = 1
large_separation = []

for n in range(n, 55):
    
    nu_n_l = data[(data['degree'] == l) & (data['radial_order'] == n)]['eigenfrequency'].values[0]
    nu_nplus1_l = data[(data['degree'] == l) & (data['radial_order'] == n+1)]['eigenfrequency'].values[0]
    large_separation.append(nu_nplus1_l - nu_n_l)
    #print(nu_nplus1_l - nu_n_l)
    #print(nu_n_l, nu_nplus1_l)

# Convert to µHz
large_separation = np.array(large_separation) * 1e6

# errors using standard deviation
std = np.std(large_separation)
#print(std)

# Finally, we shall take the mean of the large separations (and its respective standard deviation).
mean_large_separation = np.mean(large_separation)

print(f'The Large Separation is {mean_large_separation:.2f} +- {std:.2f} µHz')

# Small separation
l=0
n=2
small_separation = []

for n in range(n, 55):
    nu_n_l = data[(data['degree'] == l) & (data['radial_order'] == n)]['eigenfrequency'].values[0]
    nu_nminus1_lplus2 = data[(data['degree'] == l+2) & (data['radial_order'] == n-1)]['eigenfrequency'].values[0]
    #print(nu_n_l, nu_nminus1_lplus2)
    #print(nu_n_l - nu_nminus1_lplus2)
    small_separation.append(nu_n_l - nu_nminus1_lplus2)

# Convert to µHz
small_separation = np.array(small_separation) * 1e6

# errors using standard deviation
std = np.std(small_separation)
#print(std)
    
print(f'The Small Separation is {np.mean(small_separation):.2f} +- {std:.2f} µHz')









# Comparing the data with the frequencies obtained from GYRE

path = 'a09/'
print('a09:')

# Load data with relevant columns
data = pd.read_csv(path+'freqs_summary.txt', delim_whitespace=True, header=None, usecols=[0, 2, 4],
                                    names=['eigenfrequency', 'degree', 'radial_order'], skiprows=6)



data['eigenfrequency'] = data['eigenfrequency'] * 1e-6  # Convert to Hz
#print(data)

"""
To calculate the large separation we need to keep l constant and vary n.
$ \Delta\nu=\nu_{n+1,l} -\nu_{n,l} $

And to calculate the small separation we need to vary both n and vary l.
$  \delta\nu=\nu_{n,l} - \nu_{n-1, l+2} $
"""

# Large separation
l = 0
n = 1
large_separation = []

for n in range(n, 56):
    
    nu_n_l = data[(data['degree'] == l) & (data['radial_order'] == n)]['eigenfrequency'].values[0]
    nu_nplus1_l = data[(data['degree'] == l) & (data['radial_order'] == n+1)]['eigenfrequency'].values[0]
    large_separation.append(nu_nplus1_l - nu_n_l)
    #print(nu_nplus1_l - nu_n_l)
    #print(nu_n_l, nu_nplus1_l)

# Convert to µHz
large_separation = np.array(large_separation) * 1e6

# errors using standard deviation
std = np.std(large_separation)
#print(std)

# Finally, we shall take the mean of the large separations (and its respective standard deviation).
mean_large_separation = np.mean(large_separation)

print(f'The Large Separation is {mean_large_separation:.2f} +- {std:.2f} µHz')

# Small separation
l=0
n=2
small_separation = []

for n in range(n, 56):
    nu_n_l = data[(data['degree'] == l) & (data['radial_order'] == n)]['eigenfrequency'].values[0]
    nu_nminus1_lplus2 = data[(data['degree'] == l+2) & (data['radial_order'] == n-1)]['eigenfrequency'].values[0]
    #print(nu_n_l, nu_nminus1_lplus2)
    #print(nu_n_l - nu_nminus1_lplus2)
    small_separation.append(nu_n_l - nu_nminus1_lplus2)

# Convert to µHz
small_separation = np.array(small_separation) * 1e6

# errors using standard deviation
std = np.std(small_separation)
#print(std)
    
print(f'The Small Separation is {np.mean(small_separation):.2f} +- {std:.2f} µHz')