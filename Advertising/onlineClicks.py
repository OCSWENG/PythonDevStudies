# Attempt to predict whether a advertisement will be clicked based off what they gave a features


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


ad_data = pd.read_csv('advertising.csv')

'''
# Exlpore the data
print(ad_data.head())
print(ad_data.info())
print(ad.data.columns)
print(ad_data.describe())

sns.set_style('whitegrid')

# Who are the users

ad_data['Age'].hist(bins=30)

plt.xlabel('Age')

plt.show()


# what are their income

sns.jointplot(x='Age',y='Area Income',data=ad_data)
plt.show()


# hot spot of age : usage 

sns.jointplot(x='Age',y='Daily Time Spent on Site',data=ad_data,color='red',kind='kde');
plt.show()

# platform usage 

sns.jointplot(x='Daily Time Spent on Site',y='Daily Internet Usage',data=ad_data,color='green')
plt.show()


# Who clicks on Ads
sns.pairplot(ad_data,hue='Clicked on Ad')
plt.show()

'''

# divide the data into training and testing 

X = ad_data[['Daily Time Spent on Site', 'Age', 'Area Income','Daily Internet Usage', 'Male']]

test_pct = [0.10,0.25,0.33,0.50,0.75]
randState = [0,25,50,100,125,150,175,200]

for pct in test_pct:
    for seed in randState:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_pct,random_state=seed) 

        y = ad_data['Clicked on Ad']

        # train and fit the logistic regression model
        logmodel = LogisticRegression()
        logmodel.fit(X_train,y_train)

        # predict and evauluate
        predictions = logmodel.predict(X_test)
        print("Test Percent : ",test_pct )
        print("Random State : ", seed)
        print(classification_report(y_test,predictions))
