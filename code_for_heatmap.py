import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

df = pd.read_pickle("Corrected_responces")
corr = df.corr()

# Define a custom colormap
colors = ['#fee3d4', 'lightblue', 'gray']
custom_cmap = LinearSegmentedColormap.from_list('custom_cmap', colors, N=256)

sns.heatmap(corr, cmap=custom_cmap)
