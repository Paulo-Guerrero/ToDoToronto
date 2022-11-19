from flask import Flask, render_template, request
import Content
import DBUtil

app = Flask(__name__)
criteriaModel = Content.Content()
dbUtil = DBUtil.DBUtil()

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/test", methods=['POST'])
def submit_criteria():
    if request.method == "POST":
        question = request.form.get("question")
        criteria = request.form.get("criteria")
        criteriaModel.add_criteria(question, criteria)
    return ('',204)


@app.route("/activity", methods=["POST", "GET"])
def activity():
    if request.method == "POST":
        activity = generate_activity(criteriaModel.criteria1,
                                     criteriaModel.criteria2,
                                     criteriaModel.criteria3)
    else:
        activity = generate_activity(None, None, None)

    activityName = activity.get("activityName")
    website = activity.get("website")

    return render_template('activity.html', activityName=activityName,
                           website=website)


def generate_activity(criteria1, criteria2, criteria3):
    # TODO implement
    activityInfo = {"activityName": criteria1, "website": criteria2}
    return activityInfo


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run("127.0.0.1", 8080, True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
