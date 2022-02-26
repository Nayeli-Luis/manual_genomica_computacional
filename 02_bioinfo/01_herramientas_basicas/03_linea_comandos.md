
# Introducción a linea de comandos
**Autora: M. Nayeli Luis-Vargas**

:::{admonition} Objetivo
:class: tip
Comprender la diferencia entre Unix y Linux
Conocer los comandos básicos de Bash para manejar archivos y directorios desde la terminal.
:::

## Arquitectura de una computadora

Antes de ver qué es la línea de comandos y empezar a conocer el sistema operativo que generalemnte se utiliza en bioinformática, es necesario tener nociones de la arquitectura de una computadora. Una computadora se compone de: 

* Hardware: Se refiere a las partes físicas y tangibles de una computadora, por ejemplo: el monitor, la tarjeta madre, el mouse, etc. 

* Kernel o núcleo: Es un software que constituye parte fundamental de un sistema operativo. Es el software responsable de facilitar la conexión entre los distintos programas al hardwares, en otras palabras. Es el encargado de gestionar recursos, a través de servicios de llamada al sistema, además, para acceder al kernel se requieren permisos en modo privilegiado. 

* Aplicaciones base: Aquí se encuentra el sistema operativo, asi como las aplicaciones base que brinda. También pueden encontrarse las aplicaciones de cada usuario como los navegadores, prgramas de ofimática, etc. 

* Shell gráfica: Un *shell* es un intérprete, una shell gráfica provee una interfaz gráfica que facilita al usuario accede a los programas y servicios que brinda un sistema operativo. 

* Shell CLI: Un *shel CLI* (*Command Line Interface*) es un programa que permite a los usuarios escribir comandos de texto para solicitar a la computadora que realice tareas específicas. Los *shell CLI* requieren un intérprete como `bash`. 

```{figure} ../img/arquitectura_computadora.png
---
height: 400px
name: arq_compu
---
Arquitectura de una computadora
```


## Unix y Linux

Unix es una familia de sistemas operativos multitarea y multisuario creado a finales de los 70 utilizado en servidores y estaciones de trabajo de alto rendimiento, su dueño es la compañía de AT&T Bell Labs.

Linux deriva de dos proyectos basados en Unix, el proyecto GNU (*GNU is Not Unix*) iniciado por Richard Stallman en 1983 y el kernel de Linux, desarrollado por Linus Torvalds en 1991. El término Linux se refiere a una familia de sistemas operativos de código abierto similares a Unix basados en el kernel de Linux. En la práctica, aunque Unix se refiere estrictamente a un sistema operativo comercial y Linux se refiere a un sistema operativo de código abierto disponible gratuitamente, las dos palabras tienden a usarse indistintamente.

## Terminal (*Shell CLI*)

La terminal  es un software que permite la interacción de usuario con la computadora escribiendo simples comandos de texto. Todas las computadoras con SO Linux contienen una terminal, Mac OS también tienen su equivalente, sin embargo, las versiones actuales de Windows no.

### Linea de comandos

La línea de comando es la línea actual dentro del terminal que se puede usar para ingresar comandos de texto. Cada comando se ejecuta a través de un *shell CLI* (terminal), un programa que envía comandos a la computadora para que los interprete. Los interprétes más comunes incluyen `bash`, `zsh`, `tcsh / csh` y `ksh`. En este curso, nos centraremos en el shell bash. Los comandos básicos tienden a ser los mismos en todos los shells, pero algunos de los comandos más avanzados pueden variar un poco en sintaxis entre ellos.

Utilizar la terminal y manejar archivos y directorios a través de comandos es importante porque es más eficiente y al trabajar con grandes datos biológicos, los recursos de hardware de una computadora personal no son suficientes. En cambio, se utiliza un servidor, y los servidores en general no tienen interfaz gráfica, por lo que en realidad... no tenemos mucha opción.

## Terminal virtual

Para ésta sección del curso utilizaremos una terminal virtual <a href = "https://sandbox.cs50.io/">CS50 Sandbox </a>, para acceder a ésta solo requieres crear una cuenta de [GitHub](https://github.com/). Cuando accedas a la terminal virtual te aparecerá el siguiente menú:  

```{figure} ../img/03_explorando_direc/1.png
---
height: 400px
name: ventana-Sandbox
---
Ventana de la terminal virtual Sandbox
```

Seleccion *with terminal window* y *with text editor* y da click en crear. En seguida te aparecerá la siguiente interfaz:

```{figure} ../img/03_explorando_direc/2.png
---
height: 450px
name: interfaz
---
Interfaz de la terminal virtual Sandbox.
```
Y una vez que estés aquí podremos comenzar a trabajar. 