from app import app
from app.helpers import convert_to_html
from flask import render_template

@app.route('/')
def index():
    post = convert_to_html("app/posts/exemplo.md")
    print(post)
    return render_template('home.html', post=post)