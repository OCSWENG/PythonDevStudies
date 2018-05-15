
# logistic regression curve is a sigmod better for categorical 
#   1/(1+e^-z)
# looks like a digital signal
# 0 >= x <= 0.5 is a 0

# linear : y = b0 + b2X

# Logistic z = linear

# confusion matrix : truth table TP, TN, FP, FN
# TP : predicted and tested are positive
# FP : predicted yes but tested false ( type 1 error)
# FN type 2 error
# accurate ( tp + tn)/total
# misclassification rate  (fp + fn)/total

# kaggle.com data science for datasets


import pandas as pd
import numpy as np
import matpolilotlib.pyplot as plt
import seaborn as sns


titanicTrain = pd.read_csv('titanic_train.csv')

# Explore Data

print(titanicTrain.columns)

# numerics
columns = ['passengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch','Fare']

# use heatmap to find missing data

sns.heatmap(titanicTrain.isnull(), yticklabels=False, cbar=False, cmap='viridis')


sns.countplot(x='Survived', hue='Sex', data=titanicTrain)

sns.countplot(x='Survived', hue='Pclass', data=titanicTrain)

sns.distplot(titanicTrain['Age'].dropna(), kde=False, bins=50)
titanicTrain['Age'].plot.hist(bins=50)

# child or spouse
sns.countplot(x='SibSp', data=titanicTrain)

sns.distplot(x='Fare', data=titanicTrain, bins=50)

import cufflinks as cf
cf.go_offline()

titanicTrain['Fare'].iplot(kind='hist', bins=50)

# Clean Data

sns.boxplot(x='Pclass',y='Age',data=train,palette='winter')

# take the average age of each passenger classmethod

def fillInAge (cols):
    Age = cols[0]
    PClass = cols[1]
    
    if pd.isnull(Age):
        if PClass ==1: # 1st class`
            return 37
        elif PClass ==2: # 2nd class
            return 29
        else: # 3rd class
            return 24
    else:
        return Age

    
# now use the function in the apply call

titanicTrain['Age'] = titanicTrain[['Age', 'Pclass']].apply(fillInAge, axis=1)

# too much missing data in the cabin column possibly Pclass could reveal which level, first class tends to be top and 3rd class bottom like airplanes

titanicTrain.drop('Cabin',axis=1,inplace=True)

titanicTrain.dropna(inplace=True)

# turn Sex and Embarked into numerical values

sex = pd.get_dummies(titanicTrain['Sex'],drop_first=True)
embark = pd.get_dummies(titanicTrain['Embarked'],drop_first=True)


titanicTrain.drop(['Sex','Embarked','Name','Ticket'],axis=1,inplace=True)

titanicTrain = pd.concat([titanicTrain,sex,embark],axis=1)


# Build a Logistic Regression Model

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X = titanicTrain.drop('Survived',axis=1)
y = titanicTrain['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)

logRegMod = LogisticRegression()
logRegMod.fit(X_train,y_train)

predictions = logRegMod.predict(X_test)


# Evaluation

from sklearn.metrics import classification_report
from sklearn.metrics import confustion_matrix

print(classification_report(y_test,predictions))

print(confusion_matrix(y_test,predictions))





