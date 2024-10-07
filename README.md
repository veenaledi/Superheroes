# Flask Code Challenge - Superheroes

## Author
Neema Naledi

## Description
This project implements a Flask API for tracking superheroes and their superpowers. The API interacts with a database to manage data related to heroes, their powers, and the relationships between them.

This API provides a solid foundation for tracking superheroes and their powers, with robust features for managing data integrity and relationships. Use the provided frontend to interact with the API, or test directly using Postman or automated tests.

## Features
RESTful API: Implements various endpoints to create, read, update, and delete heroes and powers.
Database Integration: Uses SQLAlchemy for ORM with SQLite as the database.
Postman Collection: A Postman collection is provided for testing API endpoints.
Validation: Ensures data integrity with validations for models.

Heroes
GET /heroes: Retrieve a list of all heroes.

GET /heroes/
: Retrieve details of a specific hero by ID.

Powers
GET /powers: Retrieve a list of all powers.

GET /powers/
: Retrieve details of a specific power by ID.

PATCH /powers/
: Update an existing power's description.

Hero Powers
POST /hero_powers: Create a new association between a hero and a power.

## Installation
1. Set up a virtual environment (recommended)

2. Install dependencies: Make sure you have SQLAlchemy installed. 
You can install it using pip: pip install sqlalchemy

### Prerequisites
- Git (for forking and cloning the repository)
Ensure you have the following installed on your machine:

Python 3.6 or higher
npm

### Steps
1. Clone the repository:
   ```bash
   git clone:
   git@github.com:veenaledi/Superheroes.git

## Getting Started
1. Install Backend Dependencies
Install the required Python packages:
pipenv install
pipenv shell

2. Install Frontend Dependencies
Install the necessary Node.js packages for the frontend:
npm install --prefix client

## Implementation
The project uses Python's database connection library to execute SQL queries using flask within the methods mentioned above.

## Running the Application
You can run the Flask API on localhost:5555 by executing:
python server/app.py
You can run the React application on localhost:4000 by executing:
npm start --prefix client

## Database Setup
1. Set the Flask application environment variable:
export FLASK_APP=server/app.py
2. Initialize the database:
flask db init
3. Apply the migrations:
flask db upgrade head
4. Seed the database with initial data:
python server/seed.py

## Technologies Used
- Python
- SQLAlchemy (ORM)
- SQLite (database)
- Flask-SQLAchemy

## Contributions
Contributions to the Superheroes application are welcome! 
If you have any suggestions, bug fixes, or additional features you'd like to add, please feel free to submit a pull request or open an issue.

## Acknowledgments
Inspiration

## Support
For support, email neema.ambuku@student.moringaschool.com


