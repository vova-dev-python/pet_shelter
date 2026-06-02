Pet Shelter Project
A Django-based web application designed for managing a pet shelter, tracking available pets, and coordinating volunteers.

Features
- Volunteer Management: Seamless tracking of shelter volunteers, including their profile details, registration data, and experience.

- Pet Profiles: Detailed registration of pets (name, animal type, age, and location) currently staying at the shelter.

- Volunteer Assignment: Ability to easily assign or toggle volunteers for specific pets.

- Django Admin Panel: Fully customized administrative interface for shelter coordinators to manage database records.

PEP 8 Compliant: Clean code base that strictly follows modern Python and Django style guides.

Setup and Installation
Follow these steps to set up and run the project locally:

1. Clone the repository
git clone https://github.com/vova-dev-python/pet_shelter
cd pet_shelter

2. Create and activate a virtual environment
For Windows:
python -m venv venv
venv\Scripts\activate
For macOS and Linux:
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run migrations
python manage.py migrate

5. Create a superuser
python manage.py createsuperuser

6. Start the server
python manage.py runserver

7. Once the server is running, open your browser and navigate to http://127.0.0.1:8000/ to explore the website.