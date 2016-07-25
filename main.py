from flask import Flask, render_template
import dogtweets
import cattweets

app = Flask (__name__)

@app.route('/')
def index():
    return render_template("index.html", dog=str(dogtweets.dog))

def index():
    return render_template("index.html", cat=str(cattweets.cat))

if __name__ == "__main__":
    app.run(debug=True, port=4000, use_reloader=False)
