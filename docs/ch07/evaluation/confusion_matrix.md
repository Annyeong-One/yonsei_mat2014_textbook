# Confusion Matrix
Visualize classification performance with true/false positives/negatives matrix.

## Basic Matrix
```python
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_true, y_pred)
print(cm)
# [[TN, FP],
#  [FN, TP]]
```

## Visualization
```python
from sklearn.metrics import ConfusionMatrixDisplay
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
```

## Classification Report
```python
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred))
# Shows precision, recall, F1 per class
```