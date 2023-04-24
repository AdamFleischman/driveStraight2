import math
class DriveStraight:
    def __init__(self, drivetrain, distance):
        self.drivetrain = drivetrain
        self.distance = distance

    def run(self):
        left_distance = self.drivetrain.left_encoder.getDistance()
        right_distance = self.drivetrain.right_encoder.getDistance()
        speed = .3
        adjustment = .3
        print(f"Left: {left_distance}, Right: {right_distance}")
        if left_distance > right_distance:
            self.drivetrain.move(-adjustment, speed)
        elif left_distance < right_distance:
            self.drivetrain.move(adjustment, speed)
        else:
            self.drivetrain.move(0, speed)
