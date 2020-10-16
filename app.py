from flask import Flask, render_template, request
import media

app = Flask(__name__)

"""
Objets
"""


movies = {
    'movie1': media.movie1,
    'movie2': media.movie2,
    'movie3': media.movie3,
    'movie4': media.movie4,
    'movie5': media.movie5
}


"""
Utility functions
"""


def get_response(userText):
    return userText


'''
Routes
'''


@app.route("/")
def stats():
    return render_template("stats.html")


conversation = ['', '']


@app.route("/pinkbot")
def pinkbot():
    return render_template("pinkbot.html", conversation=conversation)


@app.route("/pinkbot/get")
def get_bot_response():
    userText = request.args.get('msg')
    botText = str(get_response(userText))
    conversation.append(userText)
    conversation.append(botText)
    return render_template("pinkbot.html", conversation=conversation)


@app.route("/organizations")
def organizations():
    return render_template("organizations.html")


@app.route("/stories")
def stories():
    return render_template("stories.html")


@app.route("/media")
def media():
    return render_template("media.html", movies=movies)


if __name__ == "__main__":
    app.run(debug=True)
