from flask import Flask,send_file 
import re
from flask import render_template, request, redirect, url_for 
import pandas as pd 
from sqlalchemy import create_engine
from models import db, Throwersd 
from io import BytesIO
import matplotlib.pyplot as plt

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:991550sp@localhost/postgres' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False  

db.init_app(app)



@app.route('/') 
def index():
  result = Throwersd.query.order_by("spbest desc").all()
  
  return render_template('form1.html', result = result)

@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']
	year = request.form['year']
	
	spbest = request.form['spbest']
	bp = request.form['bp']
	squat = request.form['squat']
	clean = request.form['clean']
	signature = Throwersd(name=name, year=year,spbest=spbest,bp=bp,squat=squat,clean=clean)
	db.session.add(signature)
	db.session.commit()

	return redirect(url_for('index'))

@app.route('/adddata')
def sign():
	return render_template('sign.html')

@app.route('/plot')
def plot():
  dsn = create_engine('postgresql+psycopg2://postgres:991550sp@localhost/postgres')  # Use ENV vars: keep it secret, keep it safe
  df = pd.read_sql_query ('select * from throwersd where bp > 10', con = dsn)
  #print (df)
  
  fig = plt.scatter([df.spbest],[df.bp])
  img = BytesIO()
    
  plt.savefig(img)
  img.seek(0)
  return send_file(img, mimetype='image/png')
  

@app.route('/links')
def links():
    links = ['http://www.willcountythrows.com', 'http://www.willcountythrows.com','https://www.twitter.com']
    return render_template('links.html', links = links)



if __name__ == '__main__' :
    app.run(debug=True) 
    