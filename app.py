from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "Shhhhh"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route("/")
def home():
    
    board = boggle_game.make_board() #this needs to go into a session

    print("\n\nBoard", board, "\n\n")

    return render_template("board.html", board = board)