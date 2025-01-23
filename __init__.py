from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Fonction pour se connecter à la base de données
def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row  # Permet d'accéder aux colonnes par nom
    return connection

# Route pour la page d'accueil avec la barre de recherche
@app.route('/', methods=['GET'])
def accueil():
    query = request.args.get('query', '').strip()  # Récupérer la recherche de l'utilisateur
    books = []
    if query:
        connection = get_db_connection()
        cur = connection.cursor()
        cur.execute("SELECT * FROM livres WHERE titre LIKE ?", ('%' + query + '%',))
        books = cur.fetchall()
        connection.close()
    return render_template('index.html', books=books, query=query)

if __name__ == "__main__":
    app.run(debug=True)
