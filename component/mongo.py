import os
from motor.motor_tornado import MotorClient
from core.component import Component

class Mongo(Component):

    def __init__(self):
        self._motor = None

    def install(self):
        self._motor = MotorClient(os.environ.get('MONGO_URI'))

    def initialize(self):
        return self._motor
