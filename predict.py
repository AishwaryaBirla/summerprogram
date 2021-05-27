import joblib
model=joblib.load('salary.pk1')
print(model.predict([[10]])) #give the values to test here in 2D array
