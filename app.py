from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension 
from stories import Story

app = Flask(__name__)
app.config['SECRET_KEY'] = "madlibs"
debug = DebugToolbarExtension(app)

@app.route('/')
def show_form():
    return render_template('home.html')

@app.route('/story')
def show_story():
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]
    answers = {
        "place": place,
        "noun": noun,
        "verb": verb,
        "adjective": adjective,
        "plural_noun": plural_noun
    }
    story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    )
    result = story.generate(answers)
    return render_template('story.html', result=result)