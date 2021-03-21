#!/usr/bin/python3
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__) 

@app.route("/")
def defult():
	return redirect(url_for('home'))
		
@app.route("/<name>")
def name(name):
	return redirect(url_for('home'))	
#-----------------------------------#	
@app.route("/home")
def home():
	return render_template("index.html")
	
@app.route("/logon")
def logon():
	return render_template("logon.html")
	
@app.route("/reg")
def reg():
	return render_template("reg.html")
#------------------------------------#
if __name__ =="__main__":
	app.run()
	#app.run(debug=True)
