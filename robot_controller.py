# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 18:59:22 2024

@author: Edwin
"""

# robot_controller.py
class RobotController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def procesar_comando(self, elevacion, giro, longitud):
        self.modelo.move_elevation(elevacion)
        self.modelo.move_rotation(giro)
        self.modelo.move_length(longitud)
        self.vista.mostrar_posicion(self.modelo)

    def run(self):
        while True:
            elevacion, giro, longitud = self.vista.get_user_input()
            if elevacion == 'stop' or giro == 'stop' or longitud == 'stop':
                self.modelo.stop_movement()
                print("Movimiento detenido.")
            else:
                self.procesar_comando(int(elevacion), int(giro), int(longitud))