from flask import Flask, render_template

app = Flask(__name__)

'''
Routes
'''


@app.route("/")
def stats():
    return render_template("stats.html")


@app.route("/stories")
def stories():
    return render_template("stories.html")


@app.route("/media")
def media():
    return render_template("media.html")

if __name__ == "__main__":
    app.run(debug=True)