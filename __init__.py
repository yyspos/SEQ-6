from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
import http.client
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

   # Construisez dynamiquement une chaîne de modèle HTML
    template_string = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Bibliotheque</title>
    </head>
    <body>
        <h1>Contenu de la base de données</h1>
        <table border="1">
            <tr>
                <th>ID</th>
                <th>DATE</th>
                <th>TITRE</th>
                <th>AUTEUR</th>
            </tr>
            {% for row in data %}
            <tr>
                <td>{{ row[0] }}</td>
                <td>{{ row[1] }}</td>
                <td>{{ row[2] }}</td>
                <td>{{ row[3] }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
    return render_template_string(template_string, data=data)

@app.route('/api/meteo/')
def meteo():
    connection = http.client.HTTPSConnection('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    connection.request('GET', '/')
    response = connection.getresponse()
    return f'Response status code: {response.status}'
                                                                                                                                       
if __name__ == "__main__":
  app.run(debug=True)
