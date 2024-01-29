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
    conn = mysql.connector.connect(
    host='localhost',
    user='boris',
    password='Scooter90%1',
    database='boris_BDD'
    )
    cursor = conn.cursor()
    # Execute a query
    cursor.execute("SELECT * FROM livres")
    # Fetch and print the results
    print(cursor.fetchone())
    # Close the connection
    conn.close()
                                                                                                                                       
if __name__ == "__main__":
  app.run(debug=True)
