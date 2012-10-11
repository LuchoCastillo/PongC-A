# -*- coding: utf-8 -*-
# Pong - version 0.1
#
# 2012 - Luciano Castillo & Franco Agresta
#

"""
Módulo escena
=============

Este módulo representa las tres escenas del juego:

    1. :Escena Menu: en la cual se despliega el menú de opciones. Es la escena inicial.
    2. :Escena Ayuda: en la cual se presentan los mandos de cada jugador.
    3. :Escena Juego: en la cual se desarrolla el juego. Allí están presentes todos los actores que participan.

Se puede invocar una escena de este modo:

    >>> from pong import escena
    >>> escena_actual = escena.Juego()
"""

from menu import Menu
from ayuda import Ayuda
from juego import Juego
