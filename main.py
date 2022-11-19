from flask import Flask, render_template, request

import ActivityGenerator
import Content
import DBUtil

app = Flask(__name__)
criteriaModel = Content.Content()
dbUtil = DBUtil.DBUtil()
ag = ActivityGenerator.ActivityGenerator(dbUtil)

longName = 4
link = 5
description = 6
date = 7


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/test", methods=['POST'])
def submit_criteria():
    if request.method == "POST":
        question = request.form.get("question")
        criteria = request.form.get("criteria")
        criteriaModel.add_criteria(question, criteria)
    return ('', 204)


@app.route("/activity", methods=["POST", "GET"])
def activity():
    event = None
    activityName = "Oops! All out of recommendations!"
    website = None
    descrip = None
    eventDate = None

    if request.method == "POST":
        ag.generate_activity(criteriaModel)
        activities = ag.activities
        print(activities)
        event = activities[0]
    else:
        activities = ag.activities
        if activities:
            activities.pop(0)
        if activities:
            event = activities[0]
    if event:
        activityName = event[longName]
        website = event[link]
        descrip = event[description]
        eventDate = event[date]
    if event:
        render_template('activity.html', activityName=activityName)
    return render_template('activity.html',
                           activityName=activityName,
                           website=website,
                           description=descrip,
                           date=eventDate)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run("127.0.0.1", 8080, True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
