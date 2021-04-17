from flask import Flask, request, Markup, render_template, flash, Markup 
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    print("RunningMain")
    with open('medal_of_honor.json') as medalofhonor_data:
        names = json.load(medalofhonor_data)
    return render_template('index.html')
        
    if 'names' in request.args:
        return render_template('page1.html', citations = get_citation_options(names), average_age = average_age(get_names_citation(request.args['names'],names), names), names = get_name_options(get_name_citation(request.args['names'],names),names), name_age = get_name_age(request.args['names'],names))
    if 'citations' in request.args:
        return render_template('page1.html', citations = get_citation_options(names), average_age = average_age(request.args['citations'], names), names = get_name_options(request.args['citations'],names))
   
    elif 'citations' not in request.args and 'names' not in request.args:
        return render_template('page1.html', citations = get_citation_options(names))
def get_citation_options(names):
    citations = []
    print("RunningOP")
    for data in names:
        if data["Citation"] not in states:
            citations.append(data["Citation"])
    options = ""
    for data in citations:
        options = options + Markup("<option value="" + data + "">" + data + "</option>")
    return options

def average_age(citation, names):
    print("RunningAge")
    points = float(0)
    total = float(0)
    for name in names:
        if name["Citation"] == citation:
            total = total + name["Age"]["Percent Under 18 Years"]
            points=points + 1
    avg = float(total//points)
    return avg

def get_county_options(states,counties):
    countylist = []
    print("RunningCOP")
    for county in counties:
        if county["State"] == states :
            countylist.append(county["County"])
    options = ""
    for data in countylist:
        options = options + Markup("<option value="" + data + "">" + data + "</option>")
    return options

def get_county_age(county, counties):
    print("RunningCAge")
    for county1 in counties:
        if county1["County"] == county:
            return county1["Age"]["Percent Under 18 Years"]
 
def get_county_state(county, counties):
    print("RunningState")
    state = ""
    for data in counties:
        if data["County"] == county:
            state = data["State"]
    return state

if __name__ == "__main__":
    app.run(debug=True)
        
  
