import requests
import json
from datetime import datetime
import os

NUTRITION_API_KEY = os.environ.get("NUTRITION_KEY")#"1810f5e4b152f266a803d31053fa7ce1"
APPLICATION_ID = os.getenv("APPLICATION_ID")  #"3d6ac3ab"
sheety_token = os.environ.get('SHEETY_TOKEN')
sheety_header ={"Authorization": f"Bearer {sheety_token}"}

SHEETY_API_GET ="https://api.sheety.co/3a8941c417b2613f150a106ec690cf06/exercise/workouts"
SHEETY_API_POST = "https://api.sheety.co/3a8941c417b2613f150a106ec690cf06/exercise/workouts"

nutrition_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_input = input("Write what have you done: ")
header = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": NUTRITION_API_KEY,
}
data = {
    'query': user_input,
    "gender": "male",
    "weight_kg": 81,
    "height_cm": 183,
    "age": 29
}
response = requests.post(url=nutrition_URL, headers=header, data=json.dumps(data))
print(response.status_code)
print(json.loads(response.text))

nutrition_data = json.loads(response.text)
user_exercise = nutrition_data['exercises'][0]["name"]
duration = nutrition_data['exercises'][0]["duration_min"]
calories = nutrition_data['exercises'][0]["nf_calories"]

date  = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

sheety_data ={
    "workout":{
        "date": f'{date}',
        "time": f"{time}",
        "exercise": user_exercise.title(),
        "duration": duration,
        "calories": calories
    }
}



sheety_request = requests.get(url=SHEETY_API_POST, headers= sheety_header)

print(sheety_request.json())

sheety_add_row = requests.post(url=SHEETY_API_POST, json= sheety_data, headers= sheety_header)
print(sheety_add_row.text)
