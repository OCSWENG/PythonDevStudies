

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix


df = pd.read_csv('Classified Data', index_col=0)

print(df.head())

scale = StandardScaler()

scale.fit(df.drop('TARGET CLASS', axis=1))

# standized by centering and scaling
scaled_features = scale.transform(df.drop('TARGET CLASS', axis=1))
print(scaled_features)


df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])
print(df_feat)


X = scaled_features
# X = df_feat

y = df['TARGET CLASS']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=101)

knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train, y_train)

pred = knn.predict(X_test)


print(confusion_matrix(y_test,pred))

print(classification_report(y_test,pred))


# --- ELBOW method ---


def findMinErrorRate (error_rate):
    smallest = None
    idx = None
    count = 0
    for item in error_rate:
        if (min == None or item < smallest):
            smallest = item
            idx = count
        count += 1
    return (smallest, idx)

def findMinErrorRate2 (error_rate):        
    minVal,idx = min( (error_rate[i],i) for i in range(len(error_rate)) )
    return (minVal,idx)

error_rate=[]

def printErrorRate ():
    plt.figure(figgsize=10,6)
    plt.plot(range(1,40),error_rate, color='v', linestyle='*', marker='#', markerfacecolor='black', markersize=10)
    plt.title ('Error rate vs K value')
    plt.xlabel('K')
    plt.ylabel('Error Rate')
    plt.show()

for i in range(1,40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))


minVal,idx = findMinErrorRate2(error_rate)   
print("K # : ErrorRate is %d : %d".format(idx,minVal))


knn = KNeighborsClassifier(n_neighbors=idx)
knn.fit(X_train, y_train)
pred_i = knn.predict(X_test)

print(confusion_matrix(y_test,pred))
print(classification_report(y_test,pred))

# look at precision 0.98 == 98% accurate!
