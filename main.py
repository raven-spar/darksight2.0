from flask import Flask, render_template, redirect , request
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
    

@app.route("/",methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        try:
            mail = request.form['content']
            query = Mytask.query.filter_by(email = mail).all()
            return render_template('index.html', response=query)
        except Exception as e:
            print(f"error:{e}")
            return f"error:{e}"
    else:
        return render_template("index.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)