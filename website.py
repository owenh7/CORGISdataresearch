from flask import Flask, request, Markup, render_template, flash, Markup 
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    print("RunningMain")
    with open('medal_of_honor.json') as name_data:
        recipients = json.load(name_data)
        
        people_string = '''
        {
            "people": [
            {
             "name": "Sagelhurst, John C.",
             "awarded": {
            "General Order number": -1,
            "accredited to": "",
            "citation": "Under a heavy fire from the enemy carried off the field a commissioned officer who was severely wounded and also led a charge on the enemy's rifle pits.",
             "issued": "01/03/1906",
             "date": {
             "day": 6,
             "full": "1865-2-6",
             "month": 2,
              "year": 1865
                },
              "name": "Hack, John",
              "awarded": {
              "General Order number": -1,
              "accredited to": "",
              "citation": "Was one of a party which volunteered and attempted to run the enemy's batteries with a steam tug and 2 barges loaded with subsistence stores.",
              "issued": "01/03/1907",
              "date": {
              "day": 3,
              "full": "1863-5-3",
              "month": 5,
              "year": 1863
                },
              ]
             }
             '''
        
        data = json.loads(people_string)
        
        print(data)
        
        
  
