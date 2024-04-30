# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 18:59:38 2024

@author: Edwin
"""

# main.py
from robot_model import RobotModel
from robot_view import RobotView
from robot_controller import RobotController

modelo = RobotModel()
vista = RobotView()
controlador = RobotController(modelo, vista)

controlador.run()