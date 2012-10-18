================
Actores y fondos
================

Actores
-------

Un concepto importante en pilas es del de actores.

.. topic:: Actor:
    
    **Un actor** en pilas **es un objeto que aparece en pantalla, tiene una posición determinada y se puede manipular**.

Por ejemplo:
    
* Una nave.
* Un ingeniero.
* Una zanahoria.
    
.. image:: imagenes/pilas-actores.png
    :align: center
    
Para empezar, pilas se puede usar directamente desde un intérprete interactivo de python. Una vez dentro del intérprete, tienes que escribir estas dos líneas de código:

.. code-block:: python
    :linenos:
    
    import pilas         # importa la librería pilas
    pilas.iniciar()      # inicia una ventana predeterminada


En tu pantalla tiene que aparecer una ventana de color gris.

Para ver un ejemplo de actor podemos ingresar (luego de haber generado la vetana con las líneas anteriores):

.. code-block:: python
    :linenos:
    
    bomba = pilas.actores.Bomba()         # le asignamos a "bomba" el actor "Bomba()", ubicado en pilas.actores.


Se va a crear inmediatamente una bomba, en la ventana, como ésta:

.. image:: imagenes/pilas-bomba.png
    :align: center

Como Bomba es un actor, encontraremos mucha funcionalidad en él que la tendrán el resto de los actores.

Por ejemplo:


Posición
********

Podemos cambiar la posición del actor en el eje de cordenadas mediante las propiedades x e y:

.. code-block:: python
    :linenos:
    
    bomba.x = 100
    bomba.y = 100

Se puede observar si pulsas la tecla F12, la posición de los actores en el eje, de esta forma:

.. image:: imagenes/pilas-bomba100-100.png
    :align: center
    

Escala
******

Este atributo indica su tamaño en pantalla:

.. code-block:: python
    :linenos:
    
    bomba.escala = 2         # le duplicamos el tamaño a "bomba"
    
.. image:: imagenes/pilas-bomba-duplicada.png
    :align: center


Rotación
********

La rotación siempre se indica en grados, e indica el grado de inclinación hacia la derecha:

.. code-block:: python
    :linenos:
    
    bomba.rotacion = 45

.. image:: imagenes/pilas-bomba-rotada.png
    :align: center


Eliminar actor
**************

Para eliminar un actor basta con llamar a la función eliminar():

.. code-block:: python
    :linenos:

    bomba.eliminar()


Fondos
------

Otro concepto a aprender es el de fondos.

.. topic:: Fondo:
    
    En pilas **un fondo es** un concepto muy simple, es solamente **una imágen detras de mis actores, que suele ser un paisaje**.

Por ejemplo:

.. code-block:: python
    :linenos:
    
    fondo = pilas.fondos.Tarde()

.. image:: imagenes/pilas-fondo.png
    :align: center

Bueno, después de esta primera parte ya vamos a poder probar muchas cosas, pero ya que esta guía está destinada a un determinado juego, para conocer más y poder aplicarlo consulten al manual.

A partir de ahora solo vamos a ver lo necesario para nuestro "Pong".
