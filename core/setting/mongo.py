import os
from motor.motor_tornado import MotorClient

def settings():
    return MotorClient(os.environ.get('MONGO_URI'))
