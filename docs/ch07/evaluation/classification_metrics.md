# Classification Metrics
Accuracy, precision, recall, F1-score, ROC-AUC for evaluating classification models.

## Accuracy
```python
from sklearn.metrics import accuracy_score
acc = accuracy_score(y_true, y_pred)
```

## Precision/Recall/F1
```python
from sklearn.metrics import precision_score, recall_score, f1_score
prec = precision_score(y_true, y_pred)
rec = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
```

## ROC-AUC
```python
from sklearn.metrics import roc_auc_score, roc_curve
auc = roc_auc_score(y_true, y_pred_proba)
fpr, tpr, thresholds = roc_curve(y_true, y_pred_proba)
```