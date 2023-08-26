from training.training_classes import (
    WorkoutPlan,
    Workout,
    Exercise,
    ExerciseSet
)
from training.training_functions import create_workout_plan, clear_terminal
import atexit
import dill


def exit_handler():
    save_to_file(workout_plans)


atexit.register(exit_handler)


def save_to_file(workout):
    with open("workout_plans.pkl", "wb") as save_file:
        dill.dump(workout, save_file)


workout_plans = []


def main(input_plans):
    workout_plans_main = input_plans
    try:
        with open("workout_plans.pkl", "rb") as load_file:
            workout_plans_main = dill.load(load_file)
    except FileNotFoundError:
        print("Looks like you don\'t have a workout plan yet, lets create one")
        workout_plans_main.append(create_workout_plan())
    if not workout_plans_main:
        print("Looks like you don\'t have a workout plan yet, lets create one")
        workout_plans_main.append(create_workout_plan())
    print(workout_plans_main[0].workouts[0].exercises[0].name)
    input("Press enter to exit")


main(workout_plans)
