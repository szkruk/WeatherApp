 
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)  
import requests, datetime ,sqlite3

bp = Blueprint('home', __name__, url_prefix='/')

def connect_db():
    connection = sqlite3.connect('./database.db') 
    return connection

def get_db():
    if not hasattr(g,'sqlite3'):
        g.sqlite3_db = connect_db()
    return g.sqlite3_db

 
@bp.route('/home',methods = ('GET','POST'))
def home():   
    db = get_db()
    # cursor = db.cursor()
    # data = cursor.execute('SELECT * FROM results').fetchall()
    # print(data)
    if request.method == 'POST': 
        print(request.form)
        city = request.form["city"]
        obj = {} 
        if city:
            ress = get_weather_info(city) 
            if ress['cod']==200 :
                obj= {
                    "city_name":ress["name"],
                    "temp" : round(ress["main"]["feels_like"]-273.15,1),
                    "temp_min" : round(ress["main"]["temp_min"]-273.15,1),
                    "temp_max" : round(ress["main"]["temp_max"]-273.15,1),
                    "humidity" : ress["main"]["humidity"],
                    "wind" : ress["wind"]["speed"],
                    "main_weather" : ress["weather"][0]["main"] ,
                    "vis" : round(ress["visibility"]/10000,2),
                    "date" : datetime.datetime.now().strftime("%c") 
                } 
                return render_template('index.html',**obj)   
        return render_template("home.html", error= 1)
    return render_template("home.html", error= 0)

 
def get_weather_info(name_city):
    url_key = "a317ee35a2765c697275078137a6b7fc" 
    api_url = "https://api.openweathermap.org/data/2.5/weather?q="+name_city+"&appid="+url_key
    try:
        return requests.get(api_url).json() 
    except:
        pass  