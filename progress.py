class Progress:
    def __init__(self):
        self.records = []

    def add_record(self, weight):
        self.records.append(weight)

    def show_progress(self):
        print("\nProgress History:")
        for i, w in enumerate(self.records):
            print(f"Week {i+1}: {w} kg")