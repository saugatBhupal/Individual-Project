import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# Estimated confusion matrix
labels = ['ball', 'goalkeeper', 'player', 'referee']

# Rows = actual classes, Columns = predicted
cm = [
    [0, 10, 20, 5],         # ball
    [2, 15, 7, 3],          # goalkeeper
    [5, 30, 606, 113],      # player
    [1, 6, 5, 49],          # referee
]

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='YlGnBu', xticklabels=labels, yticklabels=labels)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Estimated Confusion Matrix (YOLOv5s)")
plt.show()
