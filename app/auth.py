from flask import Blueprint, request, render_template, flash, redirect, url_for
from app.constants import *
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in succesfully!", category = "success")
                login_user(user, remember=True) 
                return redirect(url_for('routes.home'))
            else:
                flash("Incorrect password", category="Failure")
        else:
            flash("Email not registered, register!", category="Warning")

    return render_template("login.html", title=appName, user=current_user)

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        pass_confirmation = request.form.get('password-conf')

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already registered.", category="Warning")
        elif len(name) < 5:
            flash("That doesn't looks like a name", category="Failure")
        elif password != pass_confirmation:
            flash("Passwords don't match", category="Failure")
        else:
            new_user = User(email=email, name=name, password=generate_password_hash(password, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True) 
            flash("Account created", category="Success")
            return redirect(url_for('routes.home'))


    return render_template("signup.html", title=appName, user=current_user)

@auth.route("logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
