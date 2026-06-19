from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load dataset and split it
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

# Train KNN model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Get predictions
y_pred = knn.predict(X_test)

# Check if y_test and y_pred have the same length
print(f"Length of y_test: {len(y_test)}")
print(f"Length of y_pred: {len(y_pred)}")  # Ensure both lengths are the same

# Get the classification report
report = classification_report(y_test, y_pred, output_dict=True)

# Convert to DataFrame for easy plotting
df_report = pd.DataFrame(report).transpose()

# Check if 'accuracy' is in the DataFrame before dropping
if 'accuracy' in df_report.index:
    df_report = df_report.drop('accuracy')

# Remove 'support' column (optional)
df_report = df_report.drop(columns=['support'])

# Plot Precision, Recall, F1-Score per class
df_report.plot(kind='bar', figsize=(8, 5))
plt.title("Precision, Recall, F1-Score per Class")
plt.ylabel("Score")
plt.ylim(0, 1.1)  # Set y-axis range to [0, 1]
plt.xticks(rotation=0)  # Rotate x-axis labels for better readability
plt.grid(axis='y')  # Add grid lines along the y-axis
plt.tight_layout()  # Adjust layout to prevent label cutoff
plt.show()
