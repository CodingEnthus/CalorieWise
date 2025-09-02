import kagglehub
import pandas as pd

# Download the dataset
path = kagglehub.dataset_download("utsavdey1410/food-nutrition-dataset")

# Print to verify where it downloaded
print("Downloaded dataset files to:", path)

# Example: Load the dataset
# You may need to update this filename based on what’s inside the zip
csv_file = path + "/nutrition_data.csv"  # or whatever the real CSV file is
df = pd.read_csv(csv_file)

print("Loaded dataset successfully!")
print(df.head())  # Show first 5 rows
