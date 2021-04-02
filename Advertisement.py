#import important libraries
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import skew
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use("ggplot")
plt.rcParams['figure.figsize'] = (12,8)
#Load the daatset
advert = pd.read_csv('Advertising.csv')
#advert: dataframe
#to look at the 1st 5 values:
print(advert.head())
#to look at some other info about the same dataset:
print(advert.info())
#in the result: there are 200 rows and 4 columns
#our goal is to maximize the accuracy of prediction using any of the 3 predictors

#let's identify the relationship between features and Response
#this can be done using seaborn library
sns.pairplot(advert, x_vars=['TV','radio','newspaper'], y_vars='sales',height=7, aspect=0.7)
#Apply some model
from sklearn.linear_model import LinearRegression
x = advert[['TV', 'radio', 'newspaper' ]]
y= advert.sales
lm1 = LinearRegression()
lm1.fit(x,y)
#this returns the parameters
print(lm1.intercept_)
print(lm1.coef_)
list(zip(['TV','radio', 'newspaper'],lm1.coef_))
sns.heatmap(advert.corr(), annot= True)
#Feature selection
from sklearn.metrics import r2_score
lm2 = LinearRegression().fit(x[['TV', 'radio']],y)
lm2_pred = lm2.predict(x[['TV', 'radio']])
print("R^2: ", r2_score(y,lm2_pred))
#let's create 3rd linear model
lm3 = LinearRegression().fit(x[['TV','radio', 'newspaper']],y)
lm3_pred = lm3.predict(x[['TV','radio','newspaper']])
print("R^2: ", r2_score(y, lm3_pred))
