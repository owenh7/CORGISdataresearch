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
        return render_template('page2.html', states = get_state_options(counties), average_issued = average_issued(get_county_state(request.args['counties'],counties), counties), counties = get_county_options(get_county_state(request.args['counties'],counties),counties), county_issued = get_county_issued(request.args['counties'],counties))
    if 'states' in request.args:
        return render_template('page2.html', states = get_state_options(counties), average_issued = average_issued(request.args['states'], counties), counties = get_county_options(request.args['states'],counties))
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
        options = options + Markup("<option value=\"" + data + "\">" + data + "</option>")
    return options

def average_issued(state, counties):
    print("RunningAge")
    points = float(0)
    total = float(0)
    for county in counties:
        if county["name"] == state:
            total = total + county["awarded"]
            points=points + 1
    avg = float(total//points)
    return avg
    
def get_county_options(states,counties):
    countylist = []
    print("RunningCOP")
    for county in counties:
        if county["name"] == states :
            countylist.append(county["County"])
    options = ""
    for data in countylist:
        options = options + Markup("<option value=\"" + data + "\">" + data + "</option>")
    return options
    
def get_county_age(county, counties):
    print("RunningCAge")
    for county1 in counties:
        if county1["issued"] == county:
            return county1["issued"]
 
def get_county_state(county, counties):
    print("RunningState")
    state = ""
    for data in counties:
        if data["issued"] == county:
            state = data["name"]
    return state
    return render_template('page2.html')
@app.route("/p3")
def render_first3():
    return render_template('page3.html')
@app.route("/p4")
def render_first4():
    return render_template('page4.html')

if __name__ == "__main__":
    app.run(debug=True)
