import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample data (X, Y) for regression
data_lr = pd.DataFrame({
    "X": [5, 12, 18, 23, 45, 50],
    "Y": [7, 15, 20, 25, 48, 52]
})

# Splitting the data into input and output
X_lr = data_lr[["X"]]  # Features must be in 2D
y_lr = data_lr["Y"]    # Target

# Fitting the regression model
reg_model = LinearRegression()
reg_model.fit(X_lr, y_lr)

# Predicting values
y_pred_lr = reg_model.predict(X_lr)

# Plotting the regression line
plt.figure(figsize=(6, 4))
sns.scatterplot(x="X", y="Y", data=data_lr, color='blue', label='Data Points')
plt.plot(data_lr["X"], y_pred_lr, color='red', label='Regression Line')
plt.title("Linear Regression Fit")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.tight_layout()
plt.show()
