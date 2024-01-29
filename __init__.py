from flask import Flask, render_template_string
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
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contenu de la base de données</title>
    </head>
    <body>
        <h1>Contenu de la base de données</h1>
        <table border="1">
            <tr>
                <th>Colonne1</th>
                <th>Colonne2</th>
                <!-- Ajoutez d'autres en-têtes de colonne selon votre structure de base de données -->
            </tr>
            {% for row in data %}
            <tr>
                <td>{{ row[0] }}</td>
                <td>{{ row[1] }}</td>
                <!-- Ajoutez d'autres colonnes selon votre structure de base de données -->
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """

    # Renvoyez la chaîne de modèle HTML directement
    return render_template_string(template_string, data=data)
                                                                                                                                       
if __name__ == "__main__":
  app.run(debug=True)
