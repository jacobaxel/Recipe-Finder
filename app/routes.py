from app import app
from flask import render_template, request, session, redirect
from app.models import model, formopener
import random

app.secret_key=b'>C\xad\n\xc4\xbb\xd9/ \xe7\x8d\xdf?EY\xab\xa1\\\x8bd(\xa3\xf5z'

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", cuisineList=model.cuisineList)
    
@app.route('/favorites',methods=["GET","POST"])
def favorites():
    if request.method=="GET":
        return redirect('/')
    else:
        userdata = request.form
        if 'cuisine' not in userdata:
            # cuisine = 'American'
            cuisine = random.choice(model.cuisineList)['strArea']
            session['cuisine'] = model.code(cuisine)['cuisine']
            dishes = model.meals(session['cuisine'])
            code = model.code(cuisine)['code']
            return render_template('genre.html', cuisine=cuisine, dishes=dishes, code=code)
        cuisine = userdata['cuisine']
        session['cuisine'] = model.code(cuisine)['cuisine']
        dishes = model.meals(session['cuisine'])
        code = model.code(cuisine)['code']
        return render_template('genre.html', cuisine=cuisine, dishes=dishes, code=code)
        
@app.route('/dishes',methods=["GET","POST"])
def recipe():
    if request.method=="GET":
        return redirect('/')
    else:
        userdata = request.form
        if 'meal' not in userdata:
            meal = random.choice(model.meals(session['cuisine']))['strMeal']
            session['meal']=meal
            recipe = model.recipes(session['meal'])
            return render_template('recipe.html', meal=meal, recipe=recipe)
        meal = userdata['meal']
        session['meal']=meal
        recipe = model.recipes(session['meal'])
        return render_template('recipe.html', meal=meal, recipe=recipe)
        
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')