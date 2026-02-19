import markdown
import os
from flask import url_for
from datetime import datetime

def convert_to_html(input):
    with open(input, "r", encoding="utf-8") as f:
        markdown_content = f.read()
    return markdown.markdown(markdown_content, extensions=["mdx_math","fenced_code"], extension_configs={'mdx_math': {'enable_dollar_delimiter': True}})

def show_posts():
    posts_dir = 'app/posts/'
    html_content = ''

    files = [
        f for f in os.listdir(posts_dir)
        if f.endswith('.md')
    ]

    files.sort(key=lambda f: os.path.getmtime(os.path.join(posts_dir, f)), reverse=True)

    for f in files:
        file_path = os.path.join(posts_dir, f)
        file_name = os.path.splitext(f)[0]

        timestamp = os.path.getmtime(file_path)
        date = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y')

        html_content += (
            '<a href="' + url_for('post', name=file_name) + '" '
            'class="text-decoration-none text-dark">'
                '<div class="card mb-4 shadow-sm post-card">'
                    '<div class="card-body">'
                        '<h5 class="card-title">' + file_name + '</h5>'
                        '<p class="card-text text-muted small mb-2">'
                            'Última modificação: ' + date +
                        '</p>'
                        '<p class="card-text text-muted small">'
                            'Clique para ler o post'
                        '</p>'
                    '</div>'
                '</div>'
            '</a>'
        )
    return html_content