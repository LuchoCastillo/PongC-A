# -*- coding: utf-8 -*-
# Pong - version 0.1
#
# 2012 - Luciano Castillo & Franco Agresta
#

import pilas
from pilas.actores import Actor
from pilas.habilidades import Habilidad, SeMantieneEnPantalla
from pilas.simbolos import *


class Jugador1(Actor):
    '''Representa a la barra roja del juego'''

    def __init__(self, x=0, y=0):
        '''Genera el actor, carga la imágen y su radio, y le enseña sus habilidades.'''
        Actor.__init__(self, x=x, y=y)
        self.imagen = pilas.imagenes.cargar('escena/actor/base/roja.bmp')
        self.radio_de_colision = 15
        self.aprender(SeMantieneEnPantalla)
        self.aprender(self.MoverseConWS)
        
        
    class MoverseConWS(Habilidad):
        '''
        Habilidad que hace que un actor se pueda mover con las teclas:
        
            W --> arriba
            S --> abajo
        
        Facilita el uso de un segundo mando, muy usado en juegos multiplayer
        '''

        def __init__(self, receptor):
            '''Genera los eventos necesarios para el mando.'''
            Habilidad.__init__(self, receptor)
            self.w = False
            self.s = False
            pilas.eventos.actualizar.conectar(self.pulsa_tecla)
            pilas.eventos.pulsa_tecla.conectar(self.cuando_pulsa_la_tecla)
            pilas.eventos.suelta_tecla.conectar(self.cuando_suelta_la_tecla)
            
        def pulsa_tecla(self, evento):
            '''Mueve al jugador según se haya pulsado o despulsado una tecla.'''
            velocidad = 5

            if self.w:
                self.receptor.y += velocidad
            elif self.s:
                self.receptor.y -= velocidad
                
        def cuando_pulsa_la_tecla(self, evento):
            '''Evento causado por la pulsación de una tecla.'''
            self.procesar_cambio_de_estado_en_la_tecla(evento.codigo, True)

        def cuando_suelta_la_tecla(self, evento):
            '''Evento causado por la despulsación de una tecla.'''
            self.procesar_cambio_de_estado_en_la_tecla(evento.codigo, False)
                
        def procesar_cambio_de_estado_en_la_tecla(self, codigo, estado):
            '''Evento encargado de procesar el cambio de estado según el parámetro recibido.'''
            mapa = {
                w: 'w',
                s: 's',
            }

            if mapa.has_key(codigo):
                setattr(self, mapa[codigo], estado)

