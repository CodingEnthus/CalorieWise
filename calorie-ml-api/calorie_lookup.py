import pandas as pd
import os

# Correct folder name (after rename)
data_folder = 'final_food_dataset'

# Read all CSVs from the folder
csv_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]
if not csv_files:
    raise FileNotFoundError("No CSV files found in final_food_dataset folder.")

df_list = [pd.read_csv(os.path.join(data_folder, file)) for file in csv_files]
df = pd.concat(df_list, ignore_index=True)

# Clean up column names
df.columns = df.columns.str.strip()

# Use correct column name — let’s inspect one file for now
# print(df.columns)  # Uncomment this if you want to debug

def get_calories(food, amount):
    try:
        food_row = df[df['Food'].str.lower() == food.lower()]
        if food_row.empty:
            return None
        calories = food_row.iloc[0]['Calories (kcal)']  # Change if needed
        return (calories * amount) / 100
    except Exception as e:
        print(f"Error: {e}")
        return None
