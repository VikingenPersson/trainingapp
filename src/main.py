from training.training_classes import (
    WorkoutPlan,
    Workout,
    Exercise,
    ExerciseSet
)
from training.training_functions import select_day

workout_plans = []
available_days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)

while True:
    if not workout_plans:
        print("Looks like you don\'t have a workout plan yet, lets create one!")
        selected_day = select_day()

