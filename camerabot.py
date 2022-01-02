import logging
import sys
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

# 
#  Set up logging to go to journalctl.
# 
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(formatter)
logger.addHandler(handler)


class Camerabot:
    def __init__(self,motor="h"):
        logger.debug("The motor being used is "+ motor)
        self.kit = MotorKit()
        self.motor = self.kit.stepper1 if motor.lower() == "h" else self.kit.stepper2

    def down(self):
        logger.debug("^^^ going down! ^^^ ")
        self.motor.onestep(direction=stepper.BACKWARD,style=stepper.DOUBLE)

    def up(self):
        logger.debug("^^^ going up! ^^^ ")
        self.motor.onestep(direction=stepper.FORWARD,style=stepper.DOUBLE)

    def stop(self):
        logger.debug("^^^ stopped! ^^^")
        self.motor.release()