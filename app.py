from flask import Flask, redirect
import requests

app = Flask(__name__)


@app.route("/<index>")
def manager(index):
    url = "https://api.npoint.io/83316894f4c0ca891969"
    list_website =  requests.get(url).json()["list"]
    return redirect(list_website[int(index)])

if __name__ == "__main__":
    app.run()