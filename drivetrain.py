from wpilib import Spark, Encoder
from wpilib.drive import DifferentialDrive
import math
# help from Eric about what method to use and how to set the tick
class Drivetrain:
    def __init__(self):
        self.left_encoder = Encoder(4,5)
        self.right_encoder = Encoder(6,7)
        self.left_motor = Spark(0)
        self.right_motor = Spark(1)
        self.drivetrain = DifferentialDrive(self.left_motor, self.right_motor)
        self.left_encoder.setDistancePerPulse(0.07*math.pi/(12*120))
        self.right_encoder.setDistancePerPulse(0.07 * math.pi / (12 * 120))

    def move(self, forward, rotate):

        self.drivetrain.arcadeDrive(rotate, forward)

    def checkEncoders(self):
        return f"Left: {self.left_encoder.getDistance()}\nRight: {self.right_encoder.getDistance()}"

