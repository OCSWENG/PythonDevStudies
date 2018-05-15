import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('USA_Housing.csv')

print(df.head())

print(df.info())

print(df.columns)

sns.pairplot(df)
plt.plot()

sns.distplot(df["Price"], bin=100)

correlation = df.corr()
print(correlation)
sns.heatmap(correlation, annot=True)

# train linear regression 
# split into x array and y array
# text info can't be used without natural language processor



X = df[['AVG. Area Income','AVG. Area House Age','Avg. Area Number of Rooms','Avg. Area Number of Bedrooms','Area Population']]

# trying to predict
y = df['Price']

# common is 0.3 30% random_state is a seed
# Features
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.4, random_state=101)



lm = LinearRegression()
# Train data
lm.fit(X_train, y_train)


print(lm.intercept_)
print(lm.coef_)

cdf = pd.DataFrame(lm.coef, X.columns, columns['Coef'])

# one data point move causes the price to move
print(cdf)

#from sklearn.datasets import load_boston

#boston = load_boston()

# Predictions

predictions = lm.predict(X_test)
print(predictions)

# expect a line a straight one is perfect
plt.scatter(y_test, predictions)

sns.distplot((y_test-predictions))

from sklearn import metrics


print(metrics.mean_absolute_error(y_test,predictions))
print(metrics.mean_squared_error(y_test,predictions))
print(np.sqrt(metrics.mean_squared_error(y_test,predictions)))






