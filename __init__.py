from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Fonction pour se connecter à la base de données
def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row  # Pour un accès facile aux colonnes par nom
    return connection

# Route pour la page d'accueil avec recherche
@app.route('/')
def accueil():
    return render_template('index.html')

# Route pour gérer la recherche de livres
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip()
    books = []
    if query:
        connection = get_db_connection()
        cur = connection.cursor()
        cur.execute("SELECT * FROM livres WHERE titre LIKE ?", ('%' + query + '%',))
        books = cur.fetchall()
        connection.close()
    return render_template('search_results.html', books=books, query=query)

# Route pour la page Catalogue
@app.route('/catalogue')
def catalogue():
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute("SELECT * FROM livres")
    livres = cur.fetchall()
    connection.close()
    return render_template('catalogue.html', livres=livres)

# Route pour la page Emprunts
@app.route('/emprunts')
def emprunts():
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute("""
        SELECT e.id, u.nom AS utilisateur, l.titre AS livre, e.date_retour_prevue, e.statut
        FROM emprunts e
        JOIN utilisateurs u ON e.id_utilisateur = u.id
        JOIN livres l ON e.id_livre = l.id
    """)
    emprunts = cur.fetchall()
    connection.close()
    return render_template('emprunts.html', emprunts=emprunts)

# Route pour la page Contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
