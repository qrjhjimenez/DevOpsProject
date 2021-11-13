from flask import Flask
from flask import request
from flask import render_template

web = Flask(__name__)

@web.route("/")

def main():
    return render_template("index.html")

if __name__ == "__main__":
    web.run(host="0.0.0.0", port=8080)
