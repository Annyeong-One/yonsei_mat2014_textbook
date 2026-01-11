# Ensemble Methods
Random forests, gradient boosting, bagging and boosting for improved predictive performance.

## Random Forest
```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, max_depth=10)
model.fit(X_train, y_train)
```

## Gradient Boosting
```python
from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1)
```

## XGBoost
```python
import xgboost as xgb
model = xgb.XGBClassifier(n_estimators=100, max_depth=6)
```