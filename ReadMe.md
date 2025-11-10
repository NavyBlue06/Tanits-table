![Am I responsive screenshot](documentation\amiresp.png)

# Tanit's Table

**Live Site:** [View the live project here](https://tanits-table-5445a6d81e90.herokuapp.com)

Tanit’s Table is a fictional Tunisian restaurant website built with Django. The site allows users to explore the menu, learn about the restaurant, and manage table reservations with full CRUD functionality. Designed for the Full Stack Development course at Code Institute, it emphasizes clean design, responsive layout, accessibility, and secure deployment.

---

## Table of Contents

- [Value Proposition](#value-proposition)
- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
  - [Design Decisions](#design-decisions)
  - [Wireframes](#wireframes)
- [Features](#features)
- [CRUD Functionality](#crud-functionality)
- [Database Schema](#database-schema)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
  - [Functional Testing](#functional-testing)
  - [Responsive Testing](#responsive-testing)
  - [Validators](#validators)
  - [Lighthouse Testing](#lighthouse-testing)
  - [Bugs and Resolutions](#bugs-and-resolutions)
- [Future Enhancements](#future-enhancements)
- [Deployment](#deployment)
  - [Prerequisites](#prerequisites)
  - [Heroku Deployment](#heroku-deployment)
  - [Local Deployment](#local-deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

---

## Value Proposition

Tanit’s Table offers an intuitive platform for users to explore Tunisian cuisine, browse a menu, and book tables seamlessly. It prioritizes user experience with a responsive, accessible interface and a robust booking system, reflecting Tunisian cultural aesthetics. For the restaurant owner, it provides secure, efficient reservation management, ensuring a professional and personalized experience for all users.

---

## User Experience (UX)

### User Stories

#### First Time Visitors
- I want to understand what kind of food the restaurant serves.
- I want to see the restaurant’s contact information and location.
- I want to browse the menu and make a booking.

#### Returning Visitors
- I want to check if my previous booking still exists.
- I want to cancel or modify my reservation.

#### Site Owner
- I want to display the restaurant’s menu in an elegant way.
- I want users to be able to make, edit, and delete bookings securely.
- I want to see the booking in the admin section 

### Design Decisions

- **Color Palette**: Warm, earthy tones (terracotta, olive green, beige, blue and white) inspired by Tunisian culture for authenticity and warmth.
- **Typography**: Roboto (body) and Lora (headings) for readability and aesthetic appeal.
- **Layout**: Fixed navigation bar for accessibility, hero banner for visual impact, and footer with contact/social links.
- **Accessibility**: High-contrast colors, alt text for images, and ARIA landmarks for screen reader support.
- **Responsiveness**: Bootstrap 5 ensures seamless adaptation across mobile, tablet, and desktop devices.

## Wireframes

### Desktop Wireframes

| Page          | Wireframe |
|---------------|-----------|
| Home Page     | ![Desktop Home Wireframe](documentation/wireframes/desktop_home_wireframe.png) |
| Menu Page     | ![Desktop Menu Wireframe](documentation/wireframes/desktop_menu_wireframe.png) |
| Book a Table  | ![Desktop Book a Table Wireframe](documentation/wireframes/desktop_bookatable_wireframe.png) |

---

## Features

### Implemented Features

| Feature           | Description                                                                  |
|-------------------|------------------------------------------------------------------------------|
| Homepage          | Welcome section with restaurant intro, image banner, and map.               |
| Navigation Bar    | Fixed nav with links to Home, Menu, Book a Table, and Login/Register.       |
| Menu Page         | Bootstrap cards displaying sample Tunisian dishes.                          |
| Booking System    | Users can create bookings with name, date, time, and guests (prefilled for logged-in users). |
| User Auth         | Users can log in, view, edit, or cancel their bookings.                     |
| CRUD              | Full Create, Read, Update, Delete functionality for bookings.               |
| Footer            | Contact info, address, and placeholder social links.                        |
| Responsive Design | Tested across multiple devices and screen sizes.                            |
| Custom Error Pages| Custom 403, 404, and 500 error pages for a consistent user experience.      |
| Meta Titles       | Unique meta titles for each page to improve usability and SEO.              |
---

## 🔁 CRUD Functionality

The table reservation system is the core feature, supporting full CRUD operations:

| Operation | Feature Description                                                                 |
|-----------|---------------------------------------------------------------------------------------|
| **Create** | Users submit bookings via a form (name, email, date, time, guests). Prefilled for logged-in users. Past dates are restricted. |
| **Read**   | Logged-in users view their bookings in the "My Bookings" section.                    |
| **Update** | Users can modify bookings via the "My Bookings" page.                                |
| **Delete** | Users can cancel bookings, removing them from the "My Bookings" list.                |

Input validation prevents bookings for past dates, enhancing usability and reliability.

---

## Database Schema


This section describes the data model implemented in the project and the relationships between its entities.

---

### ER Overview

```mermaid
erDiagram
    AUTH_USER ||--o{ BOOKING : "creates"
    AUTH_USER {
        int id PK
        string username
        string email
        string first_name
        string last_name
        datetime date_joined
        boolean is_active
    }
    BOOKING {
        int id PK
        int user_id FK "→ auth_user.id; on delete CASCADE"
        string name "max_length=100"
        string email "EmailField"
        date date
        time time
        int guests "PositiveIntegerField"
    }
```




## Technologies Used

- **Languages**: HTML5, CSS3, Python
- **Frameworks**: Django, Bootstrap 5
- **Libraries**: Crispy Forms, gunicorn, dj-database-url, python-decouple
- **Database**: SQLite (development), Postgres (Heroku production)
- **Hosting**: Heroku
- **Media Storage**: Cloudinary
- **Version Control**: Git, GitHub
- **Others**: Django Allauth (user accounts)

---

## 🧪 Testing

### ✅ Functional Testing

| **Feature**         | **Test Performed**                                                                 | **Result**              |
|---------------------|-------------------------------------------------------------------------------------|-------------------------|
| Booking Creation    | Submit reservation form with valid data; past dates restricted                     | Working as expected ✅   |
| Edit Booking        | Logged-in user accesses edit form, changes details, submits successfully           | Working as expected ✅   |
| Cancel Booking      | User cancels booking, removed from "My Bookings" list                              | Working as expected ✅   |
| User Auth Flow      | Registration, login, logout, and access control function correctly                 | Working as expected ✅   |
| Navigation Links    | Navbar links redirect correctly across all screen sizes                            | Working as expected ✅   |
| Static Files        | CSS, favicon, and images load correctly                                            | Working as expected ✅   |
| Error Pages         | Custom 403, 404, and 500 error pages display appropriately                        | Working as expected ✅   |

### 📱 Responsive Testing

| Device              | Browser        | Notes     |
|---------------------|----------------|-----------|
| iPhone 12           | Safari/Chrome  | ✅         |
| Samsung Galaxy S20  | Chrome         | ✅         |
| iPad                | Safari         | ✅         |
| Desktop (1920px)    | Chrome/Firefox | ✅         |
| Samsung Zflip 6     | Edge           | ✅         |

### 🔎 Validators

- **HTML**: Validated using [W3C Validator](https://validator.w3.org/)  
  - [Home](../../Downloads/documentation/validations/home.png)  
  - [Menu](../../Downloads/documentation/validations/menu.png)  
  - [Booking Form](../../Downloads/documentation/validations/booking.png)  

- **CSS**: Validated using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)  
  - [CSS Validation](../../Downloads/documentation/validations/css-validation.png)  

- **Python**: Validated with `flake8`  
  No functional or structural errors. Line length warnings (`E501`) in third-party files do not affect project code.  
  - [Flake8 Validation](../../Downloads/documentation/validations/flake8test.png)

### 📊 Lighthouse Testing

| Page           | Performance | Accessibility | Best Practices | SEO  | Screenshot |
|----------------|-------------|----------------|----------------|------|------------|
| Home           | 90          | 100            | 100            | 100  | [Home](../../Downloads/documentation/lighthouse/home.png) |
| Menu           | 88          | 98             | 100            | 100  | [Menu](../../Downloads/documentation/lighthouse/menu.png) |
| Book a Table   | 97          | 100            | 100            | 100  | [Booking Form](../../Downloads/documentation/lighthouse/bookform.png) |
| My Bookings    | 98          | 100            | 100            | 100  | [My Bookings](../../Downloads/documentation/lighthouse/mybookings.png) |

### 🐞 Bugs and Resolutions

| **Bug**                     | **Description**                                   | **Resolution**                                      | **Status** |
|-----------------------------|--------------------------------------------------|----------------------------------------------------|------------|
| Past Date Bookings          | Users could book past dates                      | Added date validation in `BookingForm`             | Resolved ✅ |
| Debug Mode in Production    | `DEBUG=True` exposed sensitive info              | Set `DEBUG=False` via environment variables        | Resolved ✅ |
| Broken Testing Links        | Incorrect paths to validation screenshots         | Updated paths in `documentation/` folder           | Resolved ✅ |

*Open Bugs*: None at this time.

---

## 🌱 Future Enhancements

- Email confirmation for bookings.
- Admin dashboard for reservation management.
- Menu filtering by category or dietary preferences.
- Google Maps integration for location UX.
- Automated tests using Django’s testing framework.

---

## Deployment

This project is deployed to **Heroku** with **Postgres** as the production database and **Cloudinary** for media storage. Below are detailed steps for deploying to Heroku and setting up locally.

### Prerequisites

- **Git**: For version control (`git --version`).
- **Python 3.8+**: For Django (`python --version`).
- **pip**: Python package manager (`pip --version`).
- **Heroku CLI**: For deployment (`heroku --version`).
- **Cloudinary Account**: For media storage ([cloudinary.com](https://cloudinary.com)).
- **Heroku Account**: For hosting ([heroku.com](https://heroku.com)).
- **GitHub Account**: For repository management.
- **Virtual Environment (local)**: To isolate dependencies (`python -m venv --version`).

### Heroku Deployment

1. **Create the Heroku App**  
   - Log in to [Heroku](https://dashboard.heroku.com/).  
   - Click **New → Create new app**, name it (e.g., `tanits-table`), and select a region.  

2. **Add a Postgres Database**  
   - In **Resources**, search for **Heroku Postgres** in Add-ons.  
   - Select **Hobby Dev** (free) plan.  
   - `DATABASE_URL` is automatically set in Config Vars.

3. **Set Config Vars**  
   - Go to **Settings → Reveal Config Vars** and add:  
     - `SECRET_KEY`: Generate using [djecrety.ir](https://djecrety.ir/).  
     - `DEBUG`: Set to `False` for production security.  
     - `DATABASE_URL`: Auto-set by Heroku Postgres.  
     - `CLOUDINARY_URL`: From Cloudinary Dashboard (format: `cloudinary://API_KEY:API_SECRET@CLOUD_NAME`).  
     - `DISABLE_COLLECTSTATIC`: Set to `1` temporarily (remove before final deployment).  

   Example:
   ```text
   SECRET_KEY=your-secure-django-secret-key
   DEBUG=False
   DATABASE_URL=postgres://[auto-generated]
   CLOUDINARY_URL=cloudinary://123456789:abcdefg@your-cloud-name
   DISABLE_COLLECTSTATIC=1
   ```

4. **Prepare the Repository**  

Include in project root:  
- `requirements.txt`: Generate with `pip freeze > requirements.txt`.  
- `Procfile`: Contains:  
  ```text
  web: gunicorn tanits_table.wsgi
  ```

Verify `settings.py` (already configured for python-decouple and dj_database_url):  
```python
from decouple import config
import dj_database_url
import os

SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = ["tanits-table-5445a6d81e90.herokuapp.com", "localhost", "127.0.0.1"]

if "DATABASE_URL" in os.environ:
    DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
```

5. **Push Code to Heroku**  
```bash
heroku login
heroku git:remote -a tanits-table
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

6. **Run Migrations**  
```bash
heroku run python manage.py migrate
```

7. **Create a Superuser (Optional)**  
```bash
heroku run python manage.py createsuperuser
```

8. **Collect Static Files**  
- Remove `DISABLE_COLLECTSTATIC` from Config Vars.  
- Run:  
  ```bash
  heroku run python manage.py collectstatic --noinput
  ```

9. **Open the Application**  
```bash
heroku open
```

Live site: https://tanits-table-5445a6d81e90.herokuapp.com

10. **Verify Deployment**  
- Test a privileged link (e.g., `/booking/edit/34/`) in incognito mode to confirm `DEBUG=False`.  
- Verify static files (via WhiteNoise), media (via Cloudinary), and CRUD operations work.

---

### Local Deployment

1. **Clone the Repository**  
```bash
git clone https://github.com/YOUR-USERNAME/tanits-table.git
cd tanits-table
```

2. **Set Up a Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install Dependencies**  
```bash
pip install -r requirements.txt
```

4. **Set Up Environment Variables**  
Create `.env` in project root:  
```text
SECRET_KEY=your-local-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
CLOUDINARY_URL=cloudinary://API_KEY:API_SECRET@CLOUD_NAME
```

Install python-decouple:  
```bash
pip install python-decouple
```

5. **Apply Migrations**  
```bash
python manage.py migrate
```

6. **Create a Superuser (Optional)**  
```bash
python manage.py createsuperuser
```

7. **Run the Development Server**  
```bash
python manage.py runserver
```

Access at: http://127.0.0.1:8000.

8. **Verify Local Setup**  
- Confirm site loads in browser.  
- Test CRUD operations and media display (via Cloudinary).

---

## Credits

- Developed by: Navah Eierdal  
- Inspiration: Code Institute Django walkthroughs, Tunisian cuisine & culture  
- Images: DALL·E  
- Wireframes: Figma  

---

## Acknowledgements

- Thanks to the Code Institute community for support during challenging times.  
- Gratitude to reviewers and peers for feedback.  
- ChatGPT for assisting with README improvements.  
