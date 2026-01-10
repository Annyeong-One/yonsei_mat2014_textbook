# Pipeline Construction
Chain preprocessing and modeling steps to prevent data leakage and simplify workflow.

## Basic Pipeline
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
```

## Benefits
**No leakage:** Scaler fit only on training data  
**Cleaner code:** Single fit/predict interface  
**Grid search:** Tune entire pipeline

## Access Steps
```python
scaler = pipeline.named_steps['scaler']
model = pipeline.named_steps['classifier']
```