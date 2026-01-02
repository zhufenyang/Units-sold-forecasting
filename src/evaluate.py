from sklearn.metrics import mean_absolute_error, mean_squared_error
from math import sqrt

def evaluate(model, X_test, y_test):
    mae = mean_absolute_error(y_test, model.predict(X_test))
    rmse = sqrt(mean_squared_error(y_test, model.predict(X_test)))
    return mae, rmse
