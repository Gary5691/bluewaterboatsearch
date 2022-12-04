#!/usr/bin/env python3

from flask import Flask, render_template

from werkzeug.middleware.proxy_fix import ProxyFix


app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)


@app.route("/")
def index():
    with open("templates/search_boats.html", "r") as results:
        result = results.read()
        return render_template("index.html", return_results=result)


if __name__ == "__main__":
    app.run("0.0.0.0", "8000")
