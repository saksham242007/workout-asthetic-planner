class Workout:
    def __init__(self, goal):
        self.goal = goal

    def generate_plan(self):
        print("\nWorkout Plan:")

        if self.goal == "gain":
            print("Day 1: Chest + Triceps")
            print("Day 2: Back + Biceps")
            print("Day 3: Legs")
            print("Day 4: Shoulders")
        elif self.goal == "lose":
            print("Day 1: Full Body + Cardio")
            print("Day 2: HIIT")
            print("Day 3: Core + Cardio")
        else:
            print("Basic Strength Training 3x/week")