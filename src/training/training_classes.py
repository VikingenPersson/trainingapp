import copy

rir_template = (3, 2, 2, 1, 1, 0)


class WorkoutPlan:
    def __init__(self, input_name="", input_workouts=None, input_length=4):
        input_workouts = [Workout()] if input_workouts is None else input_workouts
        self.name = input_name
        self.workouts = input_workouts
        self.length_weeks = input_length
        self.original_length = input_length

    def add_workout(self, input_workout):
        self.workouts.append(input_workout)

    def change_length(self, new_length):
        self.length_weeks = new_length

    def new_week(self):
        self.change_length(self.length_weeks - 1)
        if self.length_weeks <= 0:
            self.length_weeks = self.original_length
        for workout in self.workouts:
            workout.finished = False
            for exercise in workout.exercises:
                exercise.rir = rir_template[6 - self.length_weeks]


class Workout:
    def __init__(self, input_exercises=None, input_day="Monday"):
        input_exercises = [Exercise()] if input_exercises is None else input_exercises
        self.exercises = input_exercises
        self.day = input_day
        self.finished = False

    def add_exercise(self, input_exercise):
        self.exercises.append(input_exercise)

    def change_day(self, input_day):
        self.day = input_day


class Exercise:
    def __init__(self, input_name="", input_weight=0, input_sets=None, input_muscle_group="", input_rir=3):
        input_sets = [ExerciseSet()] if input_sets is None else input_sets
        self.name = input_name
        self.target_weight = float(input_weight)
        self.target_sets = input_sets
        self.muscle_group = input_muscle_group
        self.rir = int(input_rir)
        self.show_sets = copy.deepcopy(self.target_sets)
        self.show_weight = self.target_weight

    def increase_sets(self, number_of_sets=1):
        for i in range(number_of_sets):
            self.target_sets.append(ExcerciseSet(0))

    def change_weight(self, input_weight):
        # Calculate new number of reps using "The Brzycki Equation"
        # Need to add checks that weight change isn't too drastic, if it is set reps to 0
        if input_weight == self.target_weight:
            self.reset_show_sets()
            self.show_weight = self.target_weight
        elif self.target_weight == 0:
            self.show_weight = input_weight
        elif input_weight != self.show_weight:
            for set_id in range(len(self.target_sets)):
                reps_able_to_do = self.target_sets[set_id].reps + self.rir
                one_rep_max = self.target_weight / (1.0278 - (0.0278 * reps_able_to_do))
                new_reps = int(round(0 - (((input_weight / one_rep_max) - 1.0278) / 0.0278) - 3))
                if new_reps == self.target_sets[set_id].reps:
                    new_reps += 1
                elif new_reps <= 0:
                    new_reps = 0
                self.show_sets[set_id].reps = new_reps
            self.show_weight = input_weight

    def reset_show_sets(self):
        self.show_sets = copy.deepcopy(self.target_sets)

    def finish_exercise(self):
        self.target_sets = copy.deepcopy(self.show_sets)
        self.target_weight = self.show_weight

    def change_rir(self, new_rir=3):
        self.rir = new_rir


class ExerciseSet:
    def __init__(self, input_reps=0):
        self.reps = input_reps

    def change_reps(self, input_reps=1):
        self.reps += input_reps
