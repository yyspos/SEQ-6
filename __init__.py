from flask import Flask
from flask import render_template
from flask import json
import sqlite3

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
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres;')
    data = cursor.fetchall()
    conn.close()

    # Construisez un dictionnaire avec les données
    json_posts = [{'colonne1': row[0], 'colonne2': row[1]} for row in data]
    # Ajoutez d'autres clés au dictionnaire en fonction de la structure de votre base de données

    # Renvoyez les données au format JSON
    return jsonify(data=json_posts)
                                                                                                                                       
if __name__ == "__main__":
  app.run(debug=True)
