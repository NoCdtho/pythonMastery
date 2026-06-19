import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import pandas as pd
import numpy as np

# Dummy example values — replace these with your actual y_test and y_pred
y_test = [0, 1, 0, 1, 0, 1, 1, 0]      # True labels
y_pred = [0, 1, 0, 0, 0, 1, 1, 1]      # Predicted labels

# Automatically detect unique class labels
labels = np.unique(np.concatenate((y_test, y_pred)))
class_names = [f'Class {label}' for label in labels]

# Compute confusion matrix
cm = confusion_matrix(y_test, y_pred, labels=labels)

# Create a DataFrame for the heatmap
cm_df = pd.DataFrame(cm, index=class_names, columns=class_names)

# Plot the heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(cm_df, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Naive Bayes - Confusion Matrix')
plt.tight_layout()
plt.show()
