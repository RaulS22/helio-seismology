import pandas as pd
import matplotlib.pyplot as plt

path = 'Dossier_project_data_articles/'


# Load data with relevant columns
data = pd.read_csv(path+'specTCL93.txt', delim_whitespace=True, header=None, usecols=[0, 1, 8],
                   names=['degree', 'radial_order', 'eigenfrequency'])

# Data for degrees l = 0, 1, and 2
filtered_data = data[data['degree'].isin([0, 1, 2])]

# Plotting
plt.figure(figsize=(10, 6))
for degree in [0, 1, 2]:
    subset = filtered_data[filtered_data['degree'] == degree]
    plt.plot(subset['radial_order'], subset['eigenfrequency'], marker='o', label=f'Degree {degree}')

# Labeling and customization
plt.xlabel('Radial Order')
plt.ylabel('Eigenfrequency (mHz)')
plt.title('Eigenfrequency vs. Radial Order for Degrees l=0, 1, and 2')
plt.legend(title="Degree")
plt.grid()
plt.show()
