# -*- coding: utf-8 -*-
# Pong - version 0.1
#
# 2012 - Luciano Castillo & Franco Agresta
#

import pilas
from pilas.actores import Actor
from pilas.habilidades import Habilidad, SeMantieneEnPantalla


class Jugador2(Actor):
    '''Representa a la barra azul del juego'''

    def __init__(self, x=0, y=0):
        '''Genera el actor, carga la imágen y su radio, y le enseña sus habilidades.'''
        Actor.__init__(self, x=x, y=y)
        self.imagen = pilas.imagenes.cargar('escena/actor/base/azul.bmp')
        self.radio_de_colision = 15
        self.aprender(SeMantieneEnPantalla)
        self.aprender(self.MoverseConArribaAbajo)
        
        
    class MoverseConArribaAbajo(Habilidad):
        '''Hace que un actor se pueda mover con las teclas direccionales <ARRIBA> y <ABAJO>'''
    
        def __init__(self, receptor):
            '''Genera el evento necesario para el mando.'''
            Habilidad.__init__(self, receptor)
            pilas.eventos.actualizar.conectar(self.pulsa_tecla)
        
        def pulsa_tecla(self, evento):
            '''Mueve al jugador según se haya pulsado o despulsado una tecla.'''
            velocidad = 5
            c = pilas.escena_actual().control

            if c.arriba:
                self.receptor.y += velocidad
            elif c.abajo:
                self.receptor.y -= velocidad
            
    
