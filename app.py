from flask import Flask, render_template

app = Flask(__name__)

# Anunturi afisate pe site. Pentru un anunt nou: copiaza imaginea in
# static/images/anunturi/ si adauga o intrare la inceputul listei.
# Cel mai recent anunt activ apare pe prima pagina; toate cele active apar pe /anunturi.
ANUNTURI = [
    {
        "slug": "angajare-mecanici-2026",
        "eticheta": "Angajari",
        "titlu": "Angajam mecanici auto",
        "descriere": "Hai in echipa noastra! Cautam mecanici auto cu experienta, "
                     "dornici sa lucreze intr-un service modern din Domnesti, Ilfov.",
        "beneficii": [
            "Mediu de lucru profesional si stabil",
            "Salariu atractiv, in functie de experienta",
            "Posibilitati de dezvoltare profesionala",
            "Echipa tanara si dinamica",
        ],
        "telefoane": ["0773 847 746", "0754 235 006"],
        "imagine": "images/anunturi/angajare-mecanici-2026-800.jpg",
        "imagine_full": "images/anunturi/angajare-mecanici-2026.jpg",
        "data": "Septembrie 2026",
        "activ": True,
    },
]


def anunturi_active():
    return [a for a in ANUNTURI if a.get("activ")]


@app.route("/")
def index():
    active = anunturi_active()
    return render_template("index.html", anunt=active[0] if active else None)


@app.route("/servicii")
def servicii():
    return render_template("servicii.html")


@app.route("/despre")
def despre():
    return render_template("despre.html")


@app.route("/galerie")
def galerie():
    return render_template("galerie.html")


@app.route("/anunturi")
def anunturi():
    return render_template("anunturi.html", anunturi=anunturi_active())


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
