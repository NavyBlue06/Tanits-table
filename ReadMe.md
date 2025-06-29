![Am I responsive screenshot](documentation/amiresp.png)

# Tanit's Table

**Live Site:** [View the live project here](https://tanits-table-5445a6d81e90.herokuapp.com)

Tanit’s Table is a fictional Tunisian restaurant website built with Django. The site allows users to view the menu, learn about the restaurant, and make a table reservation. It is designed to showcase clean design, responsive layout, and CRUD functionality for bookings. This project is part of the Full Stack Development course at Code Institute.

---

## Table of Contents

- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
  - [Design](#design)
- [Features](#features)
- [CRUD Functionality](#crud-functionality)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
  - [Functional Testing](#functional-testing)
  - [Responsive Testing](#responsive-testing)
  - [Validators](#validators)
  - [Lighthouse Testing](#lighthouse-testing)
- [Future Enhancements](#future-enhancements)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

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
- I want users to be able to make, edit, and delete bookings.

### Design

- The site uses a warm, earthy color palette inspired by Tunisian culture.
- It includes a clear navigation bar, footer with contact/social links, and a hero banner.
- Pages are responsive on mobile, tablet, and desktop.

---

## Features

### Implemented Features

| Feature           | Description                                                                  |
|------------------|------------------------------------------------------------------------------|
| Homepage          | Welcome section with restaurant intro, image banner, and map.               |
| Navigation Bar    | Fixed nav with links to Home, Menu, Book a Table, and Login/Register.       |
| Menu Page         | Bootstrap cards displaying sample Tunisian dishes.                          |
| Booking System    | Users can create a booking with name, date, time, and number of guests.     |
| User Auth         | Users can log in, view their bookings, edit, or cancel them.                |
| CRUD              | Bookings support full CRUD (Create, Read, Update, Delete) functionality.    |
| Footer            | Contact info, address, and placeholder social links.                        |
| Responsive Design | Tested and responsive across multiple devices and screen sizes.             |

---

## 🔁 CRUD Functionality

The core feature of Tanit's Table is the table reservation system, which demonstrates full CRUD operations:

| Operation | Feature Description                                                                 |
|-----------|---------------------------------------------------------------------------------------|
| **Create** | Users can submit a table booking using a form with name, email, date, time, and guests. |
| **Read**   | Logged-in users can view their current bookings under the "My Bookings" section.       |
| **Update** | Users can modify existing bookings from the "My Bookings" page.                        |
| **Delete** | Bookings can be cancelled (deleted) by the user via the "My Bookings" section.         |

These operations are available only to authenticated users, ensuring security and personalized access.

---

## Technologies Used

- **Languages:** HTML5, CSS3, Python
- **Frameworks:** Django, Bootstrap 5
- **Libraries:** Crispy Forms, gunicorn
- **Database:** SQLite (development), Postgres via Heroku (deployment)
- **Hosting:** Heroku
- **Version Control:** Git, GitHub
- **Others:** Django Allauth (user accounts)

---

## 🧪 Testing

### ✅ Functional Testing

| **Feature**         | **Test Performed**                                                                 | **Result**              |
|---------------------|-------------------------------------------------------------------------------------|-------------------------|
| Booking Creation    | User can submit the table reservation form and see a confirmation message          | Working as expected ✅   |
| Edit Booking        | Logged-in user can access the edit form, change details, and submit successfully    | Working as expected ✅   |
| Cancel Booking      | User can cancel a booking, which is removed from their "My Bookings" list           | Working as expected ✅   |
| User Auth Flow      | Registration, login, logout, and access control work without issues                 | Working as expected ✅   |
| Navigation Links    | Navbar links redirect to the correct pages for all screen sizes                     | Working as expected ✅   |
| Static Files        | CSS loads properly; favicon, background images, and style assets display correctly  | Working as expected ✅   |

### 📱 Responsive Testing

| Device              | Browser        | Notes     |
|---------------------|----------------|-----------|
| iPhone 12           | Safari/Chrome  | ✅         |
| Samsung Galaxy S20  | Chrome         | ✅         |
| iPad                | Safari         | ✅         |
| Desktop (1920px)    | Chrome/Firefox | ✅         |
| Samsung Zflip 6     | EDGE           | ✅         |

---
### 🔎 Validators

- **HTML:** Validated using [W3C Validator](https://validator.w3.org/)
  
  ![HTML Validation Home](documentation/validations/home.png)  
  ![HTML Validation Menu](documentation/validations/menu.png)

- **CSS:** Checked with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
  
  ![CSS Validation](documentation/validations/css-validation.png)

- **Python:** Validated with `flake8`

   The Python code was validated using `flake8`.  
   No functional or structural errors were found. The only warnings reported were related to line length exceeding 79 characters (`E501`)—these appeared within third-party files inside the virtual environment and do not affect the project's own code.
  
  ![Flake8 Validation](documentation/validations/flake8test.png)

---

### 📊 Lighthouse Testing

| Page           | Performance | Accessibility | Best Practices | SEO  | Screenshot |
|----------------|-------------|----------------|----------------|------|------------|
| Home           | 90          | 100            | 100            | 100  | ![Home](documentation/lighthouse/home.png) |
| Menu           | 88          | 98             | 100            | 100  | ![Menu](documentation/lighthouse/menu.png) |
| Book a Table   | 97          | 100            | 100            | 100  | ![Booking Form](documentation/lighthouse/bookform.png) |
| My Bookings    | 98          | 100            | 100            | 100  | ![My Bookings](documentation/lighthouse/mybookings.png) |

All pages passed Lighthouse audits with high scores.

---

## 🌱 Future Enhancements

While the core functionality is fully implemented, future improvements could include:

- Email confirmation for bookings  
- Admin dashboard for managing reservations  
- Filtering menu items by category or dietary preferences  
- Google Maps integration for better location UX  

---

## Deployment

### Steps:

1. GitHub repo created and code pushed.
2. Heroku app set up with Postgres, gunicorn, and required environment variables.
3. Static files handled using WhiteNoise.
4. Cloudinary used for media file storage.
5. App deployed live at: [https://tanits-table-5445a6d81e90.herokuapp.com](https://tanits-table-5445a6d81e90.herokuapp.com)

---

## Credits

- **Developed by:** Navah Eierdal  
- **Inspiration:** Code Institute Django walkthroughs, Tunisian cuisine & culture  
- **Images:** DALLE  

---

## Acknowledgements

- Thanks to the Code Institute community for their support during one of the worst periods of my life.  
- Special thanks to reviewers and peers who gave feedback during development.
