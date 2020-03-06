from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def accessIntro():
    return render_template("MyPage.html")


@app.route('/profile')
def accessProfile():
    return render_template("profile.html")


@app.route('/interest')
def accessInterest():
    return render_template("interest.html")


@app.route('/skills')
def accessSkills():
    return render_template("skills.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="3572")
