from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__, template_folder='templates')


@app.route("/")
def render_main():
    print("RunningMain")
    with open('medal_of_honor.json') as medal_data:
        names = json.load(medal_data)
    return render_template('page1.html')
@app.route("/p1")
def render_first():
    return render_template('page1.html')
@app.route("/p2")
def render_first2():
    return render_template('page2.html')
@app.route("/p3")
def render_first3():
    return render_template('page3.html')
@app.route("/p4")
def render_first4():
    return render_template('page4.html')


        
     if 'names' in request.args:
        return render_template('main.html', years = get_year_options(counties), average_age = average_age(get_county_year(request.args['counties'],counties), counties), counties = get_county_options(get_county_year(request.args['counties'],counties),counties), county_age = get_county_age(request.args['counties'],counties))
    if 'years' in request.args:
        return render_template('main.html', years = get_year_options(counties), average_age = average_age(request.args['years'], counties), counties = get_county_options(request.args['years'],counties))
    elif 'years' not in request.args and 'counties' not in request.args:
        return render_template('main.html', years = get_year_options(counties))

def get_year_options(counties):
    years = []
    print("RunningOP")
    for data in counties:
        if data["Year"] not in years:
            years.append(data["Year"])
    options = ""
    for data in years:
        options = options + Markup("<option value=\"" + data + "\">" + data + "</option>")
    return options

def average_age(year, counties):
    print("RunningAge")
    points = float(0)
    total = float(0)
    for county in counties:
        if county["Year"] == year:
            total = total + county["Age"]["Percent Under 18 Years"]
            points=points + 1
    avg = float(total//points)
    return avg
    
def get_county_options(years,counties):
    countylist = []
    print("RunningCOP")
    for county in counties:
        if county["Year"] == years :
            countylist.append(county["County"])
    options = ""
    for data in countylist:
        options = options + Markup("<option value=\"" + data + "\">" + data + "</option>")
    return options
    
def get_county_age(county, counties):
    print("RunningCAge")
    for county1 in counties:
        if county1["County"] == county:
            return county1["Age"]["Percent Under 18 Years"]
 
def get_county_year(county, counties):
    print("RunningYear")
    year = ""
    for data in counties:
        if data["County"] == county:
            year = data["Year"]
    return year
if __name__ == "__main__":
    app.run(debug=True)
