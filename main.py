from user import User
from diet import Diet
from workout import Workout
from progress import Progress

def main():
    name = input("Enter your name: ")
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (cm): "))
    goal = input("Goal (gain/lose/maintain): ")

    user = User(name, weight, height, goal)

    user.show_details()

    # Diet
    diet = Diet(user)
    diet.suggest_diet()

    # Workout
    workout = Workout(goal)
    workout.generate_plan()

    # Progress
    progress = Progress()
    progress.add_record(weight)

    while True:
        choice = input("\nAdd new weight? (yes/no): ")
        if choice == "yes":
            new_weight = float(input("Enter new weight: "))
            progress.add_record(new_weight)
        else:
            break

    progress.show_progress()

if __name__ == "__main__":
    main()