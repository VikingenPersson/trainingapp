from training.training_classes import (
    WorkoutPlan,
    Workout,
    Exercise,
    ExerciseSet,
)
import os

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
    "Quads",
    "Hamstrings",
    "Calves",
)


def clear_terminal():
    os.system("clr||clear")


def select_day():
    print("Select one of the following days:")
    for day in range(len(available_days)):
        print(f"{day + 1}. {available_days[day]}")
    selected_day = input("Enter number: ")
    try:
        selected_day = int(selected_day) - 1
    except ValueError:
        print("Looks like you didn\'t enter a number, Try again.")
        selected_day = select_day()
    if selected_day < 0 or selected_day >= len(available_days):
        print("Looks like you entered a non existing day, Try again.")
        selected_day = select_day()
    return selected_day


def select_name_exercise():
    return input("Enter a name for the exercise: ")


def select_muscle_group():
    print("Select one of the following muscle groups")
    for muscle in range(len(available_muscle_groups)):
        print(f"{muscle + 1}. {available_muscle_groups[muscle]}")
    selected_muscle = input("Enter number: ")
    try:
        selected_muscle = int(selected_muscle) - 1
    except ValueError:
        print("Looks like you didn\'t enter a number, Try again.")
        selected_muscle = select_muscle_group()
    if selected_muscle < 0 or selected_muscle >= len(available_muscle_groups):
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
    input_name = select_name_exercise()
    input_muscle = available_muscle_groups[select_muscle_group()]
    number_of_sets = select_number_of_sets()
    list_of_sets = create_sets(number_of_sets)
    return Exercise(input_name=input_name, input_muscle_group=input_muscle, input_sets=list_of_sets)


def create_workout():
    day = available_days[select_day()]
    exercises = [create_exercise()]
    while True:
        another_exercise = input("Would you like to add another exercise? [y/N]: ").lower()
        if another_exercise == "y":
            exercises.append(create_exercise())
        elif another_exercise == "" or another_exercise == "n":
            break
        else:
            print("Please enter y for yes or n for no")
    return Workout(input_exercises=exercises, input_day=day)


def create_workout_plan():
    name = input("Enter a name for this workout plan: ")
    list_workouts = [create_workout()]
    while True:
        another_workout = input("Would you like to create another workout? [y/N]: ").lower()
        if another_workout == "y":
            list_workouts.append(create_workout())
        elif another_workout == "" or another_workout == "n":
            break
        else:
            print("Please enter y for yes or n for no")

    while True:
        while True:
            length_of_plan = input("How many weeks should this plan be for? [4-6]: ")
            try:
                length_of_plan = int(length_of_plan)
                break
            except ValueError:
                print("Looks like you didn\'t enter a number, try again.")

        if length_of_plan < 4 or length_of_plan > 6:
            print("please select a number between 4 and 6")
        else:
            break
    return WorkoutPlan(input_name=name, input_workouts=list_workouts, input_length=length_of_plan)


# Visual functions for printing in terminal

def print_set(input_set):
    print(f"reps:\t\t\t{input_set.reps}")


def print_exercise_detailed(input_exercise):
    print(f"Exercise:\t{input_exercise.name}\t{input_exercise.muscle_group}")
    print(f"Weight:\t{input_exercise.show_weight}\t|\trir={input_exercise.rir}")
    for wset in input_exercise.show_sets:
        print_set(wset)
    print__divider()


def print_workout(input_workout):
    print(f"Day:\t{input_workout.day}")
    print__divider()
    for exercise in input_workout.exercises:
        print_exercise_detailed(exercise)


def print_workout_plan(input_workout_plan):
    print__divider()
    print(f"Name:\t{input_workout_plan.name}\t|\tWeeks left:\t{input_workout_plan.length_weeks}")
    for workout in input_workout_plan.workouts:
        print_workout(workout)


def print__divider():
    print("-----------------------------------------------------------------------------------------------------------")


