import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

path = 'Dossier_project_data_articles/'

# Load data with relevant columns
data = pd.read_csv(path+'specTCL93.txt', delim_whitespace=True, header=None, usecols=[0, 1, 8],
                   names=['degree', 'radial_order', 'eigenfrequency'])

# Data for degrees l = 0, 1, and 2
filtered_data = data[data['degree'].isin([0, 1, 2])]



# Plotting the main figure
fig, ax = plt.subplots(figsize=(10, 6))
for degree in [0, 1, 2]:
    subset = filtered_data[filtered_data['degree'] == degree]
    ax.plot(subset['radial_order'], subset['eigenfrequency'], marker='o', label=f'Degree {degree}')

# Labeling and customization for the main plot
ax.set_xlabel('Radial Order')
ax.set_ylabel('Eigenfrequency (mHz)')
ax.set_title('Eigenfrequency vs. Radial Order for Degrees l=0, 1, and 2')
ax.legend(title="Degree")
ax.grid()

# Creating an inset for the zoomed-in area
axins = inset_axes(ax, width="30%", height="30%", loc='lower right')  # Customize size and location
for degree in [0, 1, 2]:
    subset = filtered_data[filtered_data['degree'] == degree]
    axins.plot(subset['radial_order'], subset['eigenfrequency'], marker='o', label=f'Degree {degree}')

# Set limits for the zoomed-in view
axins.set_xlim(0, 10)
axins.set_ylim(0, 2)

# Labeling the inset
#axins.set_xlabel('Radial Order')
#axins.set_ylabel('Eigenfrequency (mHz)')
#axins.grid()

plt.tight_layout()

# Show the plot
#plt.show()

plt.savefig('radial_frequencies.png')
plt.close()










# Load data with relevant columns
data2 = pd.read_csv(path+'specTCL93l03.txt', delim_whitespace=True, header=None, usecols=[0, 1, 8],
                    names=['degree', 'radial_order', 'eigenfrequency'])

# Data for degrees l = 0, 1, and 2
filtered_data2 = data2[data2['degree'].isin([0, 1, 2])]

# Plotting the main figure
fig, ax = plt.subplots(figsize=(10, 6))
for degree in [0, 1, 2]:
    subset2 = filtered_data2[filtered_data2['degree'] == degree]  # Corrected to filtered_data2
    ax.plot(subset2['radial_order'], subset2['eigenfrequency'], marker='o', label=f'Degree {degree}')

# Labeling and customization for the main plot
ax.set_xlabel('Radial Order')
ax.set_ylabel('Eigenfrequency (mHz)')
ax.set_title('Eigenfrequency vs. Radial Order for Degrees l=0, 1, and 2')
ax.legend(title="Degree")
ax.grid()

# Creating an inset for the zoomed-in area
axins = inset_axes(ax, width="30%", height="30%", loc='lower right')  # Customize size and location
for degree in [0, 1, 2]:
    subset2 = filtered_data2[filtered_data2['degree'] == degree]
    axins.plot(subset2['radial_order'], subset2['eigenfrequency'], marker='o', label=f'Degree {degree}')

# Set limits for the zoomed-in view
axins.set_xlim(0, 10)
axins.set_ylim(0, 2)

# Optional: Uncomment to label the inset axes
# axins.set_xlabel('Radial Order')
# axins.set_ylabel('Eigenfrequency (mHz)')
# axins.grid()

plt.tight_layout()

# Show the plot
#plt.show()

plt.savefig('radial_frequencies_l.png')
plt.close()