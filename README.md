## GREEN TRIP CHALLENGE

### Abstract und Zusammenfassung:

Nachhaltigkeit ist ein wichtiges Thema, wird aber oft wenig sichtbar gemacht – außer durch Imagemaßnahmen. Den Bahnkund:innen fehlt manchmal der Bezug und das Verhältnis dazu, wie viele Emissionen tatsächlich eingespart werden, vor allem beim Nutzen von Bahnprodukten. Durch die Website „Green Trip Challenge“ werden Emissionseinsparungen sichtbar für Bahnkund:innen, durch gamifiziertes Erleben beim Nutzen von Bahnprodukten. Die Website „Green Trip Challenge“ macht nachhaltiges Verhalten sichtbar und erlebbar durch Sharingfunktionen in den sozialen Medien – vor allem aber auch das Leaderboard (und speziell das Klettern auf der Rangliste dort), werden Anreize zum nachhaltigen Reisen geschaffen, aber auch Badges und Awards als Belohnungen warten auf, sowie die Möglichkeit XP zu sammeln. Auf Seiten des Backends wird die Anwendung durch das Python-Framework Flask und SQLite und die HeiGIT API betrieben, auf Seiten des Frontends wird die Darstellung mit HTML, CSS und der JS-Alternative Jinja realisiert. Es handelt sich bei diesem Projekt um ein fiktives / theoretisches Studienprojekt im Rahmen eines Praxistransfers meines dualen Studiums.

### Setup der Flask Web Application auf Windows:
<details>
<summary>Hier eine Schritt-für-Schritt-Anleitung für Windows, die für das Setup auszuführen ist.</summary>

0. Schritt - Erstellung eines kostenlosen API-Schlüssels bei HeiGIT:
```bash
0.1 Besuche die Webseite https://api.heigit.org/ und erstelle einen Account.
0.2 Kopiere den persönlichen, kostenlosen API-Schlüssel von der Webseite.
0.3 Ersetze den API-Schlüssel der Variable HeiGIT_APIKEY der Datei "apisecrets.py".
```

Ab hier sind die Befehle im Terminal auszuführen:

1. Schritt - Wechsel in den Ordner "challenge" mit cd:
```bash
cd challenge
```

2. Schritt - Aufsetzen der Umgebungsvariable "venv" mit:
```bash
py -m venv venv
venv\Scripts\activate
set FLASK_APP=app.py  
```

3. Schritt - Lokale Installation der "requirements.txt" mit pip install:
```bash
python.exe -m pip install --upgrade pip   
py -m pip install -r requirements.txt
```

4. Schritt - Lokaler Start der Webapplikation mit "flask run":
```bash
flask run
```

5. Schritt - Öffnen der angezeigten URL mit der IP-Adresse und dem Port im Browser:
```bash
http://127.0.0.1:5000/
```
</details>

### Setup der Flask Web Application auf macOS:
<details>
<summary>Hier eine Schritt-für-Schritt-Anleitung für macOS, die für das Setup auszuführen ist.</summary>

0. Schritt - Erstellung eines kostenlosen API-Schlüssels bei HeiGIT:
```bash
0.1 Besuche die Webseite https://api.heigit.org/ und erstelle einen Account.
0.2 Kopiere den persönlichen, kostenlosen API-Schlüssel von der Webseite.
0.3 Ersetze den API-Schlüssel der Variable HeiGIT_APIKEY der Datei "apisecrets.py".
```

Ab hier sind die Befehle im Terminal auszuführen:

1. Schritt - Wechsel in den Ordner "challenge" mit cd:
```bash
cd challenge
```

2. Schritt - Lokale Installation der "requirements.txt" mit pip install:
```bash
python3 -m pip install -r requirements.txt
```

3. Schritt - Aufsetzen der Umgebungsvariable "venv" mit:
```bash
python3 -m venv venv
source venv/bin/activate
```

4. Schritt - Lokaler Start der Webapplikation mit "flask run":
```bash
flask run
```

5. Schritt - Öffnen der angezeigten URL mit der IP-Adresse und dem Port im Browser:
```bash
http://127.0.0.1:5000/
```
</details>

### Die Inspiration für dieses Projekt:

Dieses Projekt basiert **stark abgewandelt** auf der Aufgabe "Finance" der Kursreihe CS50 (Harvard University).

### Die Architektur hinter der Software:

<span>
  <img alt="Diagram of the Software Architecture behind this Project" src="https://raw.githubusercontent.com/Cranjah/Challenge-Green-Trip/d8e10ae722466058988a6c482f70c59d0a86ae54/images/diagram.svg">
</span>
