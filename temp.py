import pandas as pd #to work with dataframes
import numpy as np #to perform mathematical operations
import seaborn as sns #to visualize data
from sklearn.model_selection import train_test_split #to partition data
from sklearn.linear_model import LogisticRegression #to perform Logistic Regression
from sklearn.metrics import accuracy_score,confusion_matrix
#data_income = pd.read_csv('income(1).csv')
data = pd.read_csv('income(1).csv')

