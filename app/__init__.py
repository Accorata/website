# print("sdjfh")

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def load_main () :
    return "a"

if __name__ == "__main__":
    app.debug = True
    app.run(port='5000')
