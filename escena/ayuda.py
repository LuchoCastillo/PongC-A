# -*- coding: utf-8 -*-
# Pong - version 0.1
#
# 2012 - Luciano Castillo & Franco Agresta
#

import pilas
from pilas.escena import Base


class Ayuda(Base):
    '''Representa a la escena que se desarrolla en la ayuda del juego. Además, informa sobre los controles del mismo.'''

    def __init__(self):
        '''Llama al __init__ de la escena "Base".'''
        Base.__init__(self)
        
    def iniciar(self):
        '''Genera todo el entorno de la escena (fondo, título, controles).'''
        self.fondo = pilas.fondos.Fondo('escena/fondo/ayuda.png')
        self.crear_texto_ayuda()
        pilas.eventos.pulsa_tecla_escape.conectar(self.cuando_pulsa_tecla)
        
    def crear_texto_ayuda(self):
        '''Función encargada de crear el texto de la ayuda (controles).'''
        titulo = pilas.actores.Texto('Controles', magnitud=30, y=200)
        titulo.color = pilas.colores.rojo
        texto1 = pilas.actores.Texto('Jugador 1 (rojo)', y=120, x=-120)
        texto2 = pilas.actores.Texto('Jugador 2 (azul)', y=120, x=120)
        pilas.avisar('Pulsa ESC para regresar al menu')

    def cuando_pulsa_tecla(self, *k, **kv):
        '''Se encarga de volver al menú inicial, al presionar <ESC>.'''
        pilas.recuperar_escena()
