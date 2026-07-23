from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash


from helperfunctions import (
    apology,
    login_required,
    distance,
    emissions,
    experience,
)

# Configure application
app = Flask(__name__)

# Custom filters
app.jinja_env.filters["emissions"] = emissions
app.jinja_env.filters["experience"] = experience

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure library to use sqlite database
db = SQL("sqlite:///challenge.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of trips"""

    trips = db.execute(
        """
        SELECT
            Start AS start,
            Destination AS destination,
            KM AS km,
            CO2 AS co2,
            XP AS xp
        FROM challenges
        WHERE user_id = ?
        ORDER BY id DESC
    """,
        session["user_id"],
    )

    return render_template("index.html", trips=trips)


@app.route("/index")
@login_required
def tripportfolio():
    """Show portfolio of trips"""

    trips = db.execute(
        """
        SELECT
            Start AS start,
            Destination AS destination,
            KM AS km,
            CO2 AS co2,
            XP AS xp
        FROM challenges
        WHERE user_id = ?
        ORDER BY id DESC
    """,
        session["user_id"],
    )

    return render_template("index.html", trips=trips)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log an user in"""

    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            return apology("You must provide username!", 403)

        elif not request.form.get("password"):
            return apology("You must provide password!", 403)

        rows = db.execute(
            """SELECT * FROM users WHERE username = ?""", request.form.get("username")
        )

        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("Invalid username or password!", 403)

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log an user out"""

    session.clear()

    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register a new user"""

    session.clear()

    user = request.form.get("username")
    hash = request.form.get("password")
    conf = request.form.get("confirmation")

    existing = db.execute("""SELECT id FROM users WHERE username = ?""", user)

    if request.method == "POST":
        if not user:
            return apology("You need to provide a username!", 403)

        if not hash:
            return apology("You need to provide a password!", 403)

        if not conf:
            return apology("You need to provide a confirmation!", 403)

        if existing:
            return apology("Username already taken by somebody else!", 403)

        if hash == conf and not existing:
            db.execute(
                """INSERT INTO users (username, hash) VALUES(?, ?)""",
                user,
                generate_password_hash(hash),
            )

        elif hash != conf:
            return apology("The password and confirmation need to match!", 403)

        return redirect("/")

    elif request.method == "GET":
        return render_template("register.html")

    else:
        return apology("You need to provide the credentials!", 403)


@app.route("/awards")
@login_required
def awards():
    """Showcase all earned awards"""

    user = db.execute(
        """
        SELECT best_rank
        FROM users
        WHERE id = ?
    """,
        session["user_id"],
    )

    if not user:
        return apology("Specific user not found!", 404)

    best_rank = user[0]["best_rank"]

    return render_template("awards.html", best_rank=best_rank)


@app.route("/badges")
@login_required
def badges():
    """Show all earned badges"""

    user_id = session["user_id"]

    hero = db.execute(
        """
        SELECT
            SUM(CASE WHEN KM >= 50 THEN 1 ELSE 0 END) AS trips50,
            SUM(CASE WHEN KM >= 200 THEN 1 ELSE 0 END) AS trips200
        FROM challenges
        WHERE user_id = ?
    """,
        user_id,
    )

    user = db.execute(
        """
        SELECT
            KM,
            CO2
        FROM users
        WHERE id = ?
    """,
        user_id,
    )

    trips50 = hero[0]["trips50"] or 0
    trips200 = hero[0]["trips200"] or 0

    total_km = user[0]["KM"] or 0
    total_co2 = user[0]["CO2"] or 0

    return render_template(
        "badges.html",
        trips50=trips50,
        trips200=trips200,
        total_km=total_km,
        total_co2=total_co2,
    )


@app.route("/leaderboard", methods=["GET", "POST"])
@login_required
def leaderboard():
    """Showcase the leaderboard"""

    users = db.execute(
        """
        SELECT
            id,
            ROW_NUMBER() OVER (ORDER BY KM DESC) AS rank,
            username,
            KM AS km,
            CO2 AS co2,
            XP AS xp
        FROM users
        ORDER BY KM DESC
    """
    )

    for rank, user in enumerate(users, start=1):

        if rank <= 3:
            db.execute(
                """
                UPDATE users
                SET best_rank =
                    CASE
                        WHEN best_rank IS NULL THEN ?
                        WHEN ? < best_rank THEN ?
                        ELSE best_rank
                    END
                WHERE id = ?
            """,
                rank,
                rank,
                rank,
                user["id"],
            )

    return render_template("leaderboard.html", users=users)


@app.route("/registertrips", methods=["GET", "POST"])
@login_required
def registertrips():

    start = request.form.get("start")
    destination = request.form.get("destination")

    if request.method == "POST":
        if not start:
            return apology("You must provide start city!", 400)

        if not destination:
            return apology("You must provide destination city!", 400)

        try:
            km = distance(start, destination)
        except (TypeError, ValueError):
            return apology("Distance calculation not possible!", 400)

        co2 = emissions(km)
        xp = experience(km)

        db.execute(
            """
            INSERT INTO challenges
            (user_id, Start, Destination, KM, CO2, XP)
            VALUES (?, ?, ?, ?, ?, ?)
        """,
            session["user_id"],
            start,
            destination,
            km,
            co2,
            xp,
        )

        db.execute(
            """
            UPDATE users
            SET
                XP = XP + ?,
                KM = KM + ?,
                CO2 = CO2 + ?
            WHERE id = ?
        """,
            xp,
            km,
            co2,
            session["user_id"],
        )

        return redirect("/index")

    return render_template("registertrips.html")
