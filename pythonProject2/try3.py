import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Example Cricketer Data
cricketers_df = pd.DataFrame({
    "Wicket": [56, 12, 34, 23, 7, 18, 29, 38],
    "Run": [120, 1132, 450, 670, 980, 540, 310, 200]
})

# Scatter plot
plt.figure(figsize=(6, 4))
sns.scatterplot(x="Wicket", y="Run", data=cricketers_df, s=100, color='green')
plt.title("Cricketer Stats - Scatter Plot")
plt.xlabel("Wickets")
plt.ylabel("Runs")
plt.show()