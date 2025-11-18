# NGO Website (Django) — Starter Kit

A clean starter for an NGO site built with Django. It includes:
- Pages (Home, About, Contact)
- Donations (simple form & admin)
- Blog (posts & detail pages)
- Events (list & detail pages)
- Auth-ready (Django auth, templates include login/logout links)
- Tailwind via CDN (swap with real pipeline later)
- Env-ready settings

## Quickstart

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Create .env from example and update values if needed
cp .env.example .env

# Run database migrations
python manage.py migrate

# Create a superuser for admin
python manage.py createsuperuser

# Start the server
python manage.py runserver
```

Open http://127.0.0.1:8000/ to view the site, and http://127.0.0.1:8000/admin/ for the admin.

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

## Roadmap

**Phase 1 — MVP (this repo):**
- ✅ Static pages (Home, About, Contact)
- ✅ Donations model + form (no payment gateway yet)
- ✅ Blog & Events CRUD via admin, public listing/detail pages
- ✅ Basic styling (Tailwind CDN) + responsive layout
- ✅ Environment-based settings

**Phase 2 — Engagement:**
- Add newsletter signups (Mailchimp/Brevo)
- Add volunteer registration form + admin export
- Add image gallery & media library
- Blog categories/tags + search

**Phase 3 — Donations v2:**
- Integrate real payment gateway (Razorpay/Stripe/PayPal)
- Record transactions & send receipts via email
- Donor portal: view history, download receipts (auth)

**Phase 4 — Impact & Transparency:**
- Project pages: goals, budgets, progress
- Impact metrics dashboard
- Annual reports & downloads

**Phase 5 — Production Hardening:**
- Switch to Postgres
- Caching + security headers
- CI/CD + containerization
- Tailwind build pipeline (Django Compressor/Whitenoise)
- Media storage (S3/Cloud) + backups

Happy building! 🙌
