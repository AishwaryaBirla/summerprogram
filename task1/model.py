import pandas
import numpy
import joblib
data = pandas.read_csv('salarayData.csv')
x=data['YearsExperience'].values.reshape(30,1)#we need to reshape as fit function takes 2D array as input.
#to convert it from pandas datatype of ndarray to numpy use .values
y=data['Salary']
from sklearn.linear_model import LinearRegression
mind= LinearRegression()
mind.fit(x,y)
joblib.dump(mind,'salary.pk1')
