import flask

from lists_forever import app


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
    return flask.render_template("index.html")


@app.route("/anime", methods=["GET"])
def anime():
    return flask.render_template("anime.html")


@app.route("/games", methods=["GET"])
def games():
    return flask.render_template("games.html")
