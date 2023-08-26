from training.training_classes import (
    WorkoutPlan,
    Workout,
    Exercise,
    ExerciseSet
)
from training.training_functions import create_workout_plan, clear_terminal
import atexit
import dill


def exit_handler(workouts_to_save):
    save_to_file(workouts_to_save)


def save_to_file(workout):
    with open("saves/workout_plans.pkl", "wb") as save_file:
        dill.dump(workout, save_file)


def load_from_file():
    with open("saves/workout_plans.pkl", "rb") as load_file:
        return dill.load(load_file)


def first_workout_plan():
    print("Looks like you don\'t have a workout plan yet, lets create one")
    return create_workout_plan()


def main():
    workout_plans = []
    atexit.register(exit_handler, workout_plans)
    try:
        workout_plans_list = load_from_file()
        for workout_plan in workout_plans_list:
            workout_plans.append(workout_plan)
        del workout_plans_list
    except FileNotFoundError:
        workout_plans.append(first_workout_plan())
    if not workout_plans:
        workout_plans.append(first_workout_plan())
    input("Press enter to exit")


if __name__ == "__main__":
    main()
