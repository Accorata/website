# print("sdjfh")

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def load_main () :
    return render_template("home.html")

@app.route("/data")
def load_data () :
    return render_template("data.html")

if __name__ == "__main__":
    app.debug = True
    app.run(port='1026')