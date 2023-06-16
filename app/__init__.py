# print("sdjfh")

from flask import Flask, render_template, redirect, request
import sqlite3

app = Flask(__name__)

@app.route("/", methods=['GET'])
def load_main () :
    return render_template("home.html")

@app.route("/data", methods=['GET'])
def load_data () :
    return render_template("data.html")

@app.route("/process_sent_data", methods=['POST'])
def process_sent_data () :
    name = request.form.get("name")
    print("name: "+name)
    return "Done"

if __name__ == "__main__":
    app.debug = True
    app.run(port='1026')
