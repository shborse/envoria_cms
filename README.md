# Envoría CMS Prototype

A lightweight Django-based Content Management System (CMS) prototype for internship technical assessment purposes.

## Features

* **User Management** – Create and manage users with admin privileges.
* **Dynamic Pages** – Home, About, Services, Career pages.
* **Form Submissions** – Contact, Demo, Admission, and Internship application forms.
* **Project & Gallery Management** – Add projects, case studies, and gallery images.
* **Admin Dashboard** – Clean interface to manage all content.

## Tech Stack

* **Backend:** Django
* **Database:** SQLite (default)
* **Frontend:** Django Templates, HTML, CSS

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shborse/envoria_cms.git
   cd envoria_cms
   ```
2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate # Mac/Linux
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:

   ```bash
   python manage.py migrate
   ```
5. Create a superuser for admin access:

   ```bash
   python manage.py createsuperuser
   ```
6. Run the server:

   ```bash
   python manage.py runserver
   ```

## Usage

* Access the CMS at `http://127.0.0.1:8000/`.
* Admin dashboard at `http://127.0.0.1:8000/admin/`.



