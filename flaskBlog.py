
from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Danny Creator',
        'title': 'Blog, 1_st. Post',
        'content': '1_st. Post Content',
        'date': 'May 9, 2020'
    },
    {
        'author': 'Djanki Bastard',
        'title': 'Blog, 2_st. Post',
        'content': '2_st. Post Content',
        'date': 'DoomDay 13, 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)
@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
