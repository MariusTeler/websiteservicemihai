from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/servicii")
def servicii():
    return render_template("servicii.html")


@app.route("/despre")
def despre():
    return render_template("despre.html")


@app.route("/galerie")
def galerie():
    return render_template("galerie.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
