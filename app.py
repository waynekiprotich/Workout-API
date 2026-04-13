from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Workout, Exercise, WorkoutExercise
from schemas import WorkoutSchema, ExerciseSchema, WorkoutExerciseSchema

app = Flask(__name__)

# CONFIGURATION
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# INITIALIZATION
db.init_app(app)
migrate = Migrate(app, db)

# SCHEMAS
workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)
exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)
workout_exercise_schema = WorkoutExerciseSchema()

@app.route("/")
def home():
    return {"message": "Workout API running 🚀"}

# WORKOUT ROUTES
@app.route("/workouts", methods=["GET"])
def get_workouts():
    workouts = Workout.query.all()
    return jsonify(workouts_schema.dump(workouts))


@app.route("/workouts/<int:id>", methods=["GET"])
def get_workout(id):
    workout = Workout.query.get_or_404(id)
    return jsonify(workout_schema.dump(workout))


@app.route("/workouts", methods=["POST"])
def create_workout():
    data = request.get_json()

    workout = Workout(
        date=data["date"],
        duration_minutes=data["duration_minutes"],
        notes=data.get("notes")
    )

    db.session.add(workout)
    db.session.commit()

    return jsonify(workout_schema.dump(workout)), 201


@app.route("/workouts/<int:id>", methods=["DELETE"])
def delete_workout(id):
    workout = Workout.query.get_or_404(id)

    db.session.delete(workout)
    db.session.commit()

    return jsonify({"message": "Workout deleted"})


# EXERCISE ROUTES
@app.route("/exercises", methods=["GET"])
def get_exercises():
    exercises = Exercise.query.all()
    return jsonify(exercises_schema.dump(exercises))


@app.route("/exercises/<int:id>", methods=["GET"])
def get_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    return jsonify(exercise_schema.dump(exercise))


@app.route("/exercises", methods=["POST"])
def create_exercise():
    data = request.get_json()

    exercise = Exercise(
        name=data["name"],
        category=data["category"],
        equipment_needed=data["equipment_needed"]
    )

    db.session.add(exercise)
    db.session.commit()

    return jsonify(exercise_schema.dump(exercise)), 201


@app.route("/exercises/<int:id>", methods=["DELETE"])
def delete_exercise(id):
    exercise = Exercise.query.get_or_404(id)

    db.session.delete(exercise)
    db.session.commit()

    return jsonify({"message": "Exercise deleted"})



# JOIN TABLE ROUTES
@app.route("/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises", methods=["POST"])
def add_exercise_to_workout(workout_id, exercise_id):
    data = request.get_json()

    workout_exercise = WorkoutExercise(
        workout_id=workout_id,
        exercise_id=exercise_id,
        reps=data["reps"],
        sets=data["sets"],
        duration_seconds=data.get("duration_seconds", 0)
    )

    db.session.add(workout_exercise)
    db.session.commit()

    return jsonify(workout_exercise_schema.dump(workout_exercise)), 201

if __name__ == "__main__":
    app.run(port=5555, debug=True)