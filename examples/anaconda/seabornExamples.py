
import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt

import seaborn as sns


tips = sns.load_dataset('tips')
print(tips.head())

#disPlot = sns.distplot(tips['total_bill'], kde= True, bins=40)
#plt.show()

# kind = hex, reg , kde, etc
#sns.jointplot(x='total_bill' , y='tip' ,data=tips, kind='reg') 
#plt.show()

#sns.pairplot(tips, hue='sex', palette='coolwater')
#plt.show()

#sns.rugplot(tips['total_bill'], kde=True)

# CATEGORY DATA
# Distribution categorical versus numerical

# by default it is the mean
#sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)

# look for variance
#plt.show()


# sns.countplot(x='sex',data=tips)

# distribution of data
# box and violin
# hue='smoker'
# sns.boxplot(x='day',y='total_bill', data=tips )

# KDE on the distribution
# hue='sex', split=True
# sns.violinplot(x='day',y='total_bill',data=tips)

# scatter plot with one categorical value
# hue='sex', split=True
#sns.stripplot(x='day',y='total_bill',data=tips,jitter=True)

# scatterplot with a violin plot
# sns.violin(x='day',y='total_bill',data=tips)
# sns.swarmplot(x='day',y='total_bill',data=tips, color='black')
# kind = bar,scatter,violin, count,etc ..
#sns.factorplot(x='day',y='total_bill',data=tips,kind='bar')


# Matrix plots

flights = sns.load_dataset('flights')

# heat maps !!
# matrix form index name and column match up revelant to both row and column
# pivot_table
tc =tips.corr()

#sns.heatmap(tc, annot=True, cmap='coolwarm')

fp = flights.pivot_table(index='month',columns='year',values='passengers')

#sns.heatmap(fp, cmap='magma', linecolor='black', linewidth=0.5)

# cluster Map!

#sns.clustermap(fp, cmap='coolwarm', standard_scale=1)

iris = sns.load_dataset('iris')

# sns.pairplot(iris)

#grid = sns.PairGrid(iris)

#grid.map(plt.scatter)
#grid.map_diag(sns.distplot)
#grid.map_upper(plt.scatter)
#grid.map_lower(sns.kdeplot)

#gridTips = sns.FacetGrid(data=tips,col='time',row='smoker')

#gridTips.map(sns.distplot,'total_bill','tip')


# Regression Plots

# linear model
# scatter_kws={'s':50}
#sns.lmplot(x='total_bill',y='tip',data=tips, hue='sex',markers=['o','x'])

#sns.lmplot(x='total_bill',y='tip',data=tips, col='sex', row='time')

sns.lmplot(x='total_bill',y='tip',data=tips, col='sex', hue='sex', aspect=0.6, size=8)










