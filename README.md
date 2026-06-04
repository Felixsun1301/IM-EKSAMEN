Prosjektbeskrivelse og dokumentasjon
Prosjekttittel: FX Studios - Bookingsystem for frisorsalong
Kandidat: Felix Sun

1. Prosjektide og problemstilling
Hva er prosjektet?
Jeg har laget et bookingsystem for min egen frisorsalong, FX Studios, som ligger i Oslo. Ideen kom fra at mange frisorsalonger bruker telefon eller meldinger for a ta imot bestillinger, noe som kan bli rotete og uoversiktlig. Jeg ville lage en enkel losning der kunder kan booke time pa nett nar det passer dem.

Hva gjor applikasjonen?
Applikasjonen lar kunder ga inn pa en nettside, velge dato og tid, fylle inn navn, telefonnummer og e-post, og bekrefte bookingen. Informasjonen lagres i en database. Administrator kan logge inn og se alle bookinger som er registrert. Det finnes ogsa en FAQ-side der kunder kan lese vanlige sporsmal og sende inn egne sporsmal.

Hva skal jeg gjore pa eksamensdagen?
Jeg starter med a sikre at Raspberry Pi er pa og at MariaDB kjorer. Deretter starter jeg Flask med python app.py og tester at alle sider fungerer. Jeg viser sensor hele flyten fra forside til bekreftelse, logger inn som admin og viser bookingsoversikten, og demonstrerer FAQ-siden. Til slutt forklarer jeg koden og svarer pa sporsmal.

Kanban-board: https://github.com/Felixsun1301/IM-TEST-EKSAMEN

2. Systembeskrivelse
Formal med applikasjonen
Jeg onsket a lage en enkel og brukervennlig losning for FX Studios slik at kunder kan booke time uten a ma ringe. Malet var at systemet skulle vare enkelt a bruke, at data skulle lagres trygt i en database, og at jeg som administrator skulle ha oversikt over alle bookinger.

Brukerflyt
Brukeren apner forsiden og ser tre valg: Book en time, FAQ og Admin innlogging. Hvis brukeren velger a booke, fyller de inn dato, tid og kontaktinfo og trykker send. Flask tar imot dataene, lagrer dem i MariaDB og sender brukeren til en bekreftelsesside. Administrator kan logge inn med brukernavn og passord for a se alle bookinger.

Teknologier brukt
•	HTML / CSS - frontend og brukergrensesnitt
•	Python / Flask - backend og ruting
•	MariaDB - database for lagring av bookinger, admin og FAQ-sporsmal

3. Server-, infrastruktur- og nettverksoppsett
Servermiljo
Databasen kjorer pa en Raspberry Pi med Ubuntu/Linux. Flask kjorer lokalt pa Windows-PC under utvikling.

Nettverksoppsett
•	Klient (nettleser) sender foresporsler til Flask pa localhost:5000
•	Flask kommuniserer med MariaDB pa Raspberry Pi via IP-adresse og port 3306
•	Klient -> Flask (port 5000) -> MariaDB pa Pi (port 3306)

IP-adresser og porter
•	Flask: localhost:5000
•	MariaDB: 10.200.x.x:3306 (Pi-ens IP-adresse)

Tjenestekonfigurasjon
MariaDB startes pa Pi med: sudo systemctl start mariadb
Flask startes pa Windows med: python app.py

4. Prosjektstyring - GitHub Projects (Kanban)
Jeg har brukt GitHub Projects til a organisere arbeidet med To Do, In Progress og Done. Dette hjalp meg med a holde oversikt over hva som var ferdig og hva som gjensto. Det var spesielt nyttig nar jeg jobbet med flere funksjoner samtidig, som admin-innlogging og FAQ.

Kanban-lenke: https://github.com/Felixsun1301/IM-TEST-EKSAMEN

5. Databasebeskrivelse
Databasenavn: fxstudios

Tabeller og felt:

