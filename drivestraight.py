class DriveStraight:
    def __init__(self, drivetrain, distance):
        self.drivetrain = drivetrain
        self.distance = distance

    def run(self):
        self.drivetrain.move(1, 0)
