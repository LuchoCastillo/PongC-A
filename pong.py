#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Pong - version 0.1
#
# 2012 - Luciano Castillo & Franco Agresta
#

'''
Pong - C&A
==========

Este juego es una versión personalizada del famoso juego "Pong", realizada en el 2012 por Luciano Castillo y Franco Agresta (programadores del ITS Villada, córdoba capital).

Consiste en dos barras verticalmente ubicadas en los laterales y controladas por dos mandos diferentes (multijugador: 2 jugadores).


Objetivo
--------

El objetivo del juego es sumar 7 puntos a favor antes de que lo haga el otro jugador.

Al finalizar el juego, se deberá pulsar <ESC> para regresar al menú.


Acerca de...
------------

    Versión   -> 0.1
    Licencia  -> Copyleft
    Creador   -> Luciano Castillo & Franco Agresta
    Profesión -> Estudiantes de programación del ITS Villada
    Provincia -> Córdoba
    Localidad -> Córdoba capital
    Website   -> https://github.com/LuchoCastillo/PongC-A


Contacto
--------

Por cualquier duda o sugerencia enviar un mail a:

    lucho.castillo97@gmail.com
'''

import pilas
import escena


class Pong:
    '''Clase que llama a la escena menú para que comience el juego.'''
    
    def __init__(self):
        '''Inicia pilas con título "Pong", y gravedad 0.'''
        pilas.iniciar(titulo='Pong', gravedad=(0, 0))
        self.empezar()
        
    def empezar(self):
        '''Ejecuta la clase "Menu".'''
        escena.Menu()
        pilas.ejecutar()
        

if __name__ == '__main__':
    '''El juego será ejecutado solo si se abre este achivo, al ser llamado por otro habrá que ejecutar la clase:
    
    >>> import pong
    >>> pong.Pong()
    '''
    Pong()
