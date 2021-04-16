from flask import Flask, request, Markup, render_template, flash, Markup 
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    print("RunningMain")
    with open('medal_of_honor.json') as name_data:
        recipients = json.load(name_data)
        
    if 'recipients' in request.args:
        return render_template('page1.html', recipients = get_name_options(name), average_age = average_age(get_name_recipient(request.args['name'],name), name), name = get_name_options(get_name_recipient(request.args['name'],name),medals), name_age = get_name_age(request.args['medals'],medals))
    if 'medals' in request.args:
        return render_template('page1.html', recipients = get_name_options(name), average_age = average_age(request.args['states'], name), name = get_name_options(request.args['recipients'],name))
   
    elif 'recipients' not in request.args and 'name' not in request.args:
        return render_template('page1.html', recipients = get_recipient_options(name))
def get_recipient_options(medals):
    recipients = []
    print("RunningOP")
    for data in medals:
        if data["Recipient"] not in recipients:
            states.append(data["Recipient"])
    options = ""
    for data in recipients:
        options = options + Markup("<option value="" + data + "">" + data + "</option>")
    return options

def average_age(recipient, medals):
    print("RunningAge")
    points = float(0)
    total = float(0)
    for medal in medals:
        if medal["Recipient"] == recipient:
            total = total +medal["Age"]["Percent Under 18 Years"]
            points=points + 1
    avg = float(total//points)
    return avg

def get_medal_options(recipients,medals):
   medallist = []
    print("RunningCOP")
    for medal in medals:
        if medal["Recipient"] == medals :
            medallist.append(medal["Medal"])
    options = ""
    for data in medallist:
        options = options + Markup("<option value="" + data + "">" + data + "</option>")
    return options

def get_medal_age(medal, medals):
    print("RunningCAge")
    for medal1 in medals:
        if medal1["Medal"] == medal:
            return medal1["Age"]["Percent Under 18 Years"]
 
def get_medal_recipient(medal, medals):
    print("RunningRecipient")
    recipient = ""
    for data in medals:
        if data["Medal"] == medal:
            recipient = data["Medal"]
    return recipient

if name == "main":
    app.run(debug=True)
