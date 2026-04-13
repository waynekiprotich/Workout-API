# Workout API
A Flask REST API for managing workouts and exercises 

---

# Project Overview
This API is designed for personal trainers to:

- Create workouts
- Create exercises
- Assign exercises to workouts
- Track sets, reps, and duration
- View structured workout data

Built using:
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Marshmallow

---

## Database Diagram

![Database Diagram](![Database Diagram](public/db_image.png))

# Setup Instructions

## 1. Clone the Repository

```bash
git clone https://github.com/waynekiprotich/Workout-API.git
cd Workout-API
```

## 2. Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
```
## 3. Install Dependencies

```bash
pip install -r requirements.txt
```
## 4. Set Up Database

```bash
flask --app app db init
flask --app app db migrate -m "initial migration"
flask --app app db upgrade
```
## 5. Seed the Database

```bash
python seed.py
```

## 6. Run the Application

```bash
flask --app app run
```

The API will be available at:

```bash
http://127.0.0.1:5000
```
## API Endpoints

Workouts
	•	GET /workouts → Get all workouts
	•	GET /workouts/<id> → Get single workout
	•	POST /workouts → Create workout
	•	DELETE /workouts/<id> → Delete workou

 Exercises
	•	GET /exercises → Get all exercises
	•	GET /exercises/<id> → Get single exercise
	•	POST /exercises → Create exercise
	•	DELETE /exercises/<id> → Delete exercise

## Author
Workout API built using Flask, SQLAlchemy, and Marshmallow.