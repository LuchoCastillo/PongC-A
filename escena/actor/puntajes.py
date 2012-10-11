# -*- coding: utf-8 -*-
# Pong - version 0.1
#
# 2012 - Luciano Castillo & Franco Agresta
#

import pilas
from pilas.actores import Puntaje


class Puntaje1(Puntaje):
    '''Representa el puntaje del jugador rojo'''

    def __init__(self, x=-70, y=210):
        '''Crea el puntaje y le asigna un color y una escala (tamaño).'''
        Puntaje.__init__(self, x=x, y=y)
        self.color = pilas.colores.blanco
        self.escala = 1.75
        
        
class Puntaje2(Puntaje):
    '''Representa el puntaje del jugador azul'''

    def __init__(self, x=70, y=210):
        '''Crea el puntaje y le asigna un color y una escala (tamaño).'''
        Puntaje.__init__(self, x=x, y=y)
        self.color = pilas.colores.blanco
        self.escala = 1.75
