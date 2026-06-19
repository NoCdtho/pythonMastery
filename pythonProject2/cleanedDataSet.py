import pandas as pd
import numpy as np

data = np.load("X_train.npy")
data2 = np.load("y_train.npy")

df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)

df.to_excel('output_file1.xlsx', index=False)
df2.to_excel('output_file2.xlsx', index=False)