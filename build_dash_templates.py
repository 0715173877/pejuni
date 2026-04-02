import os

BASE_DIR = "."
DASH_DIR = os.path.join(BASE_DIR, "templates", "dashboard")

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def build_templates():
    ensure_dir(DASH_DIR)
    for sub in ['services', 'projects', 'team', 'news']:
        ensure_dir(os.path.join(DASH_DIR, sub))

    # base_dash.html
    base_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pejuni CMS Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --c-primary: #122137;
            --c-secondary: #1a304e;
            --c-gold: #e1ab36;
            --c-white: #ffffff;
            --c-bg: #f4f6f8;
            --c-text: #334155;
            --c-border: #e2e8f0;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'Inter', sans-serif; background-color: var(--c-bg); color: var(--c-text); display: flex; min-height: 100vh; }
        
        .sidebar { width: 280px; background-color: var(--c-primary); color: white; display: flex; flex-direction: column; }
        .sidebar-header { padding: 30px; border-bottom: 1px solid rgba(255,255,255,0.1); text-align: center; }
        .sidebar-header h2 { font-family: 'Montserrat', sans-serif; letter-spacing: 2px; color: var(--c-gold); font-size: 24px; }
        .sidebar-nav { padding: 30px 0; flex-grow: 1; }
        .nav-link { display: block; padding: 15px 30px; color: rgba(255,255,255,0.7); text-decoration: none; font-weight: 500; transition: all 0.3s; }
        .nav-link:hover, .nav-link.active { background-color: var(--c-secondary); color: var(--c-gold); border-left: 4px solid var(--c-gold); }
        .sidebar-footer { padding: 20px 30px; border-top: 1px solid rgba(255,255,255,0.1); text-align: center; }
        .sidebar-footer a { color: var(--c-gold); text-decoration: none; font-size: 14px; }

        .main-content { flex: 1; display: flex; flex-direction: column; overflow-y: auto; }
        .topbar { background-color: white; padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--c-border); }
        .topbar h1 { font-family: 'Montserrat', sans-serif; font-size: 20px; color: var(--c-primary); }
        .topbar-actions a { color: var(--c-text); text-decoration: none; font-size: 14px; margin-left: 20px; }
        .topbar-actions a.btn-logout { background-color: #fee2e2; color: #dc2626; padding: 8px 15px; border-radius: 4px; font-weight: 600; }

        .content-area { padding: 40px; flex-grow: 1; max-width: 1200px; margin: 0 auto; width: 100%; }
        
        .card { background: white; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); padding: 30px; margin-bottom: 30px; }
        .card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px; padding-bottom: 15px; border-bottom: 1px solid var(--c-border); }
        .card-title { font-family: 'Montserrat', sans-serif; font-size: 18px; color: var(--c-primary); }
        
        .btn { display: inline-block; padding: 10px 20px; font-family: 'Montserrat', sans-serif; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; color: white; border-radius: 4px; text-decoration: none; border: none; cursor: pointer; transition: 0.3s; }
        .btn-gold { background-color: var(--c-gold); }
        .btn-gold:hover { background-color: #c99321; }
        .btn-navy { background-color: var(--c-primary); }
        .btn-navy:hover { background-color: var(--c-secondary); }
        .btn-red { background-color: #ef4444; }
        .btn-red:hover { background-color: #dc2626; }
        .btn-sm { padding: 6px 12px; font-size: 11px; margin-right: 5px; }

        .data-table { width: 100%; border-collapse: collapse; }
        .data-table th, .data-table td { padding: 15px; text-align: left; border-bottom: 1px solid var(--c-border); }
        .data-table th { font-family: 'Montserrat', sans-serif; font-size: 13px; text-transform: uppercase; color: #64748b; font-weight: 600; }
        .data-table tr:hover { background-color: #f8fafc; }
        
        /* Forms */
        .form-group { margin-bottom: 20px; }
        .form-label { display: block; font-weight: 500; margin-bottom: 8px; color: var(--c-primary); font-size: 14px; }
        .form-control { width: 100%; padding: 12px 15px; border: 1px solid #cbd5e1; border-radius: 4px; font-family: 'Inter', sans-serif; font-size: 15px; transition: 0.3s; }
        .form-control:focus { outline: none; border-color: var(--c-gold); box-shadow: 0 0 0 3px rgba(225, 171, 54, 0.2); }
        .form-text { display: block; font-size: 12px; color: #64748b; margin-top: 5px; }
        .helptext { font-size: 12px; color: #64748b; display: block; margin-top: 4px; }
    </style>
</head>
<body>
    <!-- Sidebar -->
    <aside class="sidebar">
        <div class="sidebar-header">
            <h2>PEJUNI CMS</h2>
            <p style="font-size: 12px; color: rgba(255,255,255,0.5); letter-spacing: 1px;">Enterprise Dashboard</p>
        </div>
        <nav class="sidebar-nav">
            <a href="{% url 'dashboard:home' %}" class="nav-link">Dashboard Overview</a>
            <a href="{% url 'dashboard:projects_list' %}" class="nav-link">Manage Projects</a>
            <a href="{% url 'dashboard:services_list' %}" class="nav-link">Manage Services</a>
            <a href="{% url 'dashboard:team_list' %}" class="nav-link">Manage Team</a>
            <a href="{% url 'dashboard:news_list' %}" class="nav-link">Manage News</a>
        </nav>
        <div class="sidebar-footer">
            <a href="/">← Return to Live Site</a>
        </div>
    </aside>

    <!-- Main -->
    <main class="main-content">
        <header class="topbar">
            <h1>{% block page_title %}Dashboard{% endblock %}</h1>
            <div class="topbar-actions">
                <span>Welcome, {{ user.username }}</span>
                <form action="{% url 'dashboard:logout' %}" method="post" style="display:inline; margin-left:15px;">
                    {% csrf_token %}
                    <button type="submit" class="btn btn-red btn-sm">Log Out</button>
                </form>
            </div>
        </header>

        <div class="content-area">
            {% block content %}{% endblock %}
        </div>
    </main>
</body>
</html>
"""
    with open(os.path.join(DASH_DIR, "base_dash.html"), "w") as f: f.write(base_html)

    # home.html
    home_html = """{% extends "dashboard/base_dash.html" %}
{% block page_title %}Dashboard Overview{% endblock %}
{% block content %}
<div class="card">
    <div class="card-header">
        <h2 class="card-title">System Overview</h2>
    </div>
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px;">
        <div style="padding: 25px; border-radius: 6px; background-color: #f8fafc; border-left: 4px solid var(--c-gold);">
            <div style="font-size: 12px; font-weight: 600; color: #64748b; text-transform: uppercase;">Total Projects</div>
            <div style="font-size: 36px; font-weight: 700; color: var(--c-primary); margin-top: 10px;">{{ projects_count }}</div>
        </div>
        <div style="padding: 25px; border-radius: 6px; background-color: #f8fafc; border-left: 4px solid var(--c-gold);">
            <div style="font-size: 12px; font-weight: 600; color: #64748b; text-transform: uppercase;">Total Services</div>
            <div style="font-size: 36px; font-weight: 700; color: var(--c-primary); margin-top: 10px;">{{ services_count }}</div>
        </div>
        <div style="padding: 25px; border-radius: 6px; background-color: #f8fafc; border-left: 4px solid var(--c-gold);">
            <div style="font-size: 12px; font-weight: 600; color: #64748b; text-transform: uppercase;">Team Members</div>
            <div style="font-size: 36px; font-weight: 700; color: var(--c-primary); margin-top: 10px;">{{ team_count }}</div>
        </div>
        <div style="padding: 25px; border-radius: 6px; background-color: #f8fafc; border-left: 4px solid var(--c-gold);">
            <div style="font-size: 12px; font-weight: 600; color: #64748b; text-transform: uppercase;">News Articles</div>
            <div style="font-size: 36px; font-weight: 700; color: var(--c-primary); margin-top: 10px;">{{ news_count }}</div>
        </div>
    </div>
</div>
{% endblock %}
"""
    with open(os.path.join(DASH_DIR, "home.html"), "w") as f: f.write(home_html)

    # login.html
    login_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pejuni CMS - Secure Login</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600&family=Inter:wght@400;500&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background-color: #122137; height: 100vh; display: flex; align-items: center; justify-content: center; margin: 0; }
        .login-box { background: white; padding: 40px; border-radius: 8px; width: 400px; box-shadow: 0 20px 40px rgba(0,0,0,0.3); text-align: center; }
        h2 { font-family: 'Montserrat', sans-serif; color: #122137; margin-bottom: 30px; letter-spacing: -1px; }
        .form-control { width: 100%; padding: 12px 15px; margin-bottom: 20px; border: 1px solid #cbd5e1; border-radius: 4px; box-sizing: border-box; }
        .btn-gold { width: 100%; padding: 14px; background-color: #e1ab36; color: white; border: none; border-radius: 4px; font-family: 'Montserrat', sans-serif; font-weight: 600; cursor: pointer; text-transform: uppercase; letter-spacing: 1px; }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>Secure Area</h2>
        <form method="post">
            {% csrf_token %}
            {{ form.username.errors }}
            <input type="text" name="username" class="form-control" placeholder="Username" required>
            {{ form.password.errors }}
            <input type="password" name="password" class="form-control" placeholder="Password" required>
            <button type="submit" class="btn-gold">Authenticate</button>
        </form>
    </div>
</body>
</html>
"""
    with open(os.path.join(DASH_DIR, "login.html"), "w") as f: f.write(login_html)

    # shared_form.html
    form_html = """{% extends "dashboard/base_dash.html" %}
{% block page_title %}{{ title }}{% endblock %}
{% block content %}
<div class="card" style="max-width: 800px;">
    <div class="card-header">
        <h2 class="card-title">{{ title }} Details</h2>
    </div>
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.non_field_errors }}
        {% for field in form %}
            <div class="form-group">
                <label class="form-label">{{ field.label }}</label>
                {{ field }}
                {% if field.help_text %}
                <span class="helptext">{{ field.help_text }}</span>
                {% endif %}
                <span style="color: red; font-size:12px;">{{ field.errors }}</span>
            </div>
        {% endfor %}
        <div style="margin-top: 30px; border-top: 1px solid var(--c-border); padding-top: 20px; display: flex; gap: 15px;">
            <button type="submit" class="btn btn-gold">Save Entry</button>
            <button type="submit" name="_save_and_preview" value="1" class="btn btn-navy">Save &amp; Preview on Site</button>
            <a href="javascript:history.back()" class="btn btn-navy" style="background-color: transparent; color: var(--c-text); border: 1px solid var(--c-border);">Cancel</a>
        </div>
    </form>
</div>
{% endblock %}
"""
    with open(os.path.join(DASH_DIR, "shared_form.html"), "w") as f: f.write(form_html)

    # shared_confirm_delete.html
    del_html = """{% extends "dashboard/base_dash.html" %}
{% block page_title %}Warning: Deletion{% endblock %}
{% block content %}
<div class="card" style="max-width: 600px; border-top: 4px solid #ef4444;">
    <div class="card-header">
        <h2 class="card-title" style="color: #ef4444;">Permanently Delete?</h2>
    </div>
    <p style="font-size: 16px; margin-bottom: 25px;">Are you absolutely sure you want to delete this record (<strong>{{ object }}</strong>)? This action cannot be undone.</p>
    <form method="post">
        {% csrf_token %}
        <div style="display: flex; gap: 15px;">
            <button type="submit" class="btn btn-red">Yes, Delete Forever</button>
            <a href="javascript:history.back()" class="btn btn-navy">Cancel & Go Back</a>
        </div>
    </form>
</div>
{% endblock %}
"""
    with open(os.path.join(DASH_DIR, "shared_confirm_delete.html"), "w") as f: f.write(del_html)

    # List views for each app
    list_templates = {
        'services': ("Services", "Title", "{{ obj.title }}", "services_edit", "services_delete", "services_add"),
        'projects': ("Projects", "Title", "{{ obj.title }}", "projects_edit", "projects_delete", "projects_add"),
        'team': ("Team Members", "Name", "{{ obj.name }} - {{ obj.role }}", "team_edit", "team_delete", "team_add"),
        'news': ("News Articles", "Headline", "{{ obj.title }}", "news_edit", "news_delete", "news_add"),
    }

    for app, t in list_templates.items():
        list_html = f"""{{% extends "dashboard/base_dash.html" %}}
{{% block page_title %}}Manage {t[0]}{{% endblock %}}
{{% block content %}}
<div class="card">
    <div class="card-header">
        <h2 class="card-title">Existing {t[0]}</h2>
        <a href="{{% url 'dashboard:{t[5]}' %}}" class="btn btn-navy">+ Add New Entry</a>
    </div>
    <table class="data-table">
        <thead>
            <tr>
                <th style="width: 50px;">ID</th>
                <th>{t[1]}</th>
                <th style="width: 250px;">Last Modified</th>
                <th style="width: 200px; text-align: right;">Actions</th>
            </tr>
        </thead>
        <tbody>
            {{% for obj in objects %}}
            <tr>
                <td style="color: #64748b;">#{{{{ obj.pk }}}}</td>
                <td style="font-weight: 500;">{t[2]}</td>
                <td style="color: #64748b; font-size: 13px;">{{{{ obj.updated_at|date:"M d, Y - H:i" }}}} ({{{{ obj.updated_by }}}})</td>
                <td style="text-align: right;">
                    <a href="{{% url 'dashboard:{t[3]}' obj.pk %}}" class="btn btn-gold btn-sm">Edit</a>
                    <a href="{{% url 'dashboard:{t[4]}' obj.pk %}}" class="btn btn-red btn-sm">Delete</a>
                </td>
            </tr>
            {{% empty %}}
            <tr>
                <td colspan="4" style="text-align: center; color: #94a3b8; padding: 30px;">There are currently no {t[0].lower()} configured in the system.</td>
            </tr>
            {{% endfor %}}
        </tbody>
    </table>
</div>
{{% endblock %}}
"""
        with open(os.path.join(DASH_DIR, app, "list.html"), "w") as f: f.write(list_html)

if __name__ == '__main__':
    build_templates()
    print("Dashboard HTML Templates successfully generated.")
