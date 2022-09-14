import json
import requests
import pandas as pd
URL = 'http://127.0.0.1:8000/bookapi/'

def post_data():
    df = pd.read_csv('books_name(id) - Sheet1.csv')
    for student,name in zip(df.id, df.book):
        data = {
            'student':student,
            'name':name,
        }
        r = requests.post(url=URL,data=data)
        data = r.json()
        print(data)

post_data()