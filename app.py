from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret-key"
debug = DebugToolbarExtension
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

RESPONSES = []

@app.route('/')
def show_survey():

    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions

    return render_template('home.html', title=title, instructions=instructions)
