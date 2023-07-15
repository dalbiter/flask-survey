from flask import Flask, render_template, request, redirect, flash
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

@app.route('/start', methods=["POST"])
def begin_survey():

    return redirect('/questions/0')

@app.route('/questions/<int:qid>')
def show_question(qid):

    question = satisfaction_survey.questions[qid]
    choices =   question.choices

    return render_template('question.html', question=question, question_num=qid, choices=choices)