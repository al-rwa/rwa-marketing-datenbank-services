# Setup

## Repository Clonen:
  Im Reposetory sind folgende Daten enthalten
  Django Projekt(skilltest) mit 2 apps (stammdaten, cdr)
  - stammdaten 
    - Models in Stammdaten:
      - Mandant
      - Herkunft
      - Kommunikationsart
      - Dsgvo

  - cdr
    - Models in cdr:
      - Kunde
      - Kommunikation

  Datenbank:
  Die sqlite3 Datenbank und liegt im root Ordner skilltest
  Zum öffnen der Datenbank kann DB Browser for SQLite verwendet werden.
  [DB Browser for SQLite](https://sqlitebrowser.org/)


## Python Envirenment erstellen:
  ### Python installieren:
  Es muss Python mit Version >=3.8 installiert sein.
  [Python download](https://www.python.org/downloads/)

  ### Virtual Environment erstellen (optional):
  Um die Packages nicht mit der Hauptinstanz von Python zu vermischen kann ein Virtual Environment erstellt und aktiviert werden.
  [Virtualenvirenment](https://realpython.com/python-virtual-environments-a-primer/#create-it)

  ### Packages installieren:
  Im root (skilltest) Ordner liegt die Datei requirements.txt mit allen erforderlichen Packages.
  Um die Packages zu installieren muss über die Command Line in den Ordner navigiert werden und dann folgender Befehl ausgeführt werden.
  ```
  pip install -r requirements.txt
  ```
  
  Alternativ können die Packages auch einzeln installiert werden mit folgenden Befehlen.
  ```
  pip install django==4.0.8
  ```
  ```
  pip install pyodbc==4.0.34
  ```

## Django Server starten:
  Um den Django Server zu starten navigieren Sie in der Command Line in den Ordner skilltest in dem die Datei manage.py vorhanden ist.
  Folgender Befehl startet den Server und macht ihn über die Adresse [http://127.0.0.1:8000](http://127.0.0.1:8000) verfügbar.
  ```
  py manage.py runserver 127.0.0.1:8000
  ```

  Unter [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) kommen Sie in das Admin Portal des Django Projekts.

  - Django Superuser Login:
    - username: admin
    - password: password123



# Aufgaben

1) Erstellen Sie eine Datenbank-View mit namen vAufgabe1 für alle Kunden (kuKunden) die kontaktiert werden dürfen.
  Folgende Kriterien sind zu berücksichtigen.
   - nur aktive Mandanten (sdMandant.aktiv = 1)
   - nur aktive Herkünfte (sdHerkunft.aktiv = 1)
   - nur dsgvo newsletter upload 1 (sdDsgvo.newsletter_upload = 1)
   - jede Email Adresse sollte nur ein mal vorkommen

2) Schreiben Sie ein oder mehrere SQL Queries um Email und Telefonnummer von Kunden zu Kommunikation zu kopieren und führen Sie diese aus.
   Wir haben ein neues Model Kommunikation erstellt um mehrere Email Adressen und Telefonnummern zu einem Kunden speichern zu können ohne die Spalten von kuKunden erweitern zu müssen. Jetzt möchten wir die Daten aus den aktuellen Kundenprofilen (kuKunden) in die neue Tabelle (kuKommunikation) kopieren. 
   - Spalten die kopiert werden sollen:
     - kuKunden.email
     - kuKunden.telefon
     - kuKunden.telefon_mobil
   - Kunde hat telefon und telefon_mobil, Kommunikationsarten hat nur telefon. Was machen wir?


3) Fügen Sie eine KommunikationInline zu KundenAdmin hinzufügen

   [Django InlineAdmin](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#inlinemodeladmin-objects)
   - Erstellen Sie eine TabularInline namens KommunikationInline in admin.py und fügen Sie diese als Inline zum KundenAdmin hinzu.
     - Die Felder kommunikationswert und kommunikationsart sollen in der Inline angezeigt werden
     - es soll keine extra leere Zeile in der Inline angezeigt werden



4) Bugfix
   Über den Kunden Admin haben die User die Möglichkeit mit einer Admin Action mehrere Kunden gleichzeitig vom Newsletter abzumelden. Leider funktioniert die Action "Kunden auf 02 abgelehnt setzen" nicht richtig und setzt den status akzeptiert anstatt abgelehnt.

   [Django Admin Actions](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/actions/)
   
   4.1) Kontrollieren Sie die Funktion set_dsgvo_02 in admin.py und finden Sie heraus warum diese den falschen Status setzt.
   
   4.2) Korrigieren Sie die Funktion.

