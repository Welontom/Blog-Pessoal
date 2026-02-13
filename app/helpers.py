import markdown

def convert_to_html(input):
    with open(input, "r", encoding="utf-8") as f:
        markdown_content = f.read()
    return markdown.markdown(markdown_content, extensions=["mdx_math"], extension_configs={'mdx_math': {'enable_dollar_delimiter': True}})
