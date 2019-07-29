from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    
@app.route('/favorites',methods=["GET","POST"])
def favorites():
    if request.method=="GET":
        return render_template("index.html")
    else:
        userdata = request.form
        genre = userdata['genre']
        return render_template('genre.html', genre=genre)
        
@app.route('/dishes')
def dishes():
    return render_template('recipe.html')
    
