# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 18:58:25 2024

@author: Edwin
"""

# robot_model.py
class RobotModel:
    def __init__(self):
        self.elevacion = 0
        self.giro = 0
        self.longitud = 0

    def move_elevation(self, elevacion):
        self.elevacion = elevacion

    def move_rotation(self, giro):
        self.giro = giro

    def move_length(self, longitud):
        self.longitud = longitud

    def stop_movement(self):
        self.elevacion = 0
        self.giro = 0
        self.longitud = 0
