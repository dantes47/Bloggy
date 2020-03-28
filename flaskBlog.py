
from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return '<h1 style="text-align: center;">Nice try!!!<a href="/about" style="color: teal; margin: 0 auto; padding: 30% 30%;"> About</a></h1>'

@app.route("/about")
def about():
    return '<h2 style="text-align: center;">About Me<a href="/" style="color: red; margin: 0 auto; padding: 30% 30%;"> Home page</a></h2>'

if __name__ == '__main__':
    app.run(debug=True)
