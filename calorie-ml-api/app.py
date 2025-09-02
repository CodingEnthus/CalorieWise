from flask import Flask, request, jsonify
from flask_cors import CORS
import csv
import os

app = Flask(__name__)
CORS(app)

# Dictionary to store food name -> calories per gram
FOOD_DATA = {}

def load_all_food_data():
    """
    Load all CSV files inside final_food_dataset/ whose name starts with FOOD-DATA-GROUP
    and populate FOOD_DATA dictionary with:
    key = food name (lowercase)
    value = kcal per gram
    """

    # ✅ Path to the folder where all your CSVs are stored (inside your project)
    folder_path = os.path.join(os.path.dirname(__file__), 'final_food_dataset')

    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.startswith('FOOD-DATA-GROUP') and filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            
            # Open and read the CSV file
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
                        # Extract food name and calorie data
                        food_name = row['Food Name'].strip().lower()
                        kcal_per_100g = float(row['Energy (kcal) / 100 g'])

                        # Convert to per gram
                        kcal_per_gram = kcal_per_100g / 100
                        FOOD_DATA[food_name] = kcal_per_gram
                    except (ValueError, KeyError):
                        continue  # Skip rows with missing or invalid data

# Function to calculate total calories for a food item
def get_calories(food, amount):
    food = food.lower()
    if food in FOOD_DATA:
        return round(FOOD_DATA[food] * amount, 2)  # total kcal = per gram * amount
    return None

# API Endpoint
@app.route('/calories', methods=['POST'])
def calories():
    data = request.get_json()
    food = data.get('food')
    amount = data.get('amount')  # in grams

    if not food or not amount:
        return jsonify({'error': 'Please provide food and amount'}), 400

    calories = get_calories(food, float(amount))
    if calories is None:
        return jsonify({'error': 'Food not found'}), 404

    return jsonify({'calories': calories})

# Load data once when app starts
load_all_food_data()

if __name__ == '__main__':
    app.run(debug=True)
