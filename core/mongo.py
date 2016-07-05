import os
from motor.motor_tornado import MotorClient

def mongo_configurations():
    return MotorClient(os.environ.get('MONGO_URI'))
