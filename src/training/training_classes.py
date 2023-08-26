class WorkoutPlan:
    def __init__(self, input_name="", input_workouts=None, input_length=4):
        input_workouts = [Workout()] if input_workouts is None else input_workouts
        self.name = input_name
        self.workouts = input_workouts
        self.length_weeks = input_length

    def add_workout(self, input_workout):
        self.workouts.append(input_workout)

    def change_length(self, new_length):
        self.length_weeks = new_length


class Workout:
    def __init__(self, input_exercises=None, input_day="Monday"):
        input_exercises = [Exercise()] if input_exercises is None else input_exercises
        self.exercises = input_exercises
        self.day = input_day

    def add_exercise(self, input_exercise):
        self.exercises.append(input_exercise)

    def change_day(self, input_day):
        self.day = input_day


class Exercise:
    def __init__(self,input_name="", input_weight=0, input_sets=None, input_muscle_group="", input_rir=3):
        input_sets = [ExerciseSet()] if input_sets is None else input_sets
        self.name = input_name
        self.weight = float(input_weight)
        self.sets = input_sets
        self.muscle_group = input_muscle_group
        self.rir = int(input_rir)

    def increase_sets(self, number_of_sets=1):
        for i in range(number_of_sets):
            self.sets.append(ExcerciseSet(0))

    def change_weight(self, input_weight):
        # Calculate new number of reps using "The Brzycki Equation"
        # Will probably change this for loop into a function later
        # Need to add checks that weight change isn't too drastic, if it is set reps to 0
        # if self.reps is 0 do nothing
        for training_set in self.sets:
            reps_able_to_do = trianing_set.reps + self.rir
            one_rep_max = self.weight / (1.0278 - (0.0278 * reps_able_to_do))
            training_set.reps = int(round(0 - (((input_weight / one_rep_max) - 1.0278) / 0.0278) - 3))
        self.weight = input_weight

    def change_rir(self, new_rir=3):
        self.rir = new_rir


class ExerciseSet:
    def __init__(self, input_reps=0):
        self.reps = input_reps

    def change_reps(self, input_reps=1):
        self.reps += input_reps
