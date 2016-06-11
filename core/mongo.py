from motor.motor_tornado import MotorClient

def mongo_configurations(config):
    return MotorClient(config.get('MONGO_URI'))
