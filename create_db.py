import sqlite3

# Connexion à la base de données
connection = sqlite3.connect('database.db')

# Lecture et exécution du fichier SQL pour créer les tables
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Insertion des données dans la table utilisateurs
cur.execute("INSERT INTO utilisateurs (nom, email, mot_de_passe, role) VALUES (?, ?, ?, ?)", ('Admin', 'admin@example.com', 'password123', 'Administrateur'))
cur.execute("INSERT INTO utilisateurs (nom, email, mot_de_passe, role) VALUES (?, ?, ?, ?)", ('Dupont', 'emilie.dupont@example.com', 'userpassword', 'Utilisateur'))
cur.execute("INSERT INTO utilisateurs (nom, email, mot_de_passe, role) VALUES (?, ?, ?, ?)", ('Leroux', 'lucas.leroux@example.com', 'userpassword', 'Utilisateur'))
cur.execute("INSERT INTO utilisateurs (nom, email, mot_de_passe, role) VALUES (?, ?, ?, ?)", ('Dagare', 'yann.dagare@example.com', 'password123', 'Administrateur'))


# Insertion des données dans la table livres
cur.execute("INSERT INTO livres (titre, auteur, categorie, isbn, stock) VALUES (?, ?, ?, ?, ?)", ('Le Petit Prince', 'Antoine de Saint-Exupéry', 'Littérature', '9782070612758', 5))
cur.execute("INSERT INTO livres (titre, auteur, categorie, isbn, stock) VALUES (?, ?, ?, ?, ?)", ('1984', 'George Orwell', 'Science-fiction', '9780451524935', 3))
cur.execute("INSERT INTO livres (titre, auteur, categorie, isbn, stock) VALUES (?, ?, ?, ?, ?)", ('Les Misérables', 'Victor Hugo', 'Classique', '9782070402036', 4))
cur.execute("INSERT INTO livres (titre, auteur, categorie, isbn, stock) VALUES (?, ?, ?, ?, ?)", ('La Peste', 'Albert Camus', 'Philosophie', '9780141185132', 6))
cur.execute("INSERT INTO livres (titre, auteur, categorie, isbn, stock) VALUES (?, ?, ?, ?, ?)", ('Le Rouge et le Noir', 'Stendhal', 'Classique', '9780140447644', 2))

# Insertion des données dans la table emprunts
cur.execute("INSERT INTO emprunts (id_utilisateur, id_livre, date_retour_prevue, statut) VALUES (?, ?, ?, ?)", (2, 1, '2025-01-25', 'En cours'))
cur.execute("INSERT INTO emprunts (id_utilisateur, id_livre, date_retour_prevue, statut) VALUES (?, ?, ?, ?)", (3, 2, '2025-01-20', 'Retourné'))
cur.execute("INSERT INTO emprunts (id_utilisateur, id_livre, date_retour_prevue, statut) VALUES (?, ?, ?, ?)", (2, 3, '2025-01-15', 'En retard'))

# Insertion des données dans la table notifications
cur.execute("INSERT INTO notifications (id_utilisateur, id_emprunt, message, vu) VALUES (?, ?, ?, ?)", (2, 1, 'Votre emprunt de "Le Petit Prince" est en retard. Merci de le retourner rapidement.', 0))
cur.execute("INSERT INTO notifications (id_utilisateur, id_emprunt, message, vu) VALUES (?, ?, ?, ?)", (3, 2, 'Merci d\'avoir retourné "1984".', 1))

# Insertion des données dans la table rapports
cur.execute("INSERT INTO rapports (type_rapport, contenu) VALUES (?, ?)", ('Statistique', "Rapport mensuel d'utilisation des livres."))
cur.execute("INSERT INTO rapports (type_rapport, contenu) VALUES (?, ?)", ('Rappel', 'Liste des livres en retard ce mois-ci.'))

# Validation et fermeture de la connexion
connection.commit()
connection.close()
