from flask import Flask, render_template
import dogtweets

app = Flask (__name__)

@app.route('/')
def index():
    return str(dog)

if __name__ == "__main__":
    app.run(debug=True, port=4320, use_reloader=False)
