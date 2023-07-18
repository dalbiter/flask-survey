from flask import Flask, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret-key"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

RESPONSES = []

@app.route('/')
def show_survey():
    """Shows the title and instruction and allows the user to begin the survey"""

    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions

    return render_template('home.html', title=title, instructions=instructions)

@app.route('/start', methods=["POST"])
def begin_survey():
    """takes user to first question once they start the survey"""

    return redirect('/questions/0')

@app.route('/questions/<int:qid>')
def show_question(qid):
    """Show the current question the user is on"""
    
    #if the user tries to go to a question out of order
    if len(RESPONSES) != qid:
        flash(f'Question ID {qid} is invalid!')
        return redirect(f'/questions/{len(RESPONSES)}')
    
    #if a user has answered all of the questions
    if len(RESPONSES) == len(satisfaction_survey.questions):
        return redirect('/complete')
    
    question = satisfaction_survey.questions[qid]
    choices = question.choices
    
    return render_template('/question.html', question=question, question_num=qid, choices=choices)

@app.route('/answer', methods=['POST'])
def handle_question():
    """takes the answer from the survey question and appends it to RESPONSES then shows the next question"""

    choice = request.form.get('answer')
    
    RESPONSES.append(choice)

    #if a user has completed the survey
    if len(RESPONSES) == len(satisfaction_survey.questions):
        return redirect('/complete')
    #takew the user to the next question in the survey
    else:
        return redirect(f'/questions/{len(RESPONSES)}')
    
@app.route('/complete')
def show_complete_page():
    """Shows the completed survey page"""

    return render_template('/complete.html', responses=RESPONSES)