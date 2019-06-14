import os
import sec
from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
	if request.form:
        print(request.form)
    return render_template("index.html")

@app.route("/profile", methods=["GET"])
def profile():
	return render_template("profile.html")

	
if __name__ == "__main__":
    app.run(debug=True)