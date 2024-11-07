import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import pandas as pd

def plot_eigenfrequencies(data, dataset_name, scale_frequency=False):
    # Apply scaling if needed
    if scale_frequency:
        data['eigenfrequency'] *= 1e-3
    
    # Filter data for degrees l = 0, 1, 2, and 3
    filtered_data = data[data['degree'].isin([0, 1, 2, 3])]
    

# Print data info for debugging
    #print(f"\nPlotting data for {dataset_name}:")


    for degree in [0, 1, 2, 3]:
        subset = filtered_data[filtered_data['degree'] == degree].sort_values(by='radial_order')
        #print(f"Degree {degree} - Data points:\n{subset[['radial_order', 'eigenfrequency']]}\n")

    # Create main plot
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ['tab:blue', 'orange', 'g', 'r', 'tab:blue', 'orange', 'g', 'r', 'tab:blue', 'orange', 'g', 'r']  # Colors for each degree

    for i, degree in enumerate([0, 1, 2, 3]):
        subset = filtered_data[filtered_data['degree'] == degree].sort_values(by='radial_order')
        if not subset.empty:
            ax.plot(subset['radial_order'], subset['eigenfrequency'], marker='o', color=colors[i],
                    linestyle='-', label=f'Degree {degree}')
        else:
            print(f"No data found for Degree {degree} in {dataset_name}.")

    # Customize main plot
    ax.set_xlabel('Radial Order')
    ax.set_ylabel('Eigenfrequency (mHz)')
    ax.set_title(f'Eigenfrequency vs. Radial Order for Degrees l=0, 1, 2, and 3 ({dataset_name})')
    ax.legend(title="Degree")
    ax.grid()

    # Create inset for zoomed area
    axins = inset_axes(ax, width="40%", height="40%", loc='lower right')
    for i, degree in enumerate([0, 1, 2, 3]):
        subset = filtered_data[filtered_data['degree'] == degree].sort_values(by='radial_order')
        if not subset.empty:
            axins.plot(subset['radial_order'], subset['eigenfrequency'], marker='o', color=colors[i], linestyle='-')

    # Set limits for zoomed-in view
    axins.set_xlim(5, 8)
    axins.set_ylim(1, 1.6)
    
    # Save plot
    plt.savefig(f'radial_frequencies_{dataset_name}.png')
    plt.close()

# Paths and filenames
datasets = {
    'TCL93': 'Dossier_project_data_articles/specTCL93l03.txt',
    'gs98': 'gs98/freqs_summary.txt',
    'a09': 'a09/freqs_summary.txt'
}

# Column names and skiprows specific to each dataset
for name, path in datasets.items():
    if name == 'TCL93':
        data = pd.read_csv(path, delim_whitespace=True, header=None, usecols=[0, 1, 8],
                           names=['degree', 'radial_order', 'eigenfrequency'])
        scale_frequency = False
    else:
        data = pd.read_csv(path, delim_whitespace=True, header=None, usecols=[0, 2, 4],
                           names=['eigenfrequency', 'degree', 'radial_order'], skiprows=6)
        scale_frequency = True  # Apply frequency scaling for gs98 and a09
    
    # Plot eigenfrequencies with appropriate scaling
    plot_eigenfrequencies(data, name, scale_frequency=scale_frequency)
