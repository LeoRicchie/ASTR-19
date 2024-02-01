class SeaTurtle:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = float(arm_length)
        self.leg_length = float(leg_length)
        self.num_eyes = int(num_eyes)
        self.has_tail = bool(has_tail)
        self.is_furry = bool(is_furry)

    def describe(self):
        print("Physical Characteristics of a Sea Turtle:")
        print(f"Arm Length: {self.arm_length} cm")
        print(f"Leg Length: {self.leg_length} cm")
        print(f"Number of Eyes: {self.num_eyes}")
        print(f"Has Tail: {'Yes' if self.has_tail else 'No'}")
        print(f"Is Furry: {'Yes' if self.is_furry else 'No'}")


# Example usage:
my_sea_turtle = SeaTurtle(120, 75, 2, True, False)
my_sea_turtle.describe()

