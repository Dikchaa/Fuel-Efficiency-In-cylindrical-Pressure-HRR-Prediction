# -*- coding: utf-8 -*-
"""Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZgS0to5mNlCB6YTEydySy3gCF09FEpWH
"""

# Supress Warnings

import warnings
warnings.filterwarnings('ignore')

# Import the numpy and pandas package

import numpy as np
import pandas as pd

# Data Visualisation
import matplotlib.pyplot as plt
import seaborn as sns

d = pd.DataFrame(pd.read_csv("pro1.csv"))
d.head(15)

d.info()

d.shape

list(d.columns)

d.describe()

# Checking Null values
d.isnull().sum()

#d=d.drop(columns='FUEL')

d.isnull().sum()

# Outlier Analysis

sns.boxplot(d['BTE'])
plt.show()

np.mean(d['BTE']),np.std(d['BTE'])
#max 34 & min 7

np.mean(d['Fuel1']),np.std(d['Fuel1'])
#max=25 and min=11

np.mean(d['Fuel2']),np.std(d['Fuel2'])
#max=9 and min=1

np.mean(d['BP']),np.std(d['BP'])
#max=4 and min=1

# Outlier Analysis
fig, axs = plt.subplots(3, figsize = (5,5))
plt1 = sns.boxplot(d['Fuel1'], ax = axs[0])
plt2 = sns.boxplot(d['Fuel2'], ax = axs[1])
plt3 = sns.boxplot(d['BP'], ax = axs[2])
plt.tight_layout()



# Let's see how Sales are related with other variables using scatter plot.

sns.pairplot(d, x_vars=['Fuel1'], y_vars='BTE', height=4, aspect=1, kind='scatter')
plt.show()

sns.pairplot(d, x_vars=['BP'], y_vars='BTE', height=4, aspect=1, kind='scatter')
plt.show()

sns.pairplot(d, x_vars=['Load'], y_vars='BTE', height=4, aspect=1, kind='scatter')
plt.show()

sns.pairplot(d, x_vars=['Fuel1'], y_vars='BTE', height=4, aspect=1, kind='scatter')
plt.show()

sns.pairplot(d, x_vars=['Fuel2'], y_vars='BTE', height=4, aspect=1, kind='scatter')
plt.show()

sns.pairplot(d, x_vars=['cf'], y_vars='BTE', height=4, aspect=1, kind='scatter')
plt.show()

new_df = d[(d['Fuel1'] >= 11) & (d['Fuel1'] <= 25)]
new_df

new_df = new_df[(new_df['Fuel2'] >= 1) & (new_df['Fuel2'] <= 9)]
new_df

new_df = new_df[(new_df['BP'] >= 1) & (new_df['BP'] <= 4)]
new_df

new_df.info()

c=['FID','cf',
 'Load',
 'Fuel1',
 'Fuel2',
 'Total_Vol',
 'Mass_Fuel',
 'Heat_Input',
 'BP','BTE']
dfa=new_df[c]
dfa

dfa.to_csv('pro1.csv')

from sklearn.preprocessing import StandardScaler
import numpy as np
object = StandardScaler()
object.fit_transform(dfa)

# Let's see the correlation between different variables.
sns.heatmap(d.corr(), cmap="YlGnBu", annot = True)
plt.show()

X = d[['Fuel1','Fuel2','cf','BP','FID','Heat_Input']]
y = d['BTE']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, test_size = 0.3, random_state = 100)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

# Assuming you have defined X_train, X_test, y_train, y_test before
# X_train and X_test are the feature matrices, y_train, and y_test are the target arrays

# Create a Ridge regression object with a specific alpha value
alpha = 1.0  # You can experiment with different alpha values
ridge_model = Ridge(alpha=alpha)

ridge_model.fit(X_train, y_train)

# Make predictions on the test set
predict = ridge_model.predict([[22.4,5.6,34200,3.16,5,14.96709]])
print(predict)

# Assuming you have already trained and evaluated your ridge_model as shown in your previous code.

# Define a function to calculate accuracy within a threshold
def accuracy_within_threshold(y_true, y_pred, threshold_percentage=5):
    # Calculate the absolute percentage error between true and predicted values
    absolute_percentage_error = abs((y_true - y_pred) / y_true) * 100

    # Calculate the percentage of predictions within the specified threshold
    accuracy = (absolute_percentage_error <= threshold_percentage).mean() * 100

    return accuracy

# Make predictions on the test set
y_pred = ridge_model.predict(X_test)

# Calculate and print the accuracy within a threshold of ±5%
accuracy = accuracy_within_threshold(y_test, y_pred, threshold_percentage=5)
print("Accuracy within ±5%:", accuracy, "%")

#Printing the model coefficients
print(ridge_model.intercept_)
# pair the feature names with the coefficients
list(zip(X, ridge_model.coef_))

#Predicting the Test and Train set result
y_pred_mlr= ridge_model.predict(X_test)
x_pred_mlr= ridge_model.predict(X_train)

print("Prediction for test set: {}".format(y_pred_mlr))

# 0 means the model is perfect. Therefore the value should be as close to 0 as possible
from sklearn import metrics
meanAbErr = metrics.mean_absolute_error(y_test, y_pred_mlr)
meanSqErr = metrics.mean_squared_error(y_test, y_pred_mlr)
rootMeanSqErr = np.sqrt(metrics.mean_squared_error(y_test, y_pred_mlr))

print('Mean Absolute Error:', meanAbErr)
print('Mean Square Error:', meanSqErr)
print('Root Mean Square Error:', rootMeanSqErr)

"""# New Section"""

d.drop(columns=["Unnamed: 0"],inplace=True)

#Import library
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_X = sc_X.fit_transform(d)
#Convert to table format - StandardScaler
sc_X = pd.DataFrame(data=sc_X, columns=['FID','cf',
 'Load',
 'Fuel1',
 'Fuel2',
 'Total_Vol',
 'Mass_Fuel',
 'Heat_Input',
 'BP','BTE'])
sc_X

import seaborn as sns
import matplotlib.pyplot as plt

# Create some example data
data = [1.2, 2.5, 2.7, 3.2, 3.5, 3.8, 4.1, 4.2, 4.5, 4.7, 5.1, 5.3]

# Create a distribution plot using histplot and kdeplot
sns.histplot(sc_X['BTE'], kde=True)  # Set kde=True for the kernel density estimate
plt.xlabel('Values')
plt.ylabel('Density')
plt.title('Distribution Plot')
plt.show()