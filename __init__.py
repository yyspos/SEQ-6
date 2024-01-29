from flask import Flask
from flask import render_template
from flask import json
import mysql.connector

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

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
    conn = mysql.connector.connect(
    host='localhost',
    user='boris',
    password='Scooter90%1',
    database='boris_BDD'
    )
                                                                                                                                       
if __name__ == "__main__":
  app.run(debug=True)
