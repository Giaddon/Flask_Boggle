from flask import Flask, render_template, session, request
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

    session["board"] = board
    # print("\n\Session Board", session["board"], "\n\n")

    return render_template("board.html", board = board)

@app.route("/check/",methods=["POST"])
def check_guess():
    print("\n \nThis is our json \n \n",request.json)

    guess = request.json.get("guess","something")
    result_of_valid_word_check = boggle_game.check_valid_word( session["board"], guess)
    if result_of_valid_word_check == "not-on-board":
        return "Word isn't on the board!"
    elif result_of_valid_word_check == "ok":
        return "Cool! Good job Guy"
    else:
        return "This isn't a word"

  
