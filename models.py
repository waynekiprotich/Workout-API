from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

# Initialize the 
db = SQLAlchemy()

class Workout(db.Model):
    """Represents a single workout session."""
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)

    # Link to join table
    workout_exercises = db.relationship("WorkoutExercise", backref="workout", cascade="all, delete")

class Exercise(db.Model):
    """Represents a type of movement (e.g., Pushup, Squat)."""
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    category = db.Column(db.String, nullable=False)
    equipment_needed = db.Column(db.Boolean, default=False)

    # Link to join table
    workout_exercises = db.relationship("WorkoutExercise", backref="exercise", cascade="all, delete")

class WorkoutExercise(db.Model):
    """Association table linking Workouts and Exercises with specific performance data."""
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer, primary_key=True)

    # Foreign Keys linking to parent tables
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"), nullable=False)
    
    # Validation to ensure positive values for reps, sets, and duration
    reps = db.Column(db.Integer, nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    duration_seconds = db.Column(db.Integer)

    @validates("reps", "sets", "duration_seconds")
    def validate_positive(self, key, value):
        """Ensures that reps, sets, and duration are never negative values."""
        if value is not None and value < 0:
            raise ValueError(f"{key} must be positive")
        return value