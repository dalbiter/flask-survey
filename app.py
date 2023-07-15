from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret-key"
debug = DebugToolbarExtension
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
