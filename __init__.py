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
    # Convertit la liste de livre en un format JSON
    json_posts = [{'id': post['id'], 'title': post['title'], 'content': post['auteur']} for post in posts]
    # Renvoie la réponse JSON
    return jsonify(data=json_posts)
                                                                                                                                       
if __name__ == "__main__":
  app.run(debug=True)
