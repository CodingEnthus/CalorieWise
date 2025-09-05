# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import csv
# import os

# app = Flask(__name__)
# CORS(app)

# # Dictionary to store food name -> calories per gram
# FOOD_DATA = {}

# def load_all_food_data():
#     """
#     Load all CSV files inside final_food_dataset/ whose name starts with FOOD-DATA-GROUP
#     and populate FOOD_DATA dictionary with:
#     key = food name (lowercase)
#     value = kcal per gram
#     """
# folder_path = os.path.join(os.path.dirname(__file__), 'final_food_dataset')
# for filename in os.listdir(folder_path):
#         if filename.startswith('FOOD-DATA-GROUP') and filename.endswith('.csv'):
#             file_path = os.path.join(folder_path, filename)

#             # ✅ Keep reading inside the 'with' block
#             with open(file_path, newline='', encoding='utf-8') as csvfile:
#                 reader = csv.DictReader(csvfile)
#                 for row in reader:
#                     try:
#                         # Extract food name and calorie data
# <<<<<<< HEAD
#                         food_name = row['Food Name'].strip().lower()

#                         # Handle multiple possible calorie column names
#                         if 'Energy (kcal) / 100 g' in row:
#                             kcal_per_100g = float(row['Energy (kcal) / 100 g'])
#                         elif 'Caloric Value' in row:
#                             kcal_per_100g = float(row['Caloric Value'])
#                         else:
#                             continue  # skip if no matching column
# =======
#                         food_name = row['food'].strip().lower()
#                         kcal_per_100g = float(row['Caloric Value'])
# >>>>>>> e590d13 (Add .gitignore and remove node_modules from tracking)

#                         # Convert to per gram
#                         kcal_per_gram = kcal_per_100g / 100
#                         FOOD_DATA[food_name] = kcal_per_gram

#                     except (ValueError, KeyError):
#                         continue  # Skip rows with missing or invalid data
#                     print(f"\n✅ Loaded {len(FOOD_DATA)} foods into memory.")

# # Function to calculate total calories for a food item
# def get_calories(food, amount):
#     food = food.lower()
#     if food in FOOD_DATA:
#         return round(FOOD_DATA[food] * amount, 2)  # total kcal = per gram * amount
#     return None

# # API Endpoint
# @app.route('/calories', methods=['POST'])
# def calories():
#     data = request.get_json()
#     food = data.get('food')
#     amount = data.get('amount') or data.get('quantity')  # accept both

#     if not food or not amount:
#         return jsonify({'error': 'Please provide food and amount'}), 400

#     try:
#         calories = get_calories(food, float(amount))
#     except ValueError:
#         return jsonify({'error': 'Amount must be a number'}), 400

#     if calories is None:
#         return jsonify({'error': f'Food "{food}" not found in database'}), 404

#     return jsonify({'food': food, 'amount': amount, 'calories': calories})

# # Home route - browser friendly
# @app.route("/", methods=["GET"])
# def home():
#     return jsonify({"message": "Welcome to CalorieWise API! Use POST /calories with food + amount."})

# # Test route - quick check
# @app.route("/test", methods=["GET"])
# def test():
#     return jsonify({"status": "API is working ✅"})

# # Load data once when app starts
# load_all_food_data()

# if __name__ == '__main__':
#     app.run(debug=True)

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
    folder_path = os.path.join(os.path.dirname(__file__), 'final_food_dataset')
    for filename in os.listdir(folder_path):
        if filename.startswith('FOOD-DATA-GROUP') and filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
                        # Get food name from possible columns
                        food_name = row.get('Food Name') or row.get('food')
                        if not food_name:
                            continue
                        food_name = food_name.strip().lower()

                        # Handle multiple possible calorie column names
                        if 'Energy (kcal) / 100 g' in row:
                            kcal_per_100g = float(row['Energy (kcal) / 100 g'])
                        elif 'Caloric Value' in row:
                            kcal_per_100g = float(row['Caloric Value'])
                        else:
                            continue  # skip if no matching column

                        # Convert to per gram
                        kcal_per_gram = kcal_per_100g / 100
                        FOOD_DATA[food_name] = kcal_per_gram

                    except (ValueError, KeyError):
                        continue  # Skip rows with missing or invalid data

    print(f"\n✅ Loaded {len(FOOD_DATA)} foods into memory.")

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
    amount = data.get('amount') or data.get('quantity')  # accept both

    if not food or not amount:
        return jsonify({'error': 'Please provide food and amount'}), 400

    try:
        calories = get_calories(food, float(amount))
    except ValueError:
        return jsonify({'error': 'Amount must be a number'}), 400

    if calories is None:
        return jsonify({'error': f'Food "{food}" not found in database'}), 404

    return jsonify({'food': food, 'amount': amount, 'calories': calories})

# Home route - browser friendly
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to CalorieWise API! Use POST /calories with food + amount."})

# Test route - quick check
@app.route("/test", methods=["GET"])
def test():
    return jsonify({"status": "API is working ✅"})

# Load data once when app starts
load_all_food_data()

if __name__ == '__main__':
    app.run(debug=True)
