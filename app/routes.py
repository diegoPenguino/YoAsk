from flask import render_template, flash, redirect, Blueprint, request, jsonify
from flask_login import login_required, current_user
from .models import Survey, Option, Votes
from . import db
import json

routes = Blueprint("routes", __name__)
from app.constants import *

def add_survey() -> bool:
    question = request.form.get("question")
    if len(question) < 1:
        flash("Bruh, cmon", category="Warning")
    else:
        new_question = Survey(question=question, user_id=current_user.id)
        options = []
        
        text_form = request.form.get("first-op")
        if text_form:
            options.append(Option(text=text_form, votes=0))

        text_form = request.form.get("second-op")
        if text_form:
            options.append(Option(text=text_form, votes=0))

        text_form = request.form.get("third-op")
        if text_form:
            options.append(Option(text=text_form, votes=0))
              
        text_form = request.form.get("fourth-op")
        if text_form:
            options.append(Option(text=text_form, votes=0))
               
        if options:
            for option in options:
                new_question.options.append(option)
            db.session.add(new_question)
            db.session.commit()
        else:
            flash("You didn't add no option to choose from", category="Warning")

@routes.route("/home", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        if "add-survey" in request.form:
            add_survey()
        else:
            data = list(request.form.keys())[0].split()
            optionId = int(data[0])
            surveyId = int(data[1])
            option = Option.query.get(optionId)
            survey = Survey.query.get(surveyId)
            if option and survey:
                if option.id == optionId and survey.id == surveyId:
                    vote_registered = Votes.query.filter_by(survey_id=surveyId, user_id=current_user.id).first()
                    if vote_registered is None:
                        vote_registered = Votes(survey_id=surveyId, user_id=current_user.id)
                        db.session.add(vote_registered)
                        option.votes += 1
                        db.session.commit()
                        flash("Vote registered!", category="Success")
                    else:
                        flash("You've already voted! " + str(vote_registered), category="Warning")

    return render_template("home.html", title=f"{appName}", user=current_user, surveys=Survey.query.filter_by())


@routes.route("/")
@routes.route("/index")
def index():
    return render_template("index.html", title=appName, user=current_user)

@routes.route('/delete-survey', methods=["POST"])
def delete_survey():
    survey = json.loads(request.data)
    surveyId = survey['surveyId']
    survey = Survey.query.get(surveyId)
    if survey:
        if survey.user_id == current_user.id:
            db.session.delete(survey)
            db.session.commit()
            return jsonify({})