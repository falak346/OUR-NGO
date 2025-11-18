# NGO Website (Django)

This project is a Django-based website for an NGO, including:
- Home page
- About page
- Events section
- Blog
- Contact form
- Admin dashboard

## 🚀 Features
- Django 4+
- App structure:
  - `core` – main pages (Home, About)
  - `events` – event listing
  - `blog` – blog posts
  - `ngo_site` – main Django project config
- Templates included for all pages
- SQLite database by default

## 🛠 Installation

```bash
git clone https://github.com/USERNAME/REPO.git
cd ngo_site_starter
python -m venv env
source env/bin/activate     # Mac/Linux
env\Scripts\activate        # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Project Structure

```
ngo_site/
├── manage.py
├── requirements.txt
├── README.md
├── .env.example
├── ngo_site/            # project settings/urls
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── about.html
│   │   ├── contact.html
│   │   ├── blog/
│   │   │   ├── post_list.html
│   │   │   └── post_detail.html
│   │   ├── donations/
│   │   │   ├── donate.html
│   │   │   └── thanks.html
│   │   └── events/
│   │       ├── event_list.html
│   │       └── event_detail.html
│   └── static/
│       └── css/styles.css
├── core/
│   ├── apps.py, views.py, urls.py
├── donations/
│   ├── models.py, forms.py, views.py, urls.py, admin.py
├── blog/
│   ├── models.py, views.py, urls.py, admin.py
└── events/
    ├── models.py, views.py, urls.py, admin.py
```

