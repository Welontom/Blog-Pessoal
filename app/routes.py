from app import app
from app.helpers import convert_to_html, show_posts
from flask import render_template

@app.route('/')
def index():
    print(show_posts())
    posts_list = show_posts()
    return render_template('home.html', posts_list=posts_list)

@app.route('/posts/<name>')
def posts(name):
    file_name = (name + '.md')
    post = convert_to_html(f'app/posts/{file_name}')
    return render_template('post.html',post=post)