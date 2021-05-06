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
    if 'names' in request.args:
        return render_template('layout.html', years = get_year_options(names), average_age = average_age(get_name_year(request.args['names'],names), names), names = get_name_options(get_name_year(request.args['names'],names),names), names_age = get_name_age(request.args['names'],names))
    if 'years' in request.args:
        return render_template('layout.html', years = get_year_options(names), average_age = average_age(request.args['years'], names), names = get_name_options(request.args['years'],names))
    elif 'years' not in request.args and 'names' not in request.args:
        return render_template('layout.html', years = get_year_options(names))

def get_year_options(names):
    years = []
    print("RunningOP")
    for data in names:
        if data["birth.date.year"] not in years:
            years.append(data["birth.date.year"])
    options = ""
    for data in years:
        options = options + Markup("<option value=\"" + data + "\">" + data + "</option>")
    return options

def average_age(year, names):
    print("RunningAge")
    points = float(0)
    total = float(0)
    for name in names:
        if name["birth.date.year"] == year:
            total = total + name["Age"]["Percent Under 18 Years"]
            points=points + 1
    avg = float(total//points)
    return avg
    
def get_name_options(years,names):
    namelist = []
    print("RunningCOP")
    for name in names:
        if name["birth.date.year"] == years :
            namelist.append(name["Name"])
    options = ""
    for data in namelist:
        options = options + Markup("<option value=\"" + data + "\">" + data + "</option>")
    return options
    
def get_name_age(name, names):
    print("RunningCAge")
    for name1 in names:
        if name1["Name"] == name:
            return name1["Age"]["Percent Under 18 Years"]
 
def get_name_year(name, names):
    print("RunningYear")
    year = ""
    for data in names:
        if data["Name"] == name:
            year = data["birth.date.year"]
    return year
 
@app.route("/p3")
def render_first3():
    return render_template('page3.html')
@app.route("/p4")
def render_first4():
    return render_template('page4.html')

if __name__ == "__main__":
    app.run(debug=True)
