from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", cuisineList=model.cuisineList)
    
@app.route('/favorites',methods=["GET","POST"])
def favorites():
    if request.method=="GET":
        return render_template("index.html", cuisineList=model.cuisineList)
    else:
        userdata = request.form
        cuisine = userdata['cuisine']
        ## concatenate url string to query the API
        ## query the API
        ## set this query to dishes
        dishes = model.meals(cuisine)
        code = model.code(cuisine)
        return render_template('genre.html', cuisine=cuisine, dishes=dishes, code=code)
        
@app.route('/dishes',methods=["GET","POST"])
def recipe():
    if request.method=="GET":
        return render_template("index.html", cuisineList=model.cuisineList)
    else:
        userdata = request.form
        meal = userdata['meal']
        recipe = model.recipes(meal)
        return render_template('recipe.html', meal=meal, recipe=recipe)
        
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')