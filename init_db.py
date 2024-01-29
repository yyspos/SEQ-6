import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO livres (title, auteur) VALUES (?, ?)",
            ('Moby-Dick', 'Herman Melville')
            )

cur.execute("INSERT INTO livres (title, auteur) VALUES (?, ?)",
            ('Notre-Dame de Paris', 'Victor Hugo')
            )

cur.execute("INSERT INTO livres (title, auteur) VALUES (?, ?)",
            ('CosmoZ', 'Christophe Claro')
            )

cur.execute("INSERT INTO livres (title, auteur) VALUES (?, ?)",
            ('La reine du crime', 'Agatha Christie')
            )


connection.commit()
connection.close()
