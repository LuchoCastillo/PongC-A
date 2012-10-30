.. Tutorial Pong-C&A documentation master file, created by
   sphinx-quickstart on Wed Oct 10 23:18:07 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

¿Cómo hacer un Pong?
====================

<style type="text/css">
body {
   background-color:white;
}

#stage {
	background-color:black;
}

p,#puntaje,#score_container {
	color:black;
}

p,#puntaje,#score_container {
	color:black;
}


</style>
<script src='google.js' type='text/javascript'></script>
<script type="text/javascript">

//DECLARAMOS VARIABLES GLOBALES QUE UTILIZAREMOS

//Variable de pausa
var pausado=false;

//Variables de "A"
var x=10; //eje x
var y=115; // eje y
var dy=0;

//Variables de "B"
var w=580; //eje x
var z=115; // eje y
var dz=0;

//Variables de pelota
var m=110; //eje x
var n=145; // eje y
var dm=10;
var dn=0;
var diago=0;

//Variables de puntaje
var puntajeA=0;
var puntajeB=0;

//Funcion de inicio llamada a travez del boton Comenzar puesto en el Body
function init() {
	//se inicia la funcion, llamamos el canvas del body y lo contextualizamos para usar 2d
	myCanvas = document.getElementById("stage");
	context= myCanvas.getContext('2d');
	context.fillStyle = 'white';
	//se ejecutaran las funciones drawA, drawB y pelota en intervalos de 100
	setInterval(drawA,100);
	setInterval(drawB,100);
	setInterval(pelota,100);
	}

//jugador "A" primera funcion llamada a ejecutarse
function drawA() {
	context.clearRect (0,0, 600,300);//limpiamos pantalla
	//dibujamos jugador A
	context.beginPath();
	context.fillRect(x,y,10,70);
	context.closePath();
	context.fill();
	//aumentamos dx y dy a los respectivos ejes segun las teclas de control de la funcion control() de esa manera simulamos movimiento
	y+=dy;
	//restricciones para los bordes
	if (y<=0 || y>=230) dy=-dy
	//para que no se siga moviendo solo
	dy=0;
	}

//jugador "B" segunda funcion llamada a ejecutarse
function drawB() { //notese que ya no es necesario limpiar pantalla la primera funcion se encargara de eso
	//dibujamos jugador B
	context.beginPath();
	context.fillRect(w,z,10,70);
	context.closePath();
	context.fill();
	//aumentamos dw y dz a los respectivos ejes segun las teclas de control de la funcion control() de esa manera simulamos movimiento
	z+=dz;
	//restricciones para los bordes
	if (z<=0 || z>=230) dz=-dz
	//para que no se siga moviendo solo
	dz=0;
	}

//pelota tercera funcion llamada
function pelota() {
	var nave=navigator.userAgent.toLowerCase();
	if(nave.indexOf("firefox")!=-1)
		{
		  HTMLElement.prototype.__defineGetter__("innerText",function () { return(this.textContent); });
		  HTMLElement.prototype.__defineSetter__("innerText",function (txt) { this.textContent = txt; });
		 }
	//dibujamos la pelota
	/*
	context.beginPath();
	context.fillRect(m,n,10,10);
	context.closePath();
	context.fill();
	*/
	//@Aga mod
	context.beginPath();
	context.arc(m,n,10,0,Math.PI*2,true);
	context.closePath();
	context.fill();
	//aumentamos dw y dz a los respectivos ejes segun las condiciones declaradas a continuacion
	m+=dm;
	n+=dn;
	//relacionamos los valores de las coordenadas para que cambie de direccion cuando choque con un juagador
	if ((x+20==m && n<=y+70 && n+20>=y)||(w==m+10 && n<=z+70 && n+10>=z)) {
		//adicionalmente relacionamos coordenadas y la variable "diago" para el movimiento en diagonal de rebote de la pelota
		//segun la direccion que en ese momento estaba teniendo el jugador
		if(diago==0){dm=-dm}
		if(diago==1){dm=-dm;dn=-10}
		if(diago==2){dm=-dm;dn=10}
	}
	//restricciones para los bordes superiores
	if (n<=0 || n>=290) {dn=-dn}

	//pierde A y lanzamos otra pelota
	if (m==0){
		puntajeA+=1;
		document.getElementById('puntajeA').innerText = puntajeA;
		n=145;
		m=300;
		dm=-dm;
	}
	//pierde B y lanzamos otra pelota
	if (m==600){
		puntajeB+=1;
		document.getElementById('puntajeB').innerText = puntajeB;
		n=145;
		m=300;
		dm=-dm;
	}
}

function pausa() {
    processingInstance = Processing.getInstanceById('stage');
    processingInstance.noLoop();
    pausado=true;
}

function reanudar() {
    processingInstance = Processing.getInstanceById('stage');
    processingInstance.loop();
    pausado=false;
}

//funcion para capturar las teclas presionadas a travez del onkeydown del body y controlar los jugadores
//funcion para capturar las teclas presionadas a travez del onkeydown del body y controlar los jugadores
//@DK  mod
document.onkeydown = function (event)
   {
    var keycode = (window.event||event).keyCode;
	tecla=event.keyCode;
	//Pone pausa
	if (tecla==13/* && pausado==false*/) {pausa();}
	//Saca pausa
	//if (tecla==13 && pausado==true) {reanudar();}
	//Controles "A"
	if (tecla==87) {dy=-35; diago=1;} //arriba W
	if (tecla==83) {dy=35; diago=2;} //abajo S
	//Controles "B"
	if (tecla==38) {dz=-35; diago=1;} //arriba
	if (tecla==40) {dz=35; diago=2;} //abajo
}
/*function Control() {
	tecla=event.keyCode;
	//Controles "A"
	if (tecla==87) {dy=-10; diago=1;} //arriba W
	if (tecla==83) {dy=10; diago=2;} //abajo S
	//Controles "B"
	if (tecla==38) {dz=-10; diago=1;} //arriba
	if (tecla==40) {dz=10; diago=2;} //abajo
}
*/
</script>
</head>

<body link="red" vlink="red" alink="red">
  <div id='bar' align="center">

<h3>Ping Pong en HTML5 v0.1</h3>
<canvas id="stage" width="600" height="300" onClick="init();" >
Por favor, utiliza Firefox, Chrome, Safari u Opera.
</canvas>

      <div id='score_container'>
        Jugador A:
        <b><span id='puntajeA'>0</span></b>

        Jugador B:
        <b><span id='puntajeB'>0</span></b><br>
      </div>
</div>

**"Programando con pilas-engine"**

.. image:: data/imagenes/pilas-logo.png
    :scale: 120 %
    :align: center
        

Índice:
-------

.. toctree::
    :maxdepth: 2

    data/Introduccion.rst
    data/ActoresYfondos.rst
    data/MenuOpciones.rst
    data/EscenasMenuControles.rst
    data/EscenaJuego.rst
