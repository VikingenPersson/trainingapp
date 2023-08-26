from training_classes import (
    WorkoutPlan,
    Workout,
    Exercise,
    ExerciseSet,
)

available_days = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    )

available_muscle_groups = (
        "Chest",
        "Back",
        "Shoulders",
        "Biceps",
        "Triceps",
        "Abs",
        "Quads"
        "Hamstrings",
        "Calves",
    )

def select_day():
    print("Select one of the following days:")
    for day in range(len(available_days)):
        print(f"{day + 1}. {available_days[day]}")
    selected_day = input("Enter number: ")
    try:
        selected_day = int(selected_day)-1
    except ValueError:
        print("Looks like you didn\'t enter a number, Try again.")
        selected_day = select_day()
    if selected_day < 1 or selected_day >= len(available_days):
        print("Looks like you entered a non existing day, Try again.")
        selected_day = select_day()
    return selected_day

def select_name():
    return input("Enter a name for the exercise: ")

def select_muscle_group():
    for muscle in range(len(available_muscle_groups)):
        print(f"{muscle+1}. {available_muscle_groups[muscle]}")
    selected_muscle = input("Enter number: ")
    try:
        selected_muscle = int(selected_muscle)-1
    except ValueError:
        print("Looks like you didn\'t enter a number, Try again.")
        selected_muscle = select_muscle_group()
    if selected_muscle < 1 or selected_muscle >= len(available_muscle_groups):
        print("Looks like the muscle group you entered doesn\'t exist, Try again.")
        selected_muscle = select_muscle_group()
    return selected_muscle

def create_sets(number_of_sets):
    list_of_sets = []
    for i in range(number_of_sets):
        list_of_sets.append(ExerciseSet())
    return list_of_sets

def select_number_of_sets():
    number_of_sets = input("Enter amount of sets for this exercise: ")
    try:
        number_of_sets = int(number_of_sets)
    except ValueError:
        print("Looks like you didn\'t enter a number, try again.")
        number_of_sets = select_number_of_sets()
    return number_of_sets

def create_exercise():
    input_name = select_name()
    input_muscle = available_muscle_groups[select_muscle_group()]
    number_of_sets = select_number_of_sets()
    list_of_sets = create_sets(number_of_sets)
    return Exercise(input_name=input_name, input_muscle_group=input_muscle, input_sets=list_of_sets)
