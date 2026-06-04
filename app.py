from flask import Flask, render_template, request, redirect
import mariadb

app = Flask(__name__)

def get_db():
    return mariadb.connect(
        host="10.200.14.27", 
        user="Fxwindows1", 
        password="Fx23",
        database="fxstudios"
    )

# FORSIDE
# Når brukeren går til localhost:5000 vises index.html
@app.route("/")
def index():
    return render_template("index.html")
         
# BOOKINGSIDE
# Når brukeren trykker "Book en time" på forsiden
# vises bookingskjemaet
@app.route("/booktime")
def booktime():
    return render_template("booktime.html")

# LAGRE BOOKING
# Når brukeren trykker "Book time" i skjemaet
# henter vi dataene og lagrer dem i databasen.
# methods=["POST"] betyr at denne ruten kun tar imot
# data fra skjemaer, ikke vanlige sidebesøk
@app.route("/book", methods=["POST"])   
def book():
    # Henter det brukeren fylte inn i skjemaet
    navn = request.form.get("navn")
    telefon = request.form.get("telefon")
    epost = request.form.get("epost")
    dato = request.form.get("dato")
    tid = request.form.get("tid")

 # Kobler til databasen og setter inn bookingen
    db = get_db()
    cursor = db.cursor() # cursor brukes til å kjøre SQL
    
    # Lagrer bookingen i databasen.
    # Vi bruker %s istedenfor verdiene direkte - dette
    # kalles parameterisert SQL og beskytter mot SQL injection
    cursor.execute(
        "INSERT INTO bookinger (navn, telefon, epost, dato, tid) VALUES (%s, %s, %s, %s, %s)",
        (navn, telefon, epost, dato, tid)
    )
    db.commit()  # lagrer endringen permanent
    cursor.close() # lukker cursor
    db.close() # lukker tilkoblingen

  # Sender brukeren til bekreftelsessiden med navn, dato og tid i URL-en
    return redirect("/bekreftelse?navn=" + navn + "&dato=" + dato + "&tid=" + tid)

# BEKREFTELSESSIDE
# Henter navn, dato og tid fra URL-en og viser
# bekreftelse.html med disse verdiene
@app.route("/bekreftelse")
def bekreftelse():
    navn = request.args.get("navn")
    dato = request.args.get("dato")
    tid = request.args.get("tid")
    return render_template("bekreftelse.html", navn=navn, dato=dato, tid=tid)

# Viser innloggingssiden for administratorer
@app.route("/admin")
def admin():
    return render_template("admin.html")

# SJEKK INNLOGGING
# Når admin trykker "Logg inn" sjekker vi om
# brukernavn og passord finnes i databasen
# Sjekker brukernavn og passord
@app.route("/login", methods=["POST"])
def login():
    brukernavn = request.form.get("brukernavn")
    passord = request.form.get("passord")

    db = get_db()
    cursor = db.cursor()

     # Søker etter brukeren i admin-tabellen
     # Bruker %s her også for sikkerhet mot SQL injection
    cursor.execute(
        "SELECT * FROM admin WHERE brukernavn = %s AND passord = %s",
        (brukernavn, passord)
    )
    bruker = cursor.fetchone()
    cursor.close()
    db.close()

    if bruker: # Brukernavn og passord stemmer - send til bookingsoversikten
        return redirect("/bookinger")
    else: # Feil innlogging - vis feilmelding på innloggingssiden
        return render_template("admin.html", feil="Feil brukernavn eller passord")

# BOOKINGSOVERSIKT
# Henter alle bookinger fra databasen og viser dem
# i en tabell. Kun synlig etter innlogging
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

# FAQ-SIDE
# Viser vanlige spørsmål og svar, samt skjema
# for å sende inn egne spørsmål
# Viser FAQ-siden med vanlige spørsmål
@app.route("/faq")
def faq():
    return render_template("faq.html")

# LAGRE SPØRSMÅL
# Når brukeren sender inn et spørsmål via FAQ-siden
# lagres det i faq-tabellen i databasen
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

    return redirect("/faq") # sender brukeren tilbake til FAQ-siden

# SLETT DATA (GDPR - The General Data Protection Regulation)
# Brukeren kan skrive inn e-posten sin og få slettet
# alle spørsmål tilknyttet den e-posten.
# Dette er vår GDPR-funksjon - retten til å bli glemt
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

# STARTER FLASK
# Kjøres når du skriver: python app.py
# debug=True viser feilmeldinger i nettleseren og gjør at serveren starter på nytt når du endrer i koden
if __name__ == "__main__":
    app.run(debug=True)