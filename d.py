import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}

df = pd.DataFrame(data)

# Calculate the sum of all values except the first column
total_sum_except_first_column = df.iloc[:, 1:].sum().sum()

print("Sum of all values except the first column:", total_sum_except_first_column)