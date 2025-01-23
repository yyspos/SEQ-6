from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from functools import wraps

app = Flask(__name__)
app.secret_key = 'bibliotheque_secrete'  # Clé secrète pour la gestion des sessions


# Fonction pour se connecter à la base de données
def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection


# Décorateur pour restreindre l'accès à certaines routes
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Vous devez être connecté pour accéder à cette page.", "danger")
            return redirect(url_for('auth'))
        return f(*args, **kwargs)
    return decorated_function


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('role') != 'Administrateur':
            flash("Accès réservé aux administrateurs.", "danger")
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function


# Route pour l'accueil
@app.route('/')
def index():
    query = request.args.get('query', '').strip()
    books = []
    if query:
        connection = get_db_connection()
        cur = connection.cursor()
        cur.execute("SELECT * FROM livres WHERE titre LIKE ?", ('%' + query + '%',))
        books = cur.fetchall()
        connection.close()
    return render_template('index.html', books=books, query=query)


# Routes pour la gestion des livres
@app.route('/livres', methods=['GET', 'POST'])
@login_required
@admin_required
def livres():
    connection = get_db_connection()
    cur = connection.cursor()
    if request.method == 'POST':
        titre = request.form['titre']
        auteur = request.form['auteur']
        categorie = request.form['categorie']
        stock = request.form['stock']
        cur.execute("INSERT INTO livres (titre, auteur, categorie, stock) VALUES (?, ?, ?, ?)",
                    (titre, auteur, categorie, stock))
        connection.commit()
        flash("Livre ajouté avec succès.", "success")
    cur.execute("SELECT * FROM livres")
    livres = cur.fetchall()
    connection.close()
    return render_template('livres.html', livres=livres)


@app.route('/livres/supprimer/<int:livre_id>')
@login_required
@admin_required
def supprimer_livre(livre_id):
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute("DELETE FROM livres WHERE id = ?", (livre_id,))
    connection.commit()
    connection.close()
    flash("Livre supprimé avec succès.", "success")
    return redirect(url_for('livres'))


# Routes pour la gestion des emprunts
@app.route('/emprunts', methods=['GET', 'POST'])
@login_required
def emprunts():
    connection = get_db_connection()
    cur = connection.cursor()
    if request.method == 'POST':
        id_utilisateur = request.form['utilisateur']
        id_livre = request.form['livre']
        cur.execute("INSERT INTO emprunts (id_utilisateur, id_livre, date_retour_prevue) VALUES (?, ?, date('now', '+7 days'))",
                    (id_utilisateur, id_livre))
        cur.execute("UPDATE livres SET stock = stock - 1 WHERE id = ?", (id_livre,))
        connection.commit()
        flash("Emprunt ajouté avec succès.", "success")
    cur.execute("""
        SELECT e.id, u.nom AS utilisateur, l.titre AS livre, e.date_retour_prevue, e.statut
        FROM emprunts e
        JOIN utilisateurs u ON e.id_utilisateur = u.id
        JOIN livres l ON e.id_livre = l.id
    """)
    emprunts = cur.fetchall()
    cur.execute("SELECT * FROM utilisateurs")
    utilisateurs = cur.fetchall()
    cur.execute("SELECT * FROM livres WHERE stock > 0")
    livres = cur.fetchall()
    connection.close()
    return render_template('emprunts.html', emprunts=emprunts, utilisateurs=utilisateurs, livres=livres)


@app.route('/emprunts/retourner/<int:emprunt_id>')
@login_required
def retourner_emprunt(emprunt_id):
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute("UPDATE emprunts SET statut = 'Retourné', date_retour_effective = date('now') WHERE id = ?", (emprunt_id,))
    cur.execute("UPDATE livres SET stock = stock + 1 WHERE id = (SELECT id_livre FROM emprunts WHERE id = ?)", (emprunt_id,))
    connection.commit()
    connection.close()
    flash("Livre retourné avec succès.", "success")
    return redirect(url_for('emprunts'))


# Routes pour la gestion des utilisateurs
@app.route('/utilisateurs', methods=['GET', 'POST'])
@login_required
@admin_required
def utilisateurs():
    connection = get_db_connection()
    cur = connection.cursor()
    if request.method == 'POST':
        nom = request.form['nom']
        email = request.form['email']
        mot_de_passe = request.form['mot_de_passe']
        role = request.form['role']
        cur.execute("INSERT INTO utilisateurs (nom, email, mot_de_passe, role) VALUES (?, ?, ?, ?)",
                    (nom, email, mot_de_passe, role))
        connection.commit()
        flash("Utilisateur ajouté avec succès.", "success")
    cur.execute("SELECT * FROM utilisateurs")
    utilisateurs = cur.fetchall()
    connection.close()
    return render_template('utilisateurs.html', utilisateurs=utilisateurs)


@app.route('/utilisateurs/supprimer/<int:utilisateur_id>')
@login_required
@admin_required
def supprimer_utilisateur(utilisateur_id):
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute("DELETE FROM utilisateurs WHERE id = ?", (utilisateur_id,))
    connection.commit()
    connection.close()
    flash("Utilisateur supprimé avec succès.", "success")
    return redirect(url_for('utilisateurs'))


# Routes pour l'authentification
@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        email = request.form['email']
        mot_de_passe = request.form['mot_de_passe']
        connection = get_db_connection()
        cur = connection.cursor()
        cur.execute("SELECT * FROM utilisateurs WHERE email = ? AND mot_de_passe = ?", (email, mot_de_passe))
        utilisateur = cur.fetchone()
        connection.close()
        if utilisateur:
            session['user_id'] = utilisateur['id']
            session['nom'] = utilisateur['nom']
            session['role'] = utilisateur['role']
            flash("Connexion réussie.", "success")
            return redirect(url_for('index'))
        else:
            flash("Identifiants incorrects.", "danger")
    return render_template('auth.html')


@app.route('/logout')
@login_required
def logout():
    session.clear()
    flash("Déconnexion réussie.", "success")
    return redirect(url_for('auth'))


if __name__ == "__main__":
    app.run(debug=True)
