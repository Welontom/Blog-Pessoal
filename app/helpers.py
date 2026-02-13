import markdown
import os
from flask import url_for

def convert_to_html(input):
    with open(input, "r", encoding="utf-8") as f:
        markdown_content = f.read()
    return markdown.markdown(markdown_content, extensions=["mdx_math"], extension_configs={'mdx_math': {'enable_dollar_delimiter': True}})

def show_posts():
    html_content = ''
    for f in os.listdir('app/posts/'):
        file_name = os.path.splitext(f)[0]
        html_content += ('<a href=' + url_for('posts', name=file_name) + '>'
                         +'<div class=\"card mb-4 shadow-sm post-card\">'
                         +'<h5 class=\"card-title\">'+ file_name +'</h5>'
                         + '</div>'
                         + '</a>') 
    return html_content