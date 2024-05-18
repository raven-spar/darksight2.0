from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Scss(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db = SQLAlchemy(app)

class Mytask(db.Model): 
    email = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100))
    pass_hash = db.Column(db.String(200))
    ph_no = db.Column(db.String(13))
    

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)