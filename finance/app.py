import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
from datetime import datetime

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


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
    """Show portfolio of stocks"""
    cash = db.execute(f"SELECT cash FROM users WHERE id={session['user_id']}")[0]["cash"]
    stock = db.execute(f"SELECT name, symbol,SUM(shares) AS shares FROM stocks WHERE userid = {session['user_id']} GROUP BY name ")
    for j in range(len(stock)):
        nals2 = 0
        nalb2 = 0
        nals2 = db.execute(f"SELECT SUM(shares) FROM stocks WHERE userid = {session['user_id']} AND symbol = '{stock[j]['symbol']}' AND status = 'sell' ")[
            0]['SUM(shares)']
        if nals2 is None:
            nals2 = 0
        nalb2 = db.execute(f"SELECT SUM(shares) FROM stocks WHERE userid = {session['user_id']} AND symbol = '{stock[j]['symbol']}' AND status = 'buy' ")[
            0]['SUM(shares)']
        if nalb2 is None:
            nalb2 = 0
        nal2 = nalb2 - nals2
        stock[j]['shares'] = nal2

    balanse = cash
    for i in range(len(stock)):
        stock[i]['price'] = lookup(stock[i]['symbol'])['price']
        stock[i]['total'] = lookup(stock[i]['symbol'])['price'] * stock[i]['shares']
        stock[i]["us"] = usd(stock[i]['price'])

        balanse += stock[i]['total']
        stock[i]["ustot"] = usd(stock[i]['total'])

    return render_template("index.html", stock=stock, cash=usd(cash), balanse=usd(balanse))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        sym2 = lookup(request.form.get("symbol"))
        if not sym2:
            return apology("Symbol false")
        try:
            cnt = int(request.form.get("shares"))
        except:
            return apology("INT error")
        if cnt < 0:
            return apology("INT error")

        pr = round(sym2["price"] * cnt, 2)
        cash = db.execute(f"SELECT * FROM users WHERE id={session['user_id']}")[0]["cash"]
        cash = round(cash, 2)
        if cash < pr:
            return apology("Not money")

        else:
            # update balance
            db.execute(f"UPDATE users SET cash = cash - {pr} WHERE id={session['user_id']}")
            # print(db.execute(f"select * from users"))
            db.execute("INSERT INTO stocks (userid, symbol, name, shares, price, time, status, total) VALUES ( :userid, :symbol, :name, :shares, :price, :time, :status, :total)",
                       userid=session['user_id'],
                       symbol=sym2["symbol"],
                       name=sym2["name"],
                       shares=cnt,
                       price=sym2["price"],
                       time=str(datetime.now()),
                       status="buy",
                       total=pr)

            # CREATE TABLE IF NOT EXISTS stocks (
            #             userid varchar(45) NOT NULL,
            #             symbol varchar(45) NOT NULL,
            #             name varchar(45) NOT NULL,
            #             shares integer NOT NULL,
            #             price integer NOT NULL,
            #             total integer NOT NULL,
            #             time varchar(45),
            #             status varchar(45)
            #             );
            #             PRIMARY KEY (id) #  DROP table stoks;

            return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return render_template("history.html", stock=db.execute(f"SELECT * FROM stocks WHERE userid = {session['user_id']}"))


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        sym = lookup(request.form.get("symbol"))
        try:
            sym['price'] = round(sym['price'], 2)
        except:
            return apology("invalid symbol", 400)
        if not sym:
            return apology("invalid symbol", 400)
        else:
            return render_template("quoted.html", sim=sym, p=usd(sym['price']))

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        if not request.form.get("username") or not request.form.get("password") or not request.form.get("confirmation"):
            return apology("empty", 400)
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("confirmation is false", 400)
        else:
            try:
                name = request.form.get("username")
                hashpass = generate_password_hash(request.form.get("password"))
                db.execute("INSERT INTO users (username, hash, cash) VALUES(?, ?,?)", name, hashpass, 10000.00)
                return redirect("/")
            except:
                return apology("username is false", 400)

    # returne form
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        sym = request.form.get("symbol")
        shares = request.form.get("shares")
        pri = lookup(sym)

        if not sym:
            return apology("SYM ERROR ERROR")

        try:
            shares = int(shares)
        except:
            return apology("INT ERROR")
        if not shares > 0:
            return apology("INT ERROR")
        nals = db.execute(f"SELECT SUM(shares) FROM stocks WHERE userid = {session['user_id']} AND symbol = '{sym}' AND status = 'sell' ")[
            0]['SUM(shares)']
        if nals is None:
            nals = 0
        nalb = db.execute(f"SELECT SUM(shares) FROM stocks WHERE userid = {session['user_id']} AND symbol = '{sym}' AND status = 'buy' ")[
            0]['SUM(shares)']
        if nalb is None:
            nalb = 0
        nal = nalb - nals
        if shares > nal:
            return apology("NOT ERROR")
        tot = float(pri["price"]) * shares
        # table users
        db.execute(f"UPDATE users SET cash = cash + {tot} WHERE id={session['user_id']}")

        db.execute("INSERT INTO stocks (userid, symbol, name, shares, price, time, status, total) VALUES ( :userid, :symbol, :name, :shares, :price, :time, :status, :total)",
                   userid=session['user_id'],
                   symbol=pri["symbol"],
                   name=pri["name"],
                   shares=shares,
                   price=pri['price'],
                   time=str(datetime.now()),
                   status="sell",
                   total=tot)

        print(sym, shares, nal, nals, nalb)
        return redirect("/")
    else:
        sel = db.execute(f"SELECT DISTINCT symbol From stocks WHERE userid={session['user_id']} AND shares > 0")
        return render_template("sell.html", sel=sel)

