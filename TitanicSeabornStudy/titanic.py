


import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
tds = sns.load('titanic')


sns.jointplot(x='fare',y='age', data=tds)

sns.distplot(titanic['fare'], kde=False, color='red', bin=35)

sns.boxplot(x='class', y='age', data=titanic, palette='rainbow')

sns.swarmplot(x='class', y='age', data=titanic, palette='rainbow')

sns.countplot(x='sex', data=titanic)


# correlation plot with heatmap

sns.heatmap(titanic.corr, cmap='coolwarm')
plt.title('titanic.corr')

g = sns.FacetGrid(data=titanic, col='sex')
g.map(sns.distplot, 'age')


