from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def accueil():
    return render_template('index.html')

@app.route('/catalogue')
def catalogue():
    return render_template('catalogue.html')

@app.route('/emprunts')
def emprunts():
    return render_template('emprunts.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
