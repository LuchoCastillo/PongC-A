#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Pong - version 0.1
#
# 2012 - Luciano Castillo & Franco Agresta
#

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
