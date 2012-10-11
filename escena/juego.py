# -*- coding: utf-8 -*-
# Pong - version 0.1
#
# 2012 - Luciano Castillo & Franco Agresta
#

import pilas
from pilas.escenas import Escena
from actor import *


class Juego(Escena):
    '''Representa a la escena que se desarrolla en la ejecucion del juego.'''

    def __init__(self):
        '''Genera el entorno de la escena (fondo, actores, colisiones, eventos).'''
        Escena.__init__(self)
        self.crear_escenario()
        self.crear_colisiones()
        pilas.eventos.pulsa_tecla_escape.conectar(self.cuando_pulsa_tecla)
        self.termino_el_juego = False
        self.toco_lateral_izq = False
        self.toco_lateral_der = False
        pilas.eventos.actualizar.conectar(self.toca_lateral)

    def crear_escenario(self):
        '''Crea el escenario del juego (fondo, jugadores, puntajes).'''
        self.fondo = pilas.fondos.Fondo('escena/fondo/juego.png')
        self.pelota = Pelota()
        self.jugador1 = [Jugador1(x=-300, y=-45), Jugador1(x=-300, y=-15), Jugador1(x=-300, y=15), Jugador1(x=-300, y=45)]
        self.jugador2 = [Jugador2(x=300, y=-45), Jugador2(x=300, y=-15), Jugador2(x=300, y=15), Jugador2(x=300, y=45)]
        self.puntaje1 = Puntaje1()
        self.puntaje2 = Puntaje2()
        pilas.avisar(u'Ganará el primero en llegar a 7 puntos, ESC para salir')
        
    def crear_colisiones(self):
        '''Crea todas las colisiones del juego.'''
        def cuando_colisionan_1(pelota, jugador): # colision entre pelota y jugador 1
            pelota.x += 1
            pelota.circulo.impulsar(pelota.dx * 50000, pelota.dy * 50000)
            
        def cuando_colisionan_2(pelota, jugador): # colision entre pelota y jugador 2
            pelota.x -= 1
            pelota.circulo.impulsar(pelota.dx * -50000, pelota.dy * -50000)
            
        pilas.mundo.colisiones.agregar(self.pelota, self.jugador1, cuando_colisionan_1)
        pilas.mundo.colisiones.agregar(self.pelota, self.jugador2, cuando_colisionan_2)
        
    def toca_lateral(self, evento):
        '''Se encarga de los puntajes. Cuando la pelota llega a un lateral o al otro, suma los puntos correspondientes.'''
        if not self.termino_el_juego:
            if not self.toco_lateral_der:
                if self.pelota.x > 295:
                    a = int(self.puntaje1.obtener_texto())
                    
                    if a != 6:
                        self.puntaje1.definir_texto(str(a+1))
                    else:
                        self.puntaje1.definir_texto(str(a+1))
                        self.pelota.explotar()
                        pilas.avisar('Ganador: jugador 1')
                        texto = pilas.actores.Texto('Game Over !!!')
                        self.puntaje1.color = pilas.colores.verde
                        self.puntaje2.color = pilas.colores.rojo
                        self.termino_el_juego = True
                    self.toco_lateral_der = True
            if self.toco_lateral_der:
                if self.pelota.x < 295:
                    self.toco_lateral_der = False
                    
            if not self.toco_lateral_izq:
                if self.pelota.x < -295:
                    a = int(self.puntaje2.obtener_texto())
                
                    if a != 6:
                        self.puntaje2.definir_texto(str(a+1))
                    else:
                        self.puntaje2.definir_texto(str(a+1))
                        self.pelota.explotar()
                        pilas.avisar('Ganador: jugador 2')
                        texto = pilas.actores.Texto('Game Over !!!')
                        self.puntaje2.color = pilas.colores.verde
                        self.puntaje1.color = pilas.colores.rojo
                        self.termino_el_juego = True
                    self.toco_lateral_izq = True
            if self.toco_lateral_izq:
                if self.pelota.x > -295:
                    self.toco_lateral_izq = False
                    
    def cuando_pulsa_tecla(self, *k, **kv):
        '''Función ejecutada al pulsar <ESC>. Llama a la escena Menu().'''
        import menu
        menu.Menu()
