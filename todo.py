from operator import ne
import re
from flask import Flask, render_template, redirect, url_for, request
import flask
from flask.helpers import flash
from flask_sqlalchemy import SQLAlchemy

# connect db browser
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/kudec/Desktop/python/Flask - Uygulamalı Dökümanlar/todo_app/todo.db'
db = SQLAlchemy(app)

class Todo (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean) # gönderilen notların değeri false yada true olarak bakılacak

# HTML TEMPLATES FUNCTION

@app.route("/add",methods=["POST"])
def add_todo():
    # veriler kayıt ediliyor.
    title = request.form.get("title")
    new_todo = Todo(title = title, complete = False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))
   
@app.route("/ending/<string:id>")
def complete_todo(id):
    filter_todo = Todo.query.filter_by(id=id).first()
    filter_todo.complete = not filter_todo.complete
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def delete(id):
    delete_todo = Todo.query.filter_by(id=id).first()
    db.session.delete(delete_todo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/")
def index():
    # veriler index sayfasına çekiliyor.
    todos = Todo.query.all()
    
    
    return render_template("index.html", todos = todos)


    





















if __name__ == "__main__":
    db.create_all() # uygulama açılmadan tablo oluşturulacak. eğer yoksa
    app.run(debug=True)
        