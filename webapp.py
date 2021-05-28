from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__, template_folder='templates')


@app.route("/")
def render_main():
    print("RunningMain")
    return render_template('layout.html')
@app.route("/p1")
def render_first():
    return render_template('page1.html')
@app.route("/p2")
def render_first2():
    with open('medal_of_honor.json') as medal_data:
        counties = json.load(medal_data)
    if 'counties' in request.args:
        return render_template('page2.html', states = get_state_options(counties), awarded_citation = awarded_citation(get_issued_state(request.args['counties'],counties), counties), counties = get_issued_options(get_issued_state(request.args['counties'],counties),counties), issued_awarded = get_issued_awarded(request.args['counties'],counties))
    if 'states' in request.args:
        return render_template('page2.html', states = get_state_options(counties), awarded_citation = awarded_citation(request.args['states'], counties), counties = get_issued_options(request.args['states'],counties))
    elif 'states' not in request.args and 'counties' not in request.args:
        return render_template('page2.html', states = get_state_options(counties))
    

def get_state_options(counties):
    states = []
    print("RunningOP")
    for data in counties:
        if data["name"] not in states:
            states.append(data["name"])
    options = ""
    for data in states:
        options = options + Markup("<option value=\"" + str(data) + "\">" + str(data) + "</option>")
    return options

def awarded_citation(state, counties):
    print("RunningAge")
    points = float(0)
    total = float(0)
    for issued in counties:
        if issued["name"] == state:
            total = issued["awarded"]["citation"]
    return total
def get_issued_options(states,counties):
    issuedlist = []
    print("RunningCOP")
    for issued in counties:
        if issued["name"] == states :
            issuedlist.append(["issued"])
    options = ""
    for data in issuedlist:
        options = options + Markup("<option value=\"" + str(data) + "\">" + str(data) + "</option>")
    return options
    
def get_issued_awarded(issued, counties):
    print("RunningCAge")
    for issued1 in counties:
        if issued1["issued"] == issued:
            return issued1["awarded"]["citation"]
 
def get_issued_state(issued, counties):
    print("RunningState")
    state = ""
    for data in counties:
        if data["issued"] == issued:
            state = data["name"]
    return state
    return render_template('page2.html')
@app.route("/p3")
def render_first3():
    with open('medal_of_honor.json') as medal_data:
        counties = json.load(medal_data)
    if 'counties' in request.args:
        return render_template('page3.html', states = get_state_options(counties), military record_organization = military record_organization(get_issued_state(request.args['counties'],counties), counties), counties = get_issued_options(get_issued_state(request.args['counties'],counties),counties), issued_military record = get_issued_military record(request.args['counties'],counties))
    if 'states' in request.args:
        return render_template('page3.html', states = get_state_options(counties), military record_organization = military record_organization(request.args['states'], counties), counties = get_issued_options(request.args['states'],counties))
    elif 'states' not in request.args and 'counties' not in request.args:
        return render_template('page3.html', states = get_state_options(counties))
    

def get_state_options(counties):
    states = []
    print("RunningOP")
    for data in counties:
        if data["name"] not in states:
            states.append(data["name"])
    options = ""
    for data in states:
        options = options + Markup("<option value=\"" + str(data) + "\">" + str(data) + "</option>")
    return options

def military record_organization(state, counties):
    print("RunningAge")
    points = float(0)
    total = float(0)
    for issued in counties:
        if issued["name"] == state:
            total = issued["military record"]["orginization"]
    return total
def get_issued_options(states,counties):
    issuedlist = []
    print("RunningCOP")
    for issued in counties:
        if issued["name"] == states :
            issuedlist.append(["issued"])
    options = ""
    for data in issuedlist:
        options = options + Markup("<option value=\"" + str(data) + "\">" + str(data) + "</option>")
    return options
    
def get_issued_awarded(issued, counties):
    print("RunningCAge")
    for issued1 in counties:
        if issued1["issued"] == issued:
            return issued1["military record"]["orginization"]
 
def get_issued_state(issued, counties):
    print("RunningState")
    state = ""
    for data in counties:
        if data["issued"] == issued:
            state = data["name"]
    return state
    return render_template('page3.html')
@app.route("/p4")
def render_first4():
    return render_template('page4.html')

if __name__ == "__main__":
    app.run(debug=True)