def exercise_eval(exercise, muscle_soreness=2):
    joint_pain = 1
    pump = 1
    training_intensity = 1
    while True:
        print("Did you feel any joint pain during the exercise?")
        print("1. No pain")
        print("2. A little pain")
        print("3. Moderate amount of pain")
        print("4. Alot of pain")
        choice = input("Select option: ")
        try:
            choice = int(choice)
        except ValueError:
            input("Wrong input press enter to try again: ")
            clear_terminal()
            continue
        if choice < 1 or choice > 4:
            input("Wrong input press enter to try again: ")
            clear_terminal()
        else:
            joint_pain = choice
            clear_terminal()
            break
    while True:
        print("How was you pump after the exercise?")
        print("1. no/low pump")
        print("2. Okay pump")
        print("3. Awesome pump")
        choice = input("Select option: ")
        try:
            choice = int(choice)
        except ValueError:
            input("Wrong input press enter to try again: ")
            clear_terminal()
            continue
        if choice < 1 or choice > 3:
            input("Wrong input press enter to try again: ")
            clear_terminal()
        else:
            pump = choice
            clear_terminal()
            break
    while True:
        print("How was the training intensity?")
        print("1. Easy")
        print("2. Pretty good")
        print("3. Pushed my limits")
        print("4. Too much")
        choice = input("Select option: ")
        try:
            choice = int(choice)
        except ValueError:
            input("Wrong input press enter to try again: ")
            clear_terminal()
            continue
        if choice < 1 or choice > 4:
            input("Wrong input press enter to try again: ")
            clear_terminal()
        else:
            training_intensity = choice
            clear_terminal()
            break
    if joint_pain > 3:
        exercise.change_weight(exercise.show_weight * 0.80, True)
    if training_intensity > 3:
        exercise.show_sets.pop()
    elif training_intensity < 2:
        exercise.show_sets.append(ExerciseSet())
    if pump <= 1 and muscle_soreness < 4:
        exercise.show_sets.append(ExerciseSet())
    if muscle_soreness > 3:
        exercise.show_sets.pop()
    elif muscle_soreness < 2:
        exercise.show_sets.append(ExerciseSet())


def muscle_soreness_eval(muscle_group):
    while True:
        print(f"How was the muscle soreness in your {muscle_group} after your last workout?")
        print("1. Never got sore")
        print("2. Recovered a while ago")
        print("3. Recovered just in time")
        print("4. Still sore")
        choice = input("Select option: ")
        try:
            choice = int(choice)
        except ValueError:
            input("Wrong input press enter to try again: ")
            clear_terminal()
            continue
        if choice < 1 or choice > 4:
            input("Wrong input press enter to try again: ")
            clear_terminal()
        else:
            clear_terminal()
            return choice


def main_menu(workout_plan):
    clear_terminal()
    print__divider()
    print("1. Start Workout\t2. Show Workout plan\t3. Edit Workout plan")
    print("4. Exit program")
    choice = int(input("Select option: "))
    if choice == 1:
        clear_terminal()
        start_workout(workout_plan)
    elif choice == 2:
        clear_terminal()
        print_workout_plan(workout_plan)
        input("Press enter to go back to main menu")
    elif choice == 3:
        print("Sorry that option isn\'t implemented yet.")
        input("Press enter to continue: ")
    elif choice == 4:
        exit()
    else:
        input("Wrong input press enter to try again: ")


def start_workout(workout_plan):
    current_workout = None
    while True:
        for workout in workout_plan.workouts:
            if not workout.finished:
                current_workout = workout
                break
        if current_workout is None:
            workout_plan.new_week()
        else:
            break
    muscle_groups_for_workout = []
    muscle_soreness_dic = {muscle: 2 for muscle in available_muscle_groups}
    for exercise in current_workout.exercises:
        if exercise.muscle_group not in muscle_groups_for_workout:
            muscle_groups_for_workout.append(exercise.muscle_group)

    for exercise in current_workout.exercises:
        if exercise.muscle_group in muscle_groups_for_workout and \
                workout_plan.length_weeks < workout_plan.original_length:
            clear_terminal()
            muscle_soreness = muscle_soreness_eval(exercise.muscle_group)
            muscle_soreness_dic[exercise.muscle_group] = muscle_soreness
            muscle_groups_for_workout.remove(exercise.muscle_group)
        while True:
            print_exercise_detailed(exercise)
            print(f"1. Change Weight\t2. Enter Reps for sets")
            choice = int(input("Select option: "))
            if choice == 1:
                exercise.change_weight(input_weight=int(input("Enter new weight: ")))
                clear_terminal()
                continue
            elif choice == 2:
                current_set = 1
                for wset in exercise.show_sets:
                    clear_terminal()
                    print_exercise_detailed(exercise)
                    wset.reps = int(input(f"Enter amount of reps you did for set {current_set}: "))
                    current_set += 1
                break
            else:
                input("Wrong input press enter to try again: ")
                clear_terminal()
        clear_terminal()
        exercise_eval(exercise, muscle_soreness_dic[exercise.muscle_group])
        exercise.finish_exercise()
    current_workout.finished = True
    workouts_finished = 0
    for workout in workout_plan.workouts:
        if workout.finished:
            workouts_finished += 1
    if workouts_finished == len(workout_plan.workouts):
        workout_plan.new_week()
