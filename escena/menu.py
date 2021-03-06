# -*- coding: utf-8 -*-
# Pong - version 0.1
#
# 2012 - Luciano Castillo & Franco Agresta
#

import pilas
from pilas.escena import Base


class Menu(Base):
    '''Escena inicial donde se desarrolla el menú del juego.'''

    def __init__(self):
        '''Llama al __init__ de la escena "Base".'''
        Base.__init__(self)
        
    def iniciar(self):
        '''Genera el entorno de la escena (fondo, título, menú).'''
        self.fondo = pilas.fondos.Fondo('escena/fondo/menu.png')
        self.generar_titulo()
        pilas.avisar('Use el teclado para cambiar o seleccionar opciones')
        self.generar_menu()

    def generar_titulo(self):
        '''Crea el título y le asigna un tamaño y un color.'''
        texto = pilas.actores.Texto('Pong', magnitud=45, y=200)
        texto.color = pilas.colores.rojo

    def generar_menu(self):
        '''Crea el menú con sus respectivas opciones.'''
        opciones = [
		            ('Empezar a jugar', self.comenzar),
		            ('Ver ayuda', self.ayuda),
		            ('Salir', self.salir),
		           ]
        self.menu = pilas.actores.Menu(opciones)

    def comenzar(self):
        '''Se ejecuta cuando se presiona "Empezar a jugar", llama a la clase Juego().'''
        import juego
        pilas.almacenar_escena(juego.Juego())

    def ayuda(self):
        '''Se ejecuta cuando se presiona "Ver ayuda", llama a la clase Ayuda().'''
        import ayuda
        pilas.almacenar_escena(ayuda.Ayuda())

    def salir(self):
        '''Se ejecuta cuando se presiona "Salir", cierra el programa.'''
        pilas.terminar()
