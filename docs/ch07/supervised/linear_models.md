# Linear Models
Linear regression, logistic regression, Ridge, Lasso with L1/L2 regularization for classification and regression.

## Linear Regression
```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

## Logistic Regression
```python
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(C=1.0, penalty='l2')
model.fit(X_train, y_train)
```

## Regularization
**Ridge (L2):** Shrinks coefficients  
**Lasso (L1):** Feature selection (sparsity)  
**ElasticNet:** Combines L1 and L2