from flask import Flask, render_template, request, session

import ActivityGenerator
import Content
import DBUtil
import uuid


app = Flask(__name__)
app.secret_key = "secretKey"
dbUtil = DBUtil.DBUtil()
ag = ActivityGenerator.ActivityGenerator(dbUtil)

longName = 4
link = 5
description = 6
date = 7


@app.route("/")
def index():
    session["sessionId"] = uuid.uuid4()
    return render_template('index.html')


@app.route("/test", methods=['POST'])
def submit_criteria():
    if request.method == "POST":
        question = request.form.get("question")
        criteria = request.form.get("criteria")
        criteriaModel = Content.Content()
        if "criteriaModel" in session:
            criteriaModel = Content.Content(session["criteriaModel"])
        criteriaModel.add_criteria(question, criteria)

        session["criteriaModel"] = criteriaModel.answers

    return '', 204


@app.route("/activity", methods=["POST", "GET"])
def activity():
    event = None
    activityName = "Oops! All out of recommendations!"
    website = ""
    descrip = ""
    eventDate = ""
    eventLink = ""

    if request.method == "POST":
        criteriaModel = Content.Content()
        if "criteriaModel" in session:
            criteriaModel = Content.Content(session["criteriaModel"])
        if "sessionId" in session:
            session["activities"] = ag.generate_activity(criteriaModel)
            event = session["activities"][0]
    else:
        if "sessionId" in session:
            activities = session["activities"]
            if activities:
                activities.pop(0)
                session["activities"] = activities
            if activities:
                event = activities[0]
    if event:
        activityName = event[longName]
        website = event[link]
        descrip = event[description]
        eventDate = event[date]
        eventLink = "Event Link"
    return render_template('activity.html',
                           activityName=activityName,
                           website=website,
                           description=descrip,
                           date=eventDate,
                           link=eventLink)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run("127.0.0.1", 8080, True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
