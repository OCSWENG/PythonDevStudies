
import pandas as pd
import numpy as mp
import matplotlib.pyplot as plt
import seaborn as sns



# Get DATA

customers = pd.read_csv('Ecommerce Customers')

print(customers.head())

print(customers.describe())

print(customers.info())

# explore data study


sns.joinplot(data=customers,x='Time on Website', y='Yearly Amount Spent')

plt.show()

sns.joinplot(data=customers,x='Time on App', y='Yearly Amount Spent')

plt.show()


sns.joinplot(x='Time on App', y='Length of Membership', kind='hex', data=customers)

plt.show()


sns.pairplot(customers)

plt.show()
# highest correlation a line is Length of Membership to Yearly amount spent

sns.lmplot(x='Length of Membership', y='Yearly Amount Spent', data=customers)

plt.show()

# Train data
print(customers.columns)
# all the numerical columns
X =customers[ ['Avg. Session Length','Time on App','Time on Website', 'Length of Membership']]

y = customers['Yearly Amount Spent']


from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=101)

 from sklearn.linear_model import LinearRegression
    
lm = LinearRegression()

lm.fit(X_train, y_train)

print(lm.coef_)

predictions = lm.predict(X_test)

plt.scatter(y_test, predictions)
plt.xlabel('Y test aka True values')
plt.ylabel('Predicted values')

# evaluate the model
from sklearn import metrics


print("MAE = ",metrics.mean_absolute_error(y_test,predictions)) 

print("MSE = ",metrics.mean_squared_error(y_test,predictions)) 

print("RMSE = ",np.sqrt(metrics.mean_squared_error(y_test,predictions)))


# variance score

print(metrics.explained_variance_score(y_test, predictions))

# Residuals

sns.distplot((y_test-predictions), bins=75)

# mobile or website or length of membership

cdf = pd.DataFrame (lm.coef_, X.columns, columns['Coeff'])

# Coeff is like a weight 1:26 , 1:38, 1:0.19, 1:61.28

# Website is deficient or App is more effective





