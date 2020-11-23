# Zulassungssystem Informatik Studiengangs

## tl;dr <br>
Eine Demo mit vorgefüllter Datenbank kann unter folgender Adresse aufgerufen werden. 

Link: https://www.swt-das.team/

Der User Guide kann [hier](/doc/User%20_Guide_Semantic_Mango.pdf) aufgerufen werden.

- Beipiel Account Zulassungsausschuss Admin:<br>
Kann Zulassungsausschuss-Mitglied Accounts erstellen und löschen (Hat als einziges Mitglied des Zulassungsausschusses Zugriff auf Django-Admin) und Annahmen und Ablehnungen rückgängig machen<br>
Benutzername: zulassung@admin-user.de<br>
Passwort: das-team

- Beipiel Account Zulassungsausschuss Mitglied:<br>
Kann lediglich Bewerbungen ansehen und diese ablehnen oder annehmen<br>
Benutzername: zulassung@normal-user.de<br>
Passwort: das-team

- Beipiel Account Bewerber:<br>
Kann verschiedene Informationen für seine Bewerbungen angeben, Bewerbungen abschicken, bearbeiten und zurück nehmen<br>
  Benutzername: peter@zwegert-mail123.de <br>
  Passwort: das-team
  
- Darüberhinaus kann auch ein eigener Bewerberaccount durch Registrierung auf der Seite erstellt werden.

## Wie kann man das Zulassungssystem installieren?
- Installieren Sie Python(=> 3.6) und eine Python IDE auf Ihrem PC bspw. Pycharm.
- Klonen Sie dieses Github Repository (https://github.com/LHumpe/InfoZulassung).
```sh
$ git clone https://github.com/LHumpe/InfoZulassung.git
```
- Gehen Sie in den Ordner InfoZulassung mit dem folgenden Befehl.
```sh
$ cd InfoZulassung 
```
- Geben Sie in Ihrem Terminal den unteren Befehl ein sodass die Dependencies installiert werden.
```sh
$ pip install -r requirements.txt
```
- Geben Sie im Terminal den unteren Befehl ein um den Server zu starten.
```sh
$ python manage.py runserver 8000
```
- Wenn der Server ohne Fehlermeldung gestartet ist, können Sie die Seite unter den folgenden Adresse aufrufen: http://127.0.0.1:8000/