Tabell	Felt	Datatype	Beskrivelse
bookinger	id	INT	Primaernokkel
bookinger	navn	VARCHAR(100)	Kundens navn
bookinger	telefon	VARCHAR(20)	Telefonnummer
bookinger	epost	VARCHAR(100)	E-postadresse
bookinger	dato	DATE	Valgt dato
bookinger	tid	TIME	Valgt tidspunkt
admin	id	INT	Primaernokkel
admin	brukernavn	VARCHAR(50)	Admin brukernavn
admin	passord	VARCHAR(50)	Admin passord
faq	id	INT	Primaernokkel
faq	navn	VARCHAR(100)	Navn pa bruker
faq	epost	VARCHAR(150)	E-post til bruker
faq	sporsmal	TEXT	Brukerens sporsmal
faq	opprettet	DATETIME	Tidspunkt for innsending

6. Programstruktur
fxstudios/
├── app.py
├── templates/
│   ├── index.html
│   ├── booktime.html
│   ├── bekreftelse.html
│   ├── admin.html
│   ├── bookinger.html
│   └── faq.html
└── static/
    └── style.css

Databasestrom: HTML → Flask → MariaDB → Flask → HTML

7. Kodeforklaring
Ruter i app.py
•	/ - viser forsiden (index.html)
•	/booktime - viser bookingskjemaet
•	/book - tar imot POST-data fra skjemaet og lagrer i databasen
•	/bekreftelse - viser bekreftelsesside etter vellykket booking
•	/admin - viser innloggingssiden for administrator
•	/login - sjekker brukernavn og passord mot databasen
•	/bookinger - viser alle bookinger (krever innlogging)
•	/faq - viser FAQ-siden
•	/send_sporsmal - lagrer sporsmal fra bruker i databasen
•	/slett_data - sletter alle sporsmal tilknyttet en e-post (GDPR)

8. Sikkerhet og palitelighet
•	Parameterisert SQL: bruker %s istedenfor direkte inndata for a beskytte mot SQL injection
•	Admin-innlogging: kun administrator kan se bookingsoversikten
•	GDPR: brukere kan slette egne persondata via e-post
•	Validering: HTML required-attributt pa alle skjemafelt

9. Feilsoking og testing
Typiske feil jeg stotte pa
•	MariaDB koblet ikke til - losning: bind-address endret til 0.0.0.0 pa Pi
•	TemplateNotFound - losning: HTML-filer laa ikke i templates/-mappen
•	Feil lenker i HTML - losning: brukte Flask-ruter som /booktime istedenfor filstier
•	IP-adresse endret seg - losning: oppdaterte host i app.py med ny IP

Testmetoder
•	Testet alle sider manuelt i nettleseren
•	Registrerte testkunder og verifiserte med SELECT * FROM bookinger
•	Testet innlogging med feil passord for a sjekke feilmelding
•	Testet GDPR-sletting og verifiserte at data ble fjernet fra databasen

10. Konklusjon og refleksjon
Hva larte jeg?
Jeg larte hvordan Flask kommuniserer med en database, og hvordan man sender data fra et HTML-skjema til Python. Jeg larte ogsa mye om nettverksoppsett siden databasen kjorer pa en Raspberry Pi og ikke lokalt.

Hva fungerte bra?
Selve bookingflyten fungerte bra fra start. CSS-en ble ryddig og enkel. Databasetilkoblingen fungerte etter at jeg endret bind-address pa Pi-en.

Hva ville jeg gjort annerledes?
Jeg ville brukt .env-fil for passord og brukernavn istedenfor a skrive det direkte i koden. Jeg ville ogsa satt opp HTTPS og e-postbekreftelse til kunden.

Hva var utfordrende?
Det vanskeligste var a fa Flask pa Windows til a koble til MariaDB pa Raspberry Pi. Det tok tid a finne ut at bind-address matte endres og at brukeren trengte tilgang utenfra.

11. Kildeliste
•	https://www.w3schools.com
•	https://flask.palletsprojects.com
•	https://mariadb.com/kb/en/documentation/
•	https://jinja.palletsprojects.com
https://www.geeksforgeeks.org/python/template-inheritance-in-flask/ - Kilde for {% extends "index.html" %} brukt på html sidene

