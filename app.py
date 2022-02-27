from cmath import log10
from flask import Flask,render_template,request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("./index.html")

@app.route("/submit",methods=["POST"])
def aaa():
    a=request.form['Name']
    b=request.form['Item']
    d=request.form['nos']
    #e=input("did u complete?")

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SavvyCoderz",database='svc'
    )

    c = mydb.cursor()

    adding=("INSERT INTO svc.orders (Name, Item, Nos) VALUES (%s, %s, %s)")
    c.execute(adding,(a,b,d))
    mydb.commit()
    #c.execute("DELETE FROM orders WHERE Name='%s'",(e))
    c.execute("SELECT * FROM orders")

    res = c.fetchall()

    l=[]

    for i in res:
        l.append(i)

    return str(l)

@app.route("/l")
def nukj():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SavvyCoderz",database='svc'
    )

    c = mydb.cursor()

    c.execute("INSERT INTO svc.orders (Name) VALUES (")

    res = c.fetchall()

    
@app.route('/x')
def xyz():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SavvyCoderz",database='svc'
    )

    c = mydb.cursor()

    c.execute("DELETE FROM orders WHERE Name='rithik01")

    c.execute("SELECT * FROM orders")

    res = c.fetchall()

    l=[]

    for i in res:
        l.append(i)

    return str(l)

app.run(debug=True)