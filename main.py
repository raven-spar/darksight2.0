from flask import Flask, render_template, redirect , request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
import scrape 
import random

app = Flask(__name__)
Scss(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db = SQLAlchemy(app)

class Mytask(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(50))
    name = db.Column(db.String(100))
    address= db.Column(db.String(200))
    ph_no = db.Column(db.String(13))
    

@app.route("/index",methods = ['POST','GET'])
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
    
@app.route("/mail-pass", methods = ['POST','GET'])
def mail_pass():
    if request.method == 'POST':
        try:
            mail = request.form['content']
            passwd = scrape.mail_pass(mail)
            return render_template("mail_pass.html", response=passwd)   
        except Exception as e:
            print(f"error:{e}")
            return f"error:{e}"
    else:
        return render_template("mail_pass_get.html")
    
@app.route("/",methods = ['POST','GET'])
def breaches():
    if request.method == "POST":
        try:
            data = request.form['content']
            res = [0,0,0,0,0]
            results = Mytask.query.filter_by(email = data).all()
            for result in results:
                res[0]= result.name[0:3] + '*' * (len(result.name) - 3)
                res[1] = result.email
                res[2] = '*' * 7 + result.ph_no[7:]
                res[3] = '*'*(len(result.address)-10) + result.address[-10:]
                res[4] = 'Boat'

            return render_template("breaches.html", response=res)
        except Exception as e:
            print(f"error:{e}")
            return f"error:{e}"
    else:
        return render_template("breaches_get.html")
        
# @app.route("/pass",methods = ['POST','GET'])
# def password():
#     if request.method == "POST":
#         try:
#             passwd = request.form['content']
#             breached = scrape.password(passwd)
#             return render_template("pass.html", response=breached)
#         except Exception as e:
#             print(f"error:{e}")
#             return f"error:{e}"
#     else:
#         return render_template("pass.html")

def db_pop():
    with open('lol.txt') as file:
        j = 1
        for i in file.readlines():
            print(j)
            data = i.split('\t')
            # print(data)
            t = Mytask(id=j, name=data[0], email=data[1], ph_no=data[2], address=data[3])
            try:
                db.session.add(t)
                db.session.commit()
            except Exception as e:
                print(e)
            j += 1

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        #db_pop()
        # tasks = Mytask.query.order_by(Mytask.id).all()
        # for task in tasks:
        #     print(task.email)
    app.run(debug=True)