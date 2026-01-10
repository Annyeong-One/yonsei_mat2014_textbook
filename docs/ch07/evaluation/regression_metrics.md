# Regression Metrics
MSE, RMSE, MAE, R² for evaluating regression model performance.

## MSE/RMSE
```python
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_true, y_pred)
rmse = np.sqrt(mse)
```

## MAE
```python
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_true, y_pred)
```

## R² Score
```python
from sklearn.metrics import r2_score
r2 = r2_score(y_true, y_pred)
# 1.0 = perfect, 0.0 = baseline, <0 = worse than mean
```