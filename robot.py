from drivetrain import Drivetrain
from wpilib import Joystick
import os
import wpilib
from wpilib import TimedRobot


class MyRobot(TimedRobot):  # this is the controller
    def robotInit(self):  # something
        self.controller = Joystick(0)
        self.drivetrain = Drivetrain()

    def teleopPeriodic(self):
        forward = self.controller.getRawAxis(0)
        rotate = self.controller.getRawAxis(1)
        self.drivetrain.move(forward, rotate)
        self.linefollower.run()
        # pull controller
        # invoke drivetrain, move


if __name__ == "__main__":
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"

    wpilib.run(MyRobot)
