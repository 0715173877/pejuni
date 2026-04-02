import os
import re

html_path = "index4.html"
css_path = "style4.css"
target_html_dir = "../pejuni.com /templates"
target_html = f"{target_html_dir}/index.html"

os.makedirs(target_html_dir, exist_ok=True)

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Inject Django tag at the top
html = "{% load static %}\n" + html

# Regex replacements for images and CSS
html = re.sub(r'href="(style4\.css)"', 'href="{% static \'\\1\' %}"', html)
html = re.sub(r'src="([^"]+\.(png|jpg))"', 'src="{% static \'\\1\' %}"', html)
html = re.sub(r"url\('([^']+)\.(png|jpg)'\)", "url('{% static '\\1.\\2' %}')", html)

with open(target_html, "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully compiled Django Base Template into templates/index.html!")
