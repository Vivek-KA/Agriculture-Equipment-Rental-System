import joblib
import numpy as np;
import pandas as pd;
import pymysql
pymysql.install_as_MySQLdb()
import pymysql as MySQLdb
import matplotlib.pyplot  as plt;
from sklearn.model_selection  import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle
gmail_list=[]
password_list=[]
gmail_list1=[]
password_list1=[]
import numpy as np;
import pandas as pd;
import matplotlib.pyplot  as plt;
from sklearn.model_selection  import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle
import random

import random

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np;
import pandas as pd;
import matplotlib.pyplot  as plt;
from sklearn.model_selection  import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle





import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


from flask import Flask, request, render_template, redirect, url_for
import csv
from datetime import datetime
from PIL import Image
import numpy as np
import io
import base64

from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

#app = Flask(__name__)

# Load the CSV data

# Load the saved ML model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "xgb_model.pkl")

with open(MODEL_PATH, "rb") as file:
    loaded_model = pickle.load(file)






app = Flask(__name__) 


@app.route('/')
def home():
    return render_template('index44.html') 



@app.route('/seller')
def seller():
    return render_template('login44.html') 
@app.route('/buyer')
def buyer():
    return render_template('login45.html') 


@app.route('/logedinb',methods=['POST'])
def logedinb():
    
    int_features3 = [str(x) for x in request.form.values()]
    print(int_features3)
    logu=int_features3[0]

    passw=int_features3[1]
   # if int_features2[0]==12345 and int_features2[1]==12345:




    import MySQLdb


# Open database connection
    db = MySQLdb.connect(
    host=os.environ.get("DB_HOST"),
    user=os.environ.get("DB_USER"),
    passwd=os.environ.get("DB_PASSWORD"),
    db=os.environ.get("DB_NAME")
)


# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1=cursor.fetchall()
              #print(result1)
              #print(gmail1)
    for row1 in result1:
                      print(row1)
                      print(row1[0])
                      gmail_list.append(str(row1[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    print(gmail_list)
    

    cursor1= db.cursor()
    cursor1.execute("SELECT password FROM user_register")
    result2=cursor1.fetchall()
              #print(result1)
              #print(gmail1)
    for row2 in result2:
                      print(row2)
                      print(row2[0])
                      password_list.append(str(row2[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    print(password_list)
    print(gmail_list.index(logu))
    print(password_list.index(passw))
    
    if gmail_list.index(logu)==password_list.index(passw):
        return render_template('index45.html')
    else:
        return jsonify({'result':'use proper  gmail and password'})


@app.route('/logedin',methods=['POST'])
def logedin():
    
    int_features3 = [str(x) for x in request.form.values()]
    print(int_features3)
    logu=int_features3[0]
    # Save the text to a pickle file
    text = str(int_features3[0])
    with open('smartai_text.pkl', 'wb') as file:
        pickle.dump(text, file)


    passw=int_features3[1]
   # if int_features2[0]==12345 and int_features2[1]==12345:

    import MySQLdb


# Open database connection
    db = MySQLdb.connect(
    host=os.environ.get("DB_HOST", "localhost"),
    user=os.environ.get("DB_USER", "root"),
    passwd=os.environ.get("DB_PASSWORD", ""),
    db=os.environ.get("DB_NAME", "ddbb")
)


# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1=cursor.fetchall()
              #print(result1)
              #print(gmail1)
    for row1 in result1:
                      print(row1)
                      print(row1[0])
                      gmail_list.append(str(row1[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
  #  print(gmail_list)
    

    cursor1= db.cursor()
    cursor1.execute("SELECT password FROM user_register")
    result2=cursor1.fetchall()
              #print(result1)
              #print(gmail1)
    for row2 in result2:
                      print(row2)
                      print(row2[0])
                      password_list.append(str(row2[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    #print(password_list)
    #print(gmail_list.index(logu))
    #print(password_list.index(passw))
    
    if gmail_list.index(logu)==password_list.index(passw):
        return render_template('yield.html')
    else:
        return jsonify({'result':'use proper  gmail and password'})
                  
                                               
import os
import uuid
from PIL import Image
from flask import request, render_template
from datetime import datetime
import csv

@app.route('/add_equipment', methods=['POST'])
def add_equipment():
    # Define mappings for dropdowns
    equipment_type_map = {
        "Combine Harvester": 0, "Cultivator": 1, "Harrow": 2,
        "Manure Spreader": 3, "Mower": 4, "Plough": 5,
        "Seed Drill": 6, "Sprayer": 7, "Tractor": 8
    }
    brand_map = {
        "John Deere": 0, "CNH Industrial": 1, "AGCO Corporation": 2,
        "FMWORLD Agricultural Machinery": 3, "Kubota": 4, "Claas": 5,
        "SDF": 6, "Mahindra & Mahindra": 7, "JCB": 8, "Caterpillar": 9
    }
    condition_map = {
        "Fair": 0, "Good": 1, "New": 2, "Poor": 3
    }
    fuel_type_map = {
        "Diesel": 0, "Electric": 1, "Hybrid": 2
    }
    location_map = {
        "Rural": 0, "Suburban": 1, "Urban": 2
    }
    rental_duration_map = {
        "Long-Term": 0, "Short-Term": 1
    }
    technology_level_map = {
        "Advanced": 0, "Basic": 1, "Intermediate": 2
    }

    equipment_name_map= {'Combine Harvester Model 1': 0, 'Combine Harvester Model 10': 1, 'Combine Harvester Model 11': 2, 'Combine Harvester Model 12': 3, 'Combine Harvester Model 13': 4, 'Combine Harvester Model 14': 5, 'Combine Harvester Model 16': 6, 'Combine Harvester Model 17': 7, 'Combine Harvester Model 19': 8, 'Combine Harvester Model 2': 9, 'Combine Harvester Model 20': 10, 'Combine Harvester Model 21': 11, 'Combine Harvester Model 22': 12, 'Combine Harvester Model 23': 13, 'Combine Harvester Model 24': 14, 'Combine Harvester Model 25': 15, 'Combine Harvester Model 26': 16, 'Combine Harvester Model 27': 17, 'Combine Harvester Model 28': 18, 'Combine Harvester Model 29': 19, 'Combine Harvester Model 3': 20, 'Combine Harvester Model 30': 21, 'Combine Harvester Model 31': 22, 'Combine Harvester Model 33': 23, 'Combine Harvester Model 34': 24, 'Combine Harvester Model 35': 25, 'Combine Harvester Model 36': 26, 'Combine Harvester Model 37': 27, 'Combine Harvester Model 38': 28, 'Combine Harvester Model 39': 29, 'Combine Harvester Model 4': 30, 'Combine Harvester Model 40': 31, 'Combine Harvester Model 41': 32, 'Combine Harvester Model 42': 33, 'Combine Harvester Model 43': 34, 'Combine Harvester Model 44': 35, 'Combine Harvester Model 45': 36, 'Combine Harvester Model 47': 37, 'Combine Harvester Model 48': 38, 'Combine Harvester Model 49': 39, 'Combine Harvester Model 5': 40, 'Combine Harvester Model 50': 41, 'Combine Harvester Model 6': 42, 'Combine Harvester Model 7': 43, 'Combine Harvester Model 8': 44, 'Combine Harvester Model 9': 45, 'Cultivator Model 1': 46, 'Cultivator Model 10': 47, 'Cultivator Model 11': 48, 'Cultivator Model 12': 49, 'Cultivator Model 13': 50, 'Cultivator Model 14': 51, 'Cultivator Model 15': 52, 'Cultivator Model 16': 53, 'Cultivator Model 18': 54, 'Cultivator Model 19': 55, 'Cultivator Model 2': 56, 'Cultivator Model 20': 57, 'Cultivator Model 21': 58, 'Cultivator Model 22': 59, 'Cultivator Model 23': 60, 'Cultivator Model 24': 61, 'Cultivator Model 25': 62, 'Cultivator Model 26': 63, 'Cultivator Model 28': 64, 'Cultivator Model 3': 65, 'Cultivator Model 31': 66, 'Cultivator Model 32': 67, 'Cultivator Model 33': 68, 'Cultivator Model 34': 69, 'Cultivator Model 35': 70, 'Cultivator Model 36': 71, 'Cultivator Model 37': 72, 'Cultivator Model 38': 73, 'Cultivator Model 39': 74, 'Cultivator Model 40': 75, 'Cultivator Model 42': 76, 'Cultivator Model 43': 77, 'Cultivator Model 45': 78, 'Cultivator Model 46': 79, 'Cultivator Model 47': 80, 'Cultivator Model 48': 81, 'Cultivator Model 49': 82, 'Cultivator Model 5': 83, 'Cultivator Model 50': 84, 'Cultivator Model 6': 85, 'Cultivator Model 7': 86, 'Cultivator Model 8': 87, 'Cultivator Model 9': 88, 'Harrow Model 1': 89, 'Harrow Model 10': 90, 'Harrow Model 11': 91, 'Harrow Model 13': 92, 'Harrow Model 14': 93, 'Harrow Model 15': 94, 'Harrow Model 16': 95, 'Harrow Model 17': 96, 'Harrow Model 18': 97, 'Harrow Model 19': 98, 'Harrow Model 2': 99, 'Harrow Model 20': 100, 'Harrow Model 21': 101, 'Harrow Model 23': 102, 'Harrow Model 24': 103, 'Harrow Model 25': 104, 'Harrow Model 26': 105, 'Harrow Model 27': 106, 'Harrow Model 28': 107, 'Harrow Model 29': 108, 'Harrow Model 3': 109, 'Harrow Model 30': 110, 'Harrow Model 32': 111, 'Harrow Model 33': 112, 'Harrow Model 34': 113, 'Harrow Model 35': 114, 'Harrow Model 36': 115, 'Harrow Model 37': 116, 'Harrow Model 38': 117, 'Harrow Model 4': 118, 'Harrow Model 40': 119, 'Harrow Model 41': 120, 'Harrow Model 42': 121, 'Harrow Model 43': 122, 'Harrow Model 45': 123, 'Harrow Model 46': 124, 'Harrow Model 47': 125, 'Harrow Model 48': 126, 'Harrow Model 49': 127, 'Harrow Model 5': 128, 'Harrow Model 50': 129, 'Harrow Model 7': 130, 'Harrow Model 8': 131, 'Harrow Model 9': 132, 'Manure Spreader Model 1': 133, 'Manure Spreader Model 10': 134, 'Manure Spreader Model 11': 135, 'Manure Spreader Model 12': 136, 'Manure Spreader Model 13': 137, 'Manure Spreader Model 14': 138, 'Manure Spreader Model 15': 139, 'Manure Spreader Model 16': 140, 'Manure Spreader Model 17': 141, 'Manure Spreader Model 18': 142, 'Manure Spreader Model 19': 143, 'Manure Spreader Model 2': 144, 'Manure Spreader Model 21': 145, 'Manure Spreader Model 22': 146, 'Manure Spreader Model 23': 147, 'Manure Spreader Model 25': 148, 'Manure Spreader Model 26': 149, 'Manure Spreader Model 27': 150, 'Manure Spreader Model 28': 151, 'Manure Spreader Model 29': 152, 'Manure Spreader Model 3': 153, 'Manure Spreader Model 30': 154, 'Manure Spreader Model 31': 155, 'Manure Spreader Model 32': 156, 'Manure Spreader Model 33': 157, 'Manure Spreader Model 34': 158, 'Manure Spreader Model 35': 159, 'Manure Spreader Model 36': 160, 'Manure Spreader Model 37': 161, 'Manure Spreader Model 38': 162, 'Manure Spreader Model 39': 163, 'Manure Spreader Model 4': 164, 'Manure Spreader Model 40': 165, 'Manure Spreader Model 41': 166, 'Manure Spreader Model 42': 167, 'Manure Spreader Model 43': 168, 'Manure Spreader Model 45': 169, 'Manure Spreader Model 47': 170, 'Manure Spreader Model 48': 171, 'Manure Spreader Model 49': 172, 'Manure Spreader Model 5': 173, 'Manure Spreader Model 50': 174, 'Manure Spreader Model 6': 175, 'Manure Spreader Model 8': 176, 'Manure Spreader Model 9': 177, 'Mower Model 1': 178, 'Mower Model 11': 179, 'Mower Model 12': 180, 'Mower Model 13': 181, 'Mower Model 14': 182, 'Mower Model 15': 183, 'Mower Model 16': 184, 'Mower Model 17': 185, 'Mower Model 19': 186, 'Mower Model 2': 187, 'Mower Model 20': 188, 'Mower Model 21': 189, 'Mower Model 22': 190, 'Mower Model 23': 191, 'Mower Model 24': 192, 'Mower Model 25': 193, 'Mower Model 26': 194, 'Mower Model 27': 195, 'Mower Model 28': 196, 'Mower Model 29': 197, 'Mower Model 3': 198, 'Mower Model 30': 199, 'Mower Model 31': 200, 'Mower Model 32': 201, 'Mower Model 33': 202, 'Mower Model 34': 203, 'Mower Model 36': 204, 'Mower Model 37': 205, 'Mower Model 38': 206, 'Mower Model 39': 207, 'Mower Model 4': 208, 'Mower Model 40': 209, 'Mower Model 41': 210, 'Mower Model 42': 211, 'Mower Model 43': 212, 'Mower Model 44': 213, 'Mower Model 45': 214, 'Mower Model 46': 215, 'Mower Model 47': 216, 'Mower Model 48': 217, 'Mower Model 49': 218, 'Mower Model 5': 219, 'Mower Model 50': 220, 'Mower Model 6': 221, 'Mower Model 7': 222, 'Mower Model 8': 223, 'Mower Model 9': 224, 'Plough Model 1': 225, 'Plough Model 10': 226, 'Plough Model 11': 227, 'Plough Model 12': 228, 'Plough Model 13': 229, 'Plough Model 14': 230, 'Plough Model 15': 231, 'Plough Model 16': 232, 'Plough Model 17': 233, 'Plough Model 18': 234, 'Plough Model 19': 235, 'Plough Model 2': 236, 'Plough Model 20': 237, 'Plough Model 21': 238, 'Plough Model 23': 239, 'Plough Model 25': 240, 'Plough Model 27': 241, 'Plough Model 28': 242, 'Plough Model 29': 243, 'Plough Model 3': 244, 'Plough Model 30': 245, 'Plough Model 31': 246, 'Plough Model 32': 247, 'Plough Model 33': 248, 'Plough Model 34': 249, 'Plough Model 35': 250, 'Plough Model 36': 251, 'Plough Model 37': 252, 'Plough Model 38': 253, 'Plough Model 39': 254, 'Plough Model 4': 255, 'Plough Model 40': 256, 'Plough Model 41': 257, 'Plough Model 42': 258, 'Plough Model 43': 259, 'Plough Model 44': 260, 'Plough Model 45': 261, 'Plough Model 46': 262, 'Plough Model 47': 263, 'Plough Model 48': 264, 'Plough Model 49': 265, 'Plough Model 5': 266, 'Plough Model 50': 267, 'Plough Model 6': 268, 'Plough Model 7': 269, 'Plough Model 8': 270, 'Plough Model 9': 271, 'Seed Drill Model 1': 272, 'Seed Drill Model 10': 273, 'Seed Drill Model 11': 274, 'Seed Drill Model 12': 275, 'Seed Drill Model 13': 276, 'Seed Drill Model 14': 277, 'Seed Drill Model 15': 278, 'Seed Drill Model 16': 279, 'Seed Drill Model 17': 280, 'Seed Drill Model 18': 281, 'Seed Drill Model 19': 282, 'Seed Drill Model 2': 283, 'Seed Drill Model 20': 284, 'Seed Drill Model 21': 285, 'Seed Drill Model 22': 286, 'Seed Drill Model 23': 287, 'Seed Drill Model 24': 288, 'Seed Drill Model 25': 289, 'Seed Drill Model 26': 290, 'Seed Drill Model 27': 291, 'Seed Drill Model 28': 292, 'Seed Drill Model 29': 293, 'Seed Drill Model 3': 294, 'Seed Drill Model 30': 295, 'Seed Drill Model 31': 296, 'Seed Drill Model 32': 297, 'Seed Drill Model 33': 298, 'Seed Drill Model 36': 299, 'Seed Drill Model 37': 300, 'Seed Drill Model 38': 301, 'Seed Drill Model 39': 302, 'Seed Drill Model 4': 303, 'Seed Drill Model 40': 304, 'Seed Drill Model 41': 305, 'Seed Drill Model 42': 306, 'Seed Drill Model 43': 307, 'Seed Drill Model 44': 308, 'Seed Drill Model 46': 309, 'Seed Drill Model 48': 310, 'Seed Drill Model 49': 311, 'Seed Drill Model 5': 312, 'Seed Drill Model 50': 313, 'Seed Drill Model 6': 314, 'Seed Drill Model 7': 315, 'Seed Drill Model 9': 316, 'Sprayer Model 1': 317, 'Sprayer Model 10': 318, 'Sprayer Model 11': 319, 'Sprayer Model 12': 320, 'Sprayer Model 13': 321, 'Sprayer Model 14': 322, 'Sprayer Model 16': 323, 'Sprayer Model 17': 324, 'Sprayer Model 18': 325, 'Sprayer Model 19': 326, 'Sprayer Model 2': 327, 'Sprayer Model 20': 328, 'Sprayer Model 21': 329, 'Sprayer Model 22': 330, 'Sprayer Model 23': 331, 'Sprayer Model 24': 332, 'Sprayer Model 25': 333, 'Sprayer Model 26': 334, 'Sprayer Model 27': 335, 'Sprayer Model 28': 336, 'Sprayer Model 29': 337, 'Sprayer Model 30': 338, 'Sprayer Model 32': 339, 'Sprayer Model 33': 340, 'Sprayer Model 34': 341, 'Sprayer Model 35': 342, 'Sprayer Model 36': 343, 'Sprayer Model 37': 344, 'Sprayer Model 39': 345, 'Sprayer Model 4': 346, 'Sprayer Model 40': 347, 'Sprayer Model 41': 348, 'Sprayer Model 42': 349, 'Sprayer Model 43': 350, 'Sprayer Model 44': 351, 'Sprayer Model 45': 352, 'Sprayer Model 46': 353, 'Sprayer Model 47': 354, 'Sprayer Model 48': 355, 'Sprayer Model 49': 356, 'Sprayer Model 5': 357, 'Sprayer Model 6': 358, 'Sprayer Model 7': 359, 'Sprayer Model 8': 360, 'Tractor Model 1': 361, 'Tractor Model 10': 362, 'Tractor Model 11': 363, 'Tractor Model 12': 364, 'Tractor Model 14': 365, 'Tractor Model 15': 366, 'Tractor Model 16': 367, 'Tractor Model 18': 368, 'Tractor Model 19': 369, 'Tractor Model 2': 370, 'Tractor Model 20': 371, 'Tractor Model 22': 372, 'Tractor Model 23': 373, 'Tractor Model 24': 374, 'Tractor Model 25': 375, 'Tractor Model 26': 376, 'Tractor Model 28': 377, 'Tractor Model 29': 378, 'Tractor Model 3': 379, 'Tractor Model 30': 380, 'Tractor Model 31': 381, 'Tractor Model 34': 382, 'Tractor Model 35': 383, 'Tractor Model 36': 384, 'Tractor Model 37': 385, 'Tractor Model 39': 386, 'Tractor Model 4': 387, 'Tractor Model 40': 388, 'Tractor Model 41': 389, 'Tractor Model 42': 390, 'Tractor Model 43': 391, 'Tractor Model 44': 392, 'Tractor Model 45': 393, 'Tractor Model 46': 394, 'Tractor Model 47': 395, 'Tractor Model 48': 396, 'Tractor Model 49': 397, 'Tractor Model 50': 398, 'Tractor Model 6': 399, 'Tractor Model 7': 400, 'Tractor Model 8': 401, 'Tractor Model 9': 402}
    # Load the text from the pickle file and print it
    with open('smartai_text.pkl', 'rb') as file:
        loaded_text = pickle.load(file)

    print("this is the user name of the seller ",loaded_text)
    # Collect form data including mobile number, address, and pincode (unmapped)
    equipment_data = {
        'equipment_type': request.form['equipment_type'],
        'equipment_name': request.form['equipment_name'],
        'brand': request.form['brand'],
        'age': request.form['age'],
        'condition': request.form['condition'],
        'usage_frequency': request.form['usage_frequency'],
        'fuel_type': request.form['fuel_type'],
        'horsepower': request.form['horsepower'],
        'maintenance_score': request.form['maintenance_score'],
        'location': request.form['location'],
        'demand_level': request.form['demand_level'],
        'rental_duration_preference': request.form['rental_duration_preference'],
        'fuel_efficiency': request.form['fuel_efficiency'],
        'technology_level': request.form['technology_level'],
        'weather_dependency': request.form['weather_dependency'],
        'seasonal_demand_multiplier': request.form['seasonal_demand_multiplier'],
        'mobile_number': request.form['mobile_number'],
        'address': request.form['address'],
        'pincode': request.form['pincode'],
        'farmer_id': loaded_text ,
        'price': random.randint(500, 2000),
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }



    # Now, create a mapped (numerical) version of the data for ML processing
    mapped_data = {
        'equipment_type': equipment_type_map.get(equipment_data['equipment_type']),
        'equipment_name': equipment_name_map.get(equipment_data['equipment_name']),
        'brand': brand_map.get(equipment_data['brand']),
        'age': int(equipment_data['age']),  # Convert other fields to numerical if needed
        'condition': condition_map.get(equipment_data['condition']),
        'usage_frequency': int(equipment_data['usage_frequency']),
        'fuel_type': fuel_type_map.get(equipment_data['fuel_type']),
        'horsepower': int(equipment_data['horsepower']),
        'maintenance_score': int(equipment_data['maintenance_score']),
        'location': location_map.get(equipment_data['location']),
        'demand_level': int(equipment_data['demand_level']),
        'rental_duration_preference': rental_duration_map.get(equipment_data['rental_duration_preference']),
        'fuel_efficiency': float(equipment_data['fuel_efficiency']),
        'technology_level': technology_level_map.get(equipment_data['technology_level']),
        'weather_dependency': float(equipment_data['weather_dependency']),
        'seasonal_demand_multiplier': float(equipment_data['seasonal_demand_multiplier']),
    }

    # This mapped_data list can now be fed to your ML model

    print(mapped_data)
    # Convert mapped data into input format for the ML model
    input_list = list(mapped_data.values())
    input_array = np.array(input_list).reshape(1, -1)

    # Predict the price using the loaded model
    predicted_price = loaded_model.predict(input_array)[0]
    equipment_data['price'] = round(predicted_price, 2)  # Add predicted price to the data


    # Process and save images to static/images folder
    image_paths = []
    for i in range(1, 4):
        image_file = request.files.get(f'image{i}')
        if image_file:
            image = Image.open(image_file).convert('RGB')
            image = image.resize((256, 256))
            unique_filename = f"photo_{uuid.uuid4().hex}.png"
            image_path = os.path.join('static', 'images', unique_filename)
            image.save(image_path, format='PNG')
            image_paths.append(image_path)
        else:
            image_paths.append(None)
    
    # Add image paths to equipment data for reference (optional)
    equipment_data['image1'] = image_paths[0]
    equipment_data['image2'] = image_paths[1]
    equipment_data['image3'] = image_paths[2]
    # Save the updated equipment data to CSV
    csv_file = 'equipment_data.csv'
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=equipment_data.keys())
        if file.tell() == 0:  # Write header if file is empty
            writer.writeheader()
        writer.writerow(equipment_data)

    print("Data saved successfully with predicted price:", equipment_data['price'])
    return render_template('yield.html')

    

              
              # int_features3[0]==12345 and int_features3[1]==12345:
               #                      return render_template('index.html')
        
@app.route('/register',methods=['POST'])
def register():
    

    int_features2 = [str(x) for x in request.form.values()]
    #print(int_features2)
    #print(int_features2[0])
    #print(int_features2[1])
    r1=int_features2[0]
    print(r1)
    
    r2=int_features2[1]
    print(r2)
    logu1=int_features2[0]
    passw1=int_features2[1]
        
    

    

   # if int_features2[0]==12345 and int_features2[1]==12345:

    import MySQLdb


# Open database connection
    db = MySQLdb.connect(
    host=os.environ.get("DB_HOST", "localhost"),
    user=os.environ.get("DB_USER", "root"),
    passwd=os.environ.get("DB_PASSWORD", ""),
    db=os.environ.get("DB_NAME", "ddbb")
)


# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1=cursor.fetchall()
              #print(result1)
              #print(gmail1)
    for row1 in result1:
                      print(row1)
                      print(row1[0])
                      gmail_list1.append(str(row1[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    print(gmail_list1)
    if logu1 in gmail_list1:
                      return jsonify({'result':'this gmail is already in use '})  
    else:

                  #return jsonify({'result':'this  gmail is not registered'})
              

# Prepare SQL query to INSERT a record into the database.
                  sql = "INSERT INTO user_register(user,password) VALUES (%s,%s)"
                  val = (r1, r2)
   
                  try:
   # Execute the SQL command
                                       cursor.execute(sql,val)
   # Commit your changes in the database
                                       db.commit()
                  except:
   # Rollback in case there is any error
                                       db.rollback()

# disconnect from server
                  db.close()
                 # return jsonify({'result':'succesfully registered'})
                  return render_template('login44.html')

                      
# Route to the homepage with the search functionality
#@app.route('/')
#def index():
#    return render_template('index.html')

# Route to handle the search query
@app.route('/search', methods=['GET'])
def search():
    # Load the CSV data
    data_file = 'equipment_data.csv'
    df = pd.read_csv(data_file)
    equipment_type = request.args.get('equipment_type', '')
    
    # Filter the data for the entered equipment type
    filtered_df = df[df['equipment_type'].astype(str).str.contains(equipment_type, case=False, na=False)]
    
    # If no results found, return an empty list
    if filtered_df.empty:
        return jsonify({'results': []})
    
    # Sort the filtered DataFrame by price in ascending order
    filtered_df = filtered_df.sort_values(by='price', ascending=True)
    
    # Prepare the data to send to the front-end
    results = []
    for index, row in filtered_df.iterrows():
        equipment = {
            'equipment_type': row['equipment_type'],
            'equipment_name': row['equipment_name'],
            'brand': row['brand'],
            'age': row['age'],
            'condition': row['condition'],
            'usage_frequency': row['usage_frequency'],
            'fuel_type': row['fuel_type'],
            'horsepower': row['horsepower'],
            'maintenance_score': row['maintenance_score'],
            'location': row['location'],
            'demand_level': row['demand_level'],
            'rental_duration_preference': row['rental_duration_preference'],
            'fuel_efficiency': row['fuel_efficiency'],
            'technology_level': row['technology_level'],
            'weather_dependency': row['weather_dependency'],
            'seasonal_demand_multiplier': row['seasonal_demand_multiplier'],
            'mobile_number': row['mobile_number'],  # Added mobile number
            'address': row['address'],  # Added address
            'pincode': row['pincode'],  # Added pincode
            'farmer_id': row['farmer_id'],
            'price': row['price'],
            'timestamp': row['timestamp'],
            'image1': row['image1'],
            'image2': row['image2'],
            'image3': row['image3']
        }
        results.append(equipment)
    
    return jsonify({'results': results})



@app.route('/profile', methods=['GET'])
def profile():
    # Load the CSV data
    data_file = 'equipment_data.csv'
    df = pd.read_csv(data_file)
    
    # Load the previously saved user data
    with open('smartai_text.pkl', 'rb') as file:
        loaded_text = pickle.load(file)
    
    equipment_type = loaded_text
    
    # Filter the data for the entered equipment type
    filtered_df = df[df['farmer_id'].astype(str).str.contains(equipment_type, case=False, na=False)].reset_index()
    
    # If no results found, return an empty list
    if filtered_df.empty:
        return render_template('profile.html', results=[])
    
    # Sort the filtered DataFrame by price in ascending order
    filtered_df = filtered_df.sort_values(by='price', ascending=True)
    
    # Prepare the data to send to the front-end
    results = []
    for index, row in filtered_df.iterrows():
        equipment = {
            'id': row['index'],  # Include the index for deletion
            'equipment_type': row['equipment_type'],
            'equipment_name': row['equipment_name'],
            'brand': row['brand'],
            'age': row['age'],
            'condition': row['condition'],
            'usage_frequency': row['usage_frequency'],
            'fuel_type': row['fuel_type'],
            'horsepower': row['horsepower'],
            'maintenance_score': row['maintenance_score'],
            'location': row['location'],
            'demand_level': row['demand_level'],
            'rental_duration_preference': row['rental_duration_preference'],
            'fuel_efficiency': row['fuel_efficiency'],
            'technology_level': row['technology_level'],
            'weather_dependency': row['weather_dependency'],
            'seasonal_demand_multiplier': row['seasonal_demand_multiplier'],
            'mobile_number': row['mobile_number'],
            'address': row['address'],
            'pincode': row['pincode'],
            'farmer_id': row['farmer_id'],
            'price': row['price'],
            'timestamp': row['timestamp'],
            'image1': row['image1'],
            'image2': row['image2'],
            'image3': row['image3']
        }
        results.append(equipment)
    
    return render_template('profile.html', results=results)

@app.route('/delete_equipment/<int:row_index>', methods=['POST'])
def delete_equipment(row_index):
    # Load the CSV data
    data_file = 'equipment_data.csv'
    df = pd.read_csv(data_file)

    # Check if the row index exists
    if row_index < 0 or row_index >= len(df):
        return jsonify({"success": False, "message": "Invalid row index"}), 404

    # Drop the row with the specified index
    df = df.drop(index=row_index).reset_index(drop=True)

    # Save the updated dataset back to the file
    df.to_csv(data_file, index=False)

    return jsonify({"success": True, "message": "Equipment deleted successfully"}), 200


@app.route('/production')
def production(): 
    return render_template('yield.html')



@app.route('/production1')
def production1(): 
    return render_template('recommendation.html')

@app.route('/production11',methods=['GET', 'POST'])
def production11(): 
    return render_template('disease.html')




@app.route('/crop')
def crop():
     return render_template('recommendation.html')
if __name__ == "__main__":
    app.run()
