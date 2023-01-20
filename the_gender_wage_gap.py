# -*- coding: utf-8 -*-
"""THE GENDER WAGE GAP

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IdHVxd7OzpfFpaCN2kxasRIbZUD64OFE
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/9_OneNumSevCatSubgroupOneObs.csv")
df.head()

# Grouped barplot
# Grouping using the the Country category:
sns.set_theme(style="whitegrid")
g = sns.catplot(data=df, kind="bar",x="Value", y="Country", hue="TIME", palette="dark", alpha=.7, height=15)
g.despine(left=True)
g.set_axis_labels("gender wage gap (%)")

# Grouping using the the year category:
sns.set_theme(style="whitegrid")
g = sns.catplot(data=df, kind="bar",x="Value", y="TIME", hue="Country", palette="dark", alpha=.7, height=8)
g.despine(left=True)
g.set_axis_labels("gender wage gap (%)")

# Parallel coordinates plot
from pandas.plotting import parallel_coordinates
g=parallel_coordinates(df,'Country', colormap=plt.get_cmap("Set2"))