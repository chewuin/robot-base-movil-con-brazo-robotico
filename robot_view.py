# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 18:59:02 2024

@author: Edwin
"""

# robot_view.py
class RobotView:
    def mostrar_posicion(self, modelo):
        print(f"Posición actual del robot: Elevación={modelo.elevacion}, Giro={modelo.giro}, Longitud={modelo.longitud}")

    def get_user_input(self):
        elevacion = input("Introduce el valor de elevación: ")
        giro = input("Introduce el valor de giro: ")
        longitud = input("Introduce el valor de longitud: ")
        return elevacion, giro, longitud