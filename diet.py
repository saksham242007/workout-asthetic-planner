class Diet:
    def __init__(self, user):
        self.user = user

    def calculate_calories(self):
        # simple formula
        calories = self.user.weight * 30

        if self.user.goal == "gain":
            calories += 300
        elif self.user.goal == "lose":
            calories -= 300

        return calories

    def suggest_diet(self):
        calories = self.calculate_calories()

        print(f"\nDaily Calories Needed: {calories} kcal")

        if self.user.goal == "gain":
            print("Diet Plan:")
            print("- Oats + Milk + Banana")
            print("- Rice + Chicken/Paneer")
            print("- Peanut Butter Sandwich")
        elif self.user.goal == "lose":
            print("Diet Plan:")
            print("- Oats + Fruits")
            print("- Roti + Vegetables")
            print("- Salad + Protein")
        else:
            print("Balanced Diet Recommended")