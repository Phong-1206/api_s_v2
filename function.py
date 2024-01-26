import json
import random
def img():
  img = ["https://cdn.dribbble.com/users/1186261/screenshots/3718681/_______.gif"]
  return random.choice(img)
def info_phone(phone):
  filename='data.json'
  with open(filename,'r') as file:
    file_data = json.load(file)
    for data in file_data:
      if data["Phone"] in str(phone):
        return data
        break