from flask import Flask, render_template

app = Flask(__name__)

'''
Routes
'''


@app.route("/")
def stats():
    return render_template("stats.html")


@app.route("/pinkbot")
def pinkbot():
    return render_template("pinkbot.html")


@app.route("/organizations")
def organizations():
    return render_template("organizations.html")


@app.route("/stories")
def stories():
    return render_template("stories.html")


@app.route("/media")
def media():
    return render_template("media.html")


if __name__ == "__main__":
    app.run(debug=True)