import requests

from flask import redirect, render_template, session
from functools import wraps
from apisecrets import HeiGIT_APIKEY


def apology(message: str, code=400):

    def escape(s):
        for old, new in [
            ("-", "--"),
            (" ", " "),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def distance(start: str, destination: str):

    url = "https://api.openrouteservice.org/geocode/search"
    APIKEY = HeiGIT_APIKEY

    try:
        beginning = requests.get(
            url, params={"api_key": APIKEY, "text": start, "size": 1}
        )
        beginning.raise_for_status()
        beginning = beginning.json()

        arrival = requests.get(
            url, params={"api_key": APIKEY, "text": destination, "size": 1}
        )
        arrival.raise_for_status()
        arrival = arrival.json()

    except requests.RequestException:
        raise ValueError("Location service unavailable!")

    if not beginning.get("features"):
        raise ValueError(f"Unknown start city: {start}")

    if not arrival.get("features"):
        raise ValueError(f"Unknown destination city: {destination}")

    try:
        begcoords = beginning["features"][0]["geometry"]["coordinates"]
        arrcoords = arrival["features"][0]["geometry"]["coordinates"]

    except (KeyError, IndexError):
        raise ValueError("Invalid location data returned!")

    try:
        route = requests.post(
            "https://api.openrouteservice.org/v2/directions/driving-car",
            headers={"Authorization": APIKEY, "Content-Type": "application/json"},
            json={"coordinates": [begcoords, arrcoords]},
        )

        route.raise_for_status()
        route = route.json()

    except requests.RequestException:
        raise ValueError("Route calculation failed")

    if not route.get("routes"):
        raise ValueError(f"No route found between {start} and {destination}")

    dist_km = float(route["routes"][0]["summary"]["distance"] / 1000)

    return round(float(dist_km), 2)


def emissions(kilometer: float):
    """Format value as CO2 in kg"""
    carbondioxide = kilometer * 0.139

    return round(float(carbondioxide), 2)


def experience(kilometer: float):
    """Format value as fictive XP"""
    experiencepoints = kilometer * 100

    return int(experiencepoints)
