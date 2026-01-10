# Tree-Based Models
Decision trees, pruning, feature importance, handling non-linear relationships and categorical features.

## Decision Tree
```python
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(max_depth=5, min_samples_split=10)
model.fit(X_train, y_train)
```

## Feature Importance
```python
importances = model.feature_importances_
```

## Overfitting Prevention
**max_depth:** Limit tree depth  
**min_samples_split:** Minimum samples to split  
**min_samples_leaf:** Minimum samples in leaf