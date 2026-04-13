from app import app
from models import db, Workout, Exercise, WorkoutExercise
from datetime import date

with app.app_context():
    db.drop_all()
    db.create_all()

    w1 = Workout(date=date.today(), duration_minutes=60, notes="Chest day")
    w2 = Workout(date=date.today(), duration_minutes=45, notes="Leg day")

    e1 = Exercise(name="Push Ups", category="Strength", equipment_needed=False)
    e2 = Exercise(name="Squats", category="Strength", equipment_needed=False)

    db.session.add_all([w1, w2, e1, e2])
    db.session.commit()

    we1 = WorkoutExercise(workout_id=w1.id, exercise_id=e1.id, reps=10, sets=3)
    we2 = WorkoutExercise(workout_id=w2.id, exercise_id=e2.id, reps=12, sets=4)

    db.session.add_all([we1, we2])
    db.session.commit()

print("Seed complete")