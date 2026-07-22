## GREEN TRIP CHALLENGE

### Abstract und Zusammenfassung:

Nachhaltigkeit ist ein wichtiges Thema, wird aber oft wenig sichtbar gemacht – außer durch Imagemaßnahmen. Den Bahnkund:innen fehlt manchmal der Bezug und das Verhältnis dazu, wie viele Emissionen tatsächlich eingespart werden, vor allem beim Nutzen von Bahnprodukten. Durch die Website „Green Trip Challenge“ werden Emissionseinsparungen sichtbar für Bahnkund:innen, durch gamifiziertes Erleben beim Nutzen von Bahnprodukten. Die Website „Green Trip Challenge“ macht nachhaltiges Verhalten sichtbar und erlebbar durch Sharingfunktionen in den sozialen Medien – vor allem aber auch das Leaderboard (und speziell das Klettern auf der Rangliste dort), werden Anreize zum nachhaltigen Reisen geschaffen, aber auch Badges und Awards als Belohnungen warten auf, sowie die Möglichkeit XP zu sammeln. Auf Seiten des Backends wird die Anwendung durch das Python-Framework Flask und SQLite und die RIS-API betrieben, auf Seiten des Frontends wird die Darstellung mit HTML, CSS und JavaScript oder alternativ Jinja realisiert.

### Setup der Flask Web Application:


1. Schritt - Wechsle in den Ordner "challenge" mit cd:
```bash
cd challenge
```

2. Schritt - Installiere lokal die "requirements.txt" mit pip install:
```bash
python3 -m pip install -r requirements.txt
```

3. Schritt - Setze die Umgebungsvariable "venv" auf mit:
```bash
python3 -m venv venv
source venv/bin/activate
```

4. Schritt - Starte die Webapplikation lokal mit "flask run":
```bash
flask run
```

5. Schritt - Öffne die angezeigte URL mit der IP-Adresse / Port in Deinem Browser:
```bash
http://127.0.0.1:5000/
```
