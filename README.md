# FX Studios – Bookingsystem

Navn Felix

Klasse: 2IMI

## Om prosjektet
FX Studios er en frisørsalong som trenger en enkel måte for kunder å booke time på nett. Brukeren velger dato og tid, fyller inn kontaktinfo og får en bekreftelse på bookingen. Applikasjonen er bygget opp med flask som backend og henter bookingdata fra en mariadb database.

## Teknologier brukt
- HTML
- CSS
- Python
- Flask
- MariaDB

## Funksjonalitet
- Velg dato og tid
- Fyll inn navn, telefon og e-post
- Bekreftelsesside med oppsummering
- FAQ-side
- Sletting av info ved bruk av e-post

## Systemflyt
Bruker → Frontend (HTML/CSS) → Backend (Flask) → Database (MariaDB) → Bekreftelse til bruker

## Sikkerhet
- lage hemmelig nøkkel???
- Parameterisert SQL for å beskytte mot SQL injection
- GDPR infomeres om på FAQ siden: brukeren informeres om hva dataene brukes til, data deles ikke med tredjeparter

## Videre utvikling
- E-postbekreftelse til kunde
- Avbestilling og endring av booking
- lage en forside før bookingsiden, ha dermed FAQ og admin innlogging der.

## Hva jeg har tenkt å gjøre på eksamen
- Vise frem prosjektet mitt: Åpne nettsiden i nettleser fra en annen maskin på nettverket
- Clone prosjektet ned på raspberry Pi
- installere nødvendige pakker i en requirements.txt. 

## Kildeliste:
https://www.geeksforgeeks.org/python/template-inheritance-in-flask/ - Kilde for {% extends "index.html" %} brukt på html sidene

