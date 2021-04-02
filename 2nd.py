from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import seaborn as sns
#Train_Data and Test_Data
Train_Data = pd.read_csv('CrashTest_TrainData.csv')
Test_Data = pd.read_csv('CrashTest_TestData.csv')
train_copy = Train_Data.copy()
test_copy = Test_Data.copy()
train_copy.info()
train_copy.describe()
test_copy.describe()
train_copy.isnull().sum()
test_copy.isnull().sum()
train_copy[train_copy==np.inf]=np.nan
test_copy.fillna(test_copy.mean(), inplace=True)
test_copy[test_copy==np.inf]=np.nan
train_copy.fillna(train_copy.mean(), inplace=True)
X = train_copy.drop(columns=['CarType'])
X.head()
y = train_copy['CarType'].values
y[0:5]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1, stratify=y)
#knn = KNeighborsClassifier(n_neighbors = 3)
#knn.fit(X_train,y_train)
##knn.predict(test_copy)[0:80]
#knn.score(X_test, y_test)
#y_test = np.asarray(y_test)
#misclassified = np.where(y_test != clf.predict(X_test))
knn = KNeighborsClassifier(n_neighbors = 2)
knn.fit(X_train,y_train)
knn.predict(test_copy)[0:80]
knn.score(X_test, y_test)
