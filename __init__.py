from flask import Flask
from flask import render_template
from flask import json
import mysql.connector

app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/fr/')
def hello_world_fr():
    return "<h2>Bonjour tout le monde !</h2>"

# Création d'une nouvelle route pour la lecture de la BDD
@app.route('/lecture/')
def ReadBDD():
  mysql = MySQL()
  app.config['MYSQL_DATABASE_HOST'] = 'localhost'
  app.config['MYSQL_DATABASE_USER'] = 'boris'
  app.config['MYSQL_DATABASE_PASSWORD'] = 'Scooter90%1'
  app.config['MYSQL_DATABASE_DB'] = 'boris_BDD'
  mysql.init_app(app)
  cursor = mysql.connect().cursor()
  return "BDD"
                                                                                                                                       
if __name__ == "__main__":
  app.run(debug=True)
