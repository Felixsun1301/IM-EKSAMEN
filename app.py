from flask import Flask, render_template, request, redirect
import mariadb

app = Flask(__name__)

def get_db():
    return mariadb.connect(
        host="192.168.1.209", # Endre tilbake til 10.200.14.27 på eksamen
        user="Fxwindows1", 
        password="Fx23",
        database="fxstudios"
    )

@app.route("/")
def index():
    return render_template("index.html")
         

@app.route("/booktime")
def booktime():
    return render_template("booktime.html")

@app.route("/book", methods=["POST"])   
def book():
    navn = request.form.get("navn")
    telefon = request.form.get("telefon")
    epost = request.form.get("epost")
    dato = request.form.get("dato")
    tid = request.form.get("tid")

    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO bookinger (navn, telefon, epost, dato, tid) VALUES (%s, %s, %s, %s, %s)",
        (navn, telefon, epost, dato, tid)
    )
    db.commit()
    cursor.close()
    db.close()

 
    return redirect("/bekreftelse?navn=" + navn + "&dato=" + dato + "&tid=" + tid)

@app.route("/bekreftelse")
def bekreftelse():
    navn = request.args.get("navn")
    dato = request.args.get("dato")
    tid = request.args.get("tid")
    return render_template("bekreftelse.html", navn=navn, dato=dato, tid=tid)

# Viser innloggingssiden
@app.route("/admin")
def admin():
    return render_template("admin.html")

# Sjekker brukernavn og passord
@app.route("/login", methods=["POST"])
def login():
    brukernavn = request.form.get("brukernavn")
    passord = request.form.get("passord")

    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM admin WHERE brukernavn = %s AND passord = %s",
        (brukernavn, passord)
    )
    bruker = cursor.fetchone()
    cursor.close()
    db.close()

    if bruker:
        return redirect("/bookinger")
    else:
        return render_template("admin.html", feil="Feil brukernavn eller passord")

# Viser alle bookinger
@app.route("/bookinger")
def bookinger():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM bookinger")
    alle = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template("bookinger.html", bookinger=alle)

# Viser FAQ-siden med vanlige spørsmål
@app.route("/faq")
def faq():
    return render_template("faq.html")

# Tar imot spørsmål fra brukeren og lagrer i databasen
@app.route("/send_sporsmal", methods=["POST"])
def send_sporsmal():
    navn = request.form.get("navn")
    epost = request.form.get("epost")
    sporsmal = request.form.get("sporsmal")

    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO faq (navn, epost, sporsmal) VALUES (%s, %s, %s)",
        (navn, epost, sporsmal)
    )
    db.commit()
    cursor.close()
    db.close()

    return redirect("/faq")

# Sletter alle spørsmål tilknyttet en e-post (GDPR)
@app.route("/slett_data", methods=["POST"])
def slett_data():
    epost = request.form.get("epost")

    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "DELETE FROM faq WHERE epost = %s",
        (epost,)
    )
    db.commit()
    cursor.close()
    db.close()

    return redirect("/faq")


if __name__ == "__main__":
    app.run(debug=True)