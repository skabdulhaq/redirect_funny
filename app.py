from flask import Flask, redirect
import random, requests

app = Flask(__name__)


@app.route("/")
def home():
    url = "https://api.npoint.io/ebbdbf2551af841022dc"
    list_website =  requests.get(url).json()["list"]
    return redirect(random.choice(list_website))

if __name__ == "__main__":
    app.run()