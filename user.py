class User:
    def __init__(self, name, weight, height, goal):
        self.name = name
        self.weight = weight
        self.height = height
        self.goal = goal  # gain / lose / maintain

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Weight: {self.weight} kg")
        print(f"Height: {self.height} cm")
        print(f"Goal: {self.goal}")