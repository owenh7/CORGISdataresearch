from flask import Flask, request, Markup, render_template, flash, Markup 
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    print("RunningMain")
    with open('medal_of_honor.json') as name_data:
        recipients = json.load(name_data)
        
       class User:
        def__init__(name, death, citation):
            self.guid = guid
            
       @classmethod     
        def from_json(cls, json_string):
           json_dict = json.loads(json_string)\
            return cls(**json_dict)
        
       
        
        
  
