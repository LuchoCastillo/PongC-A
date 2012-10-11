# -*- coding: utf-8 -*-
# Pong - version 0.1
#
# 2012 - Luciano Castillo & Franco Agresta
#

import pilas
from pilas.actores import Bomba


class Pelota(Bomba):
    '''Representa a la pelota del juego'''

    def __init__(self, x=0, y=0):
        '''Genera a la bomba y le asigna el círculo de física.'''
        Bomba.__init__(self, x=x, y=y)
        self.crear_circulo(x, y)
        self._empujar()

    def crear_circulo(self, x, y):
        '''Crea el círculo de física con todas sus propiedades y se lo asigna a la pelota.'''
        self.circulo = pilas.fisica.Circulo(x, y, 20, restitucion=1, friccion=0, amortiguacion=0)
        self.imitar(self.circulo)

    def _empujar(self):
        '''Esta función es la encargada de comenzar con el movimiento de la bomba al inicio del juego.'''
        self.dx = 1
        self.dy = 1
        self.circulo.impulsar(self.dx * 50000, self.dy * 50000)

