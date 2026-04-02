import os

base_dir = "../pejuni.com "
templates_dir = os.path.join(base_dir, "templates")

# First, dynamically refactor index.html into base.html!
index_path = os.path.join(templates_dir, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    original_html = f.read()

# Splitting sections
top_split = original_html.split("<!-- Parallax Hero -->")
header_chunk = top_split[0]
remainder = top_split[1]

bottom_split = remainder.split("<!-- Contact & Footer -->")
body_chunk = bottom_split[0]
footer_chunk = "<!-- Contact & Footer -->" + bottom_split[1]

# Inject Django Routing into Navigation (Global Header)
header_chunk = header_chunk.replace('href="#expertise"', 'href="{% url \'services:list\' %}"')
header_chunk = header_chunk.replace('href="#company"', 'href="{% url \'core:company\' %}"')
header_chunk = header_chunk.replace('href="#projects"', 'href="{% url \'projects:list\' %}"')
header_chunk = header_chunk.replace('href="#team"', 'href="{% url \'team:list\' %}"')
header_chunk = header_chunk.replace('href="#community"', 'href="{% url \'core:community\' %}"')
header_chunk = header_chunk.replace('href="#" class="logo-link"', 'href="{% url \'core:home\' %}" class="logo-link"')

base_html = header_chunk + """
    <main style="min-height: 80vh;">
        {% block content %}{% endblock %}
    </main>
""" + footer_chunk

# Inject Template tags directly inside the homepage body loops
body_chunk = body_chunk.replace('href="#" class="arrow-link"', 'href="{% url \'services:detail\' service.pk %}" class="arrow-link"')
body_chunk = body_chunk.replace('href="{{ article.link|default:\'#\' }}" class="news-link4"', 'href="{% url \'news:detail\' article.pk %}" class="news-link4"')

# Rewrite index.html to inherit
index_html_new = """{% extends 'base.html' %}
{% load static %}
{% block content %}
<!-- Parallax Hero -->
""" + body_chunk + "{% endblock %}"

# Generate Base and Index
with open(os.path.join(templates_dir, "base.html"), "w", encoding="utf-8") as f:
    f.write(base_html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html_new)

print("Inheritance Engine Built: base.html and index.html")

# Create the other 11 templates
generic_header = """{% extends 'base.html' %}
{% load static %}
{% block content %}
<section class="page-header" style="background-color: var(--c-primary); padding: 160px 0 80px; text-align: center;">
    <div class="container4">
        <h1 style="color: white; font-size: 50px;">{TITLE}</h1>
    </div>
</section>
"""

templates = {
    "services/list.html": generic_header.replace("{TITLE}", "Core Capabilities") + """
<section class="expertise-area bg-light-gray" style="padding: 80px 0;">
    <div class="container4">
        {% for service in services %}
        <div class="staggered-block reveal-up active {% if forloop.counter|divisibleby:2 %}st-reverse{% endif %}">
            <div class="st-img">
                {% if service.image %}<a href="{% url 'services:detail' service.pk %}"><img src="{{ service.image.url }}" alt="{{ service.title }}"></a>{% endif %}
            </div>
            <div class="st-text">
                <div class="st-num">0{{ forloop.counter }}</div>
                <h3>{{ service.title }}</h3>
                <p>{{ service.description }}</p>
                <a href="{% url 'services:detail' service.pk %}" class="arrow-link">Explore Solutions <span class="arrow">&rarr;</span></a>
            </div>
        </div>
        {% empty %}
        <p>No capabilities configured.</p>
        {% endfor %}
    </div>
</section>
{% endblock %}
""",

    "services/detail.html": generic_header.replace("{TITLE}", "{{ service.title }}") + """
<section class="container4" style="padding: 100px 5%; max-width: 1000px; margin: 0 auto; color: var(--c-primary);">
    {% if service.image %}
    <img src="{{ service.image.url }}" style="border-radius: 4px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); margin-bottom: 60px; width: 100%;">
    {% endif %}
    <h2 style="font-size: 36px; margin-bottom: 30px;">Overview</h2>
    <p style="font-size: 18px; line-height: 1.8; margin-bottom: 40px; color: var(--c-text-body);">{{ service.description }}</p>
    {% if service.full_description %}
    <hr style="border: none; border-top: 1px solid var(--c-gray); margin-bottom: 40px;">
    <h3 style="font-size: 28px; margin-bottom: 20px;">Technical Details</h3>
    <div style="font-size: 16px; line-height: 1.8; color: var(--c-text-body); white-space: pre-wrap;">{{ service.full_description }}</div>
    {% endif %}
</section>
{% endblock %}
""",

    "projects/list.html": generic_header.replace("{TITLE}", "Global Operations") + """
<section class="projects-area bg-light-gray" style="padding: 80px 0;">
    <div class="container4">
        <div class="projects-grid4">
            {% for project in projects %}
            <div class="project-box4" style="transform: translateY(0); opacity: 1;">
                <a href="{% url 'projects:detail' project.pk %}">
                    {% if project.image %}<img src="{{ project.image.url }}" alt="{{ project.title }}">{% endif %}
                </a>
                <div class="pb-content4">
                    <h4>{{ project.title }}</h4>
                    {% if project.country %}<p style="color: var(--c-gold); font-size: 13px; font-weight: 600; text-transform: uppercase; margin-bottom: 5px;">{{ project.country }}</p>{% endif %}
                    <p>{{ project.description|truncatewords:20 }}</p>
                    <a href="{% url 'projects:detail' project.pk %}" style="display: inline-block; margin-top: 15px; color: var(--c-primary); font-weight: 600; text-decoration: underline;">View Case Study</a>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</section>
{% endblock %}
""",

    "projects/detail.html": generic_header.replace("{TITLE}", "{{ project.title }}") + """
<section class="container4" style="padding: 100px 5%; max-width: 1000px; margin: 0 auto; color: var(--c-primary);">
    {% if project.image %}
    <img src="{{ project.image.url }}" style="border-radius: 4px; margin-bottom: 40px; width: 100%;">
    {% endif %}
    {% if project.country %}
    <span style="font-family: var(--f-heading); font-size: 13px; font-weight: 600; text-transform: uppercase; padding: 10px 24px; border: 1px solid var(--c-gold); color: var(--c-gold); border-radius: 50px; margin-bottom: 30px; display: inline-block;">{{ project.country }}</span>
    {% endif %}
    <p style="font-size: 18px; line-height: 1.8; margin-bottom: 40px; color: var(--c-text-body);">{{ project.description }}</p>
    {% if project.detailed_scope %}
    <div style="background-color: var(--c-light-gray); padding: 40px; border-left: 4px solid var(--c-gold); margin-bottom: 40px;">
        <h4 style="margin-bottom: 20px;">Project Scope & Objectives</h4>
        <div style="font-size: 16px; line-height: 1.8; color: var(--c-text-body); white-space: pre-wrap;">{{ project.detailed_scope }}</div>
    </div>
    {% endif %}
</section>
{% endblock %}
""",

    "team/list.html": generic_header.replace("{TITLE}", "Meet The Team") + """
<section class="team-area" style="padding: 80px 0;">
    <div class="container4 text-center">
        <div class="team-grid4 text-left">
            {% for member in team_members %}
            <div class="team-card4" style="text-align: left; transform: translateY(0); opacity: 1;">
                <a href="{% url 'team:detail' member.pk %}">
                    <div class="team-img4">{% if member.image %}<img src="{{ member.image.url }}" alt="{{ member.name }}">{% endif %}</div>
                </a>
                <div class="team-info4">
                    <h4>{{ member.name }}</h4>
                    <p class="team-role4">{{ member.role }}</p>
                    <a href="{% url 'team:detail' member.pk %}" style="display: inline-block; margin-top: 10px; font-size: 13px; color: var(--c-primary); font-weight: 600;">Read Bio &rarr;</a>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</section>
{% endblock %}
""",

    "team/detail.html": generic_header.replace("{TITLE}", "{{ member.name }}") + """
<section class="container4" style="padding: 100px 5%; max-width: 1000px; margin: 0 auto;">
    <div style="display: grid; grid-template-columns: 1fr 2fr; gap: 60px; align-items: start;">
        <div>
            {% if member.image %}
            <img src="{{ member.image.url }}" style="width: 100%; border-radius: 4px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            {% endif %}
            <h3 style="margin-top: 20px;">{{ member.name }}</h3>
            <p style="color: var(--c-gold); font-weight: 600; text-transform: uppercase; font-size: 13px;">{{ member.role }}</p>
        </div>
        <div>
            <h4 style="font-size: 26px; border-bottom: 1px solid var(--c-gray); padding-bottom: 15px; margin-bottom: 25px;">Professional Biography</h4>
            {% if member.bio %}
            <div style="font-size: 16px; line-height: 1.9; color: var(--c-text-body); white-space: pre-wrap;">{{ member.bio }}</div>
            {% else %}
            <p>Biography is currently being updated in the system.</p>
            {% endif %}
        </div>
    </div>
</section>
{% endblock %}
""",

    "news/list.html": generic_header.replace("{TITLE}", "Latest Insights") + """
<section class="news-area bg-light-gray" style="padding: 80px 0;">
    <div class="container4">
        <div class="news-grid4">
            {% for article in articles %}
            <div class="news-card4" style="transform: translateY(0); opacity: 1;">
                <a href="{% url 'news:detail' article.pk %}">
                    <div class="news-img4">{% if article.image %}<img src="{{ article.image.url }}" alt="{{ article.title }}">{% endif %}</div>
                </a>
                <div class="news-content4">
                    <span class="news-date4">{{ article.date|date:"M d, Y" }}</span>
                    <h4>{{ article.title|truncatewords:8 }}</h4>
                    <a href="{% url 'news:detail' article.pk %}" class="news-link4">Review Analysis <span class="arrow">&rarr;</span></a>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</section>
{% endblock %}
""",

    "news/detail.html": generic_header.replace("{TITLE}", "Insight Analysis") + """
<section class="container4" style="padding: 80px 5%; max-width: 900px; margin: 0 auto;">
    <div style="text-align: center; margin-bottom: 40px;">
        <span style="color: var(--c-gold); font-weight: 600; text-transform: uppercase; letter-spacing: 2px; font-size: 12px; display: block; margin-bottom: 15px;">{{ article.date|date:"F d, Y" }}</span>
        <h1 style="font-size: 42px; line-height: 1.3; color: var(--c-primary); margin-bottom: 30px;">{{ article.title }}</h1>
        {% if article.image %}
        <img src="{{ article.image.url }}" style="width: 100%; border-radius: 4px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
        {% endif %}
    </div>
    
    {% if article.content %}
    <div style="font-size: 18px; line-height: 2.0; color: var(--c-text-body); white-space: pre-wrap;">{{ article.content }}</div>
    {% else %}
    <div style="text-align: center; padding: 40px; background: var(--c-light-gray);">
        <p style="margin-bottom: 15px;">Full article content is pending publication.</p>
        {% if article.link %}
        <a href="{{ article.link }}" target="_blank" class="btn4 btn4-primary">Read External Source</a>
        {% endif %}
    </div>
    {% endif %}
</section>
{% endblock %}
""",

    "core/company.html": generic_header.replace("{TITLE}", "Corporate Profile") + """
<section class="company-profile" style="padding: 80px 0;">
    <div class="container4 profile-grid">
        <div class="profile-text">
            <h6 class="kicker-heading">THE COMPANY</h6>
            <h2 class="main-heading">A Leading Partner in the Global Mining Industry.</h2>
            <p>Pejuni is a dominant provider of specialized technical services in the mining industry. Based in Mwanza, Tanzania with active operations spanning across Australia, DR Congo, Ghana, and South Africa.</p>
            <p>With an uncompromising commitment to technical expertise and collaborative engineering, we utilize cutting-edge tools and advanced modeling techniques to optimize incredibly complex mining plans and definitively assess ground stability.</p>
            <div class="profile-btn-group">
                <a href="https://pejuni.com/PEJUNI%20company%20profile.pdf" target="_blank" class="btn4 btn4-dark">Download Profile PDF</a>
            </div>
        </div>
        <div class="profile-image">
            <img src="{% static 'choose-img.jpg' %}" alt="Corporate Leadership" style="width: 100%;">
            <div class="gold-accent-box"></div>
        </div>
    </div>
</section>
{% endblock %}
""",

    "core/community.html": generic_header.replace("{TITLE}", "Community Engagement") + """
<section class="community-area" style="padding: 100px 0;">
    <div class="container4 text-center">
        <h6 class="kicker-heading mb-15">OUR IMPACT</h6>
        <h2 class="main-heading mb-60">Building Sustainable Futures.</h2>
        <p style="max-width: 800px; margin: 0 auto; color: var(--c-text-body); font-size: 18px; line-height: 1.8;">Pejuni is deeply committed to sustainable engineering practices and empowering the local communities where we operate. We strictly adhere to environmental safety regulations and prioritize technical skill development across Tanzania and beyond. Our engineering methodologies are designed from the ground up to ensure absolute safety and minimal environmental footprint.</p>
    </div>
</section>
{% endblock %}
""",

    "core/partners.html": generic_header.replace("{TITLE}", "Trusted Partners") + """
<section class="clients-area" style="border: none; padding: 100px 0;">
    <div class="container4 text-center">
        <h6 class="kicker-heading mb-15">OUR NETWORK</h6>
        <h2 class="main-heading mb-60">Endorsed by Industry Leaders.</h2>
        <div class="clients-flex4" style="opacity: 1;">
            {% for partner in partners %}
            <div class="client-logo4" style="flex-direction: column; gap: 15px;">
                <img src="https://www.google.com/s2/favicons?domain={{ partner.logo_domain|urlencode }}&sz=128" alt="{{ partner.name }}" style="opacity: 1; filter: none; height: 60px;">
                <span style="font-size: 14px; font-weight: 600; color: var(--c-primary);">{{ partner.name }}</span>
            </div>
            {% empty %}
            <p>No partners configured in the dashboard.</p>
            {% endfor %}
        </div>
    </div>
</section>
{% endblock %}
"""
}

# Create sub-directories and write out templates
for filepath, html_data in templates.items():
    target = os.path.join(templates_dir, filepath)
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(html_data)
    print(f"Generated Template View: {filepath}")

print("----------")
print("Template Inheritance Architecture successfully deployed.")
