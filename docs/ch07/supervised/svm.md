# Support Vector Machines
SVM finds optimal hyperplane with maximum margin for classification and regression.

## SVC
```python
from sklearn.svm import SVC
model = SVC(C=1.0, kernel='rbf', gamma='scale')
model.fit(X_train, y_train)
```

## Kernels
**linear:** Linear decision boundary  
**rbf:** Radial basis function (non-linear)  
**poly:** Polynomial features

## Key Parameters
**C:** Regularization (smaller = more regularization)  
**gamma:** Kernel coefficient