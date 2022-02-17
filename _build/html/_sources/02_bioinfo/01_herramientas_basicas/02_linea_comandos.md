

# Introducción a linea de comandos
**Autora: M. Nayeli Luis-Vargas**

:::{admonition} Objetivo
:class: tip
Comprender la diferencia entre Unix y Linux
Conocer los comandos básicos de Bash para manejar archivos y directorios desde la terminal.
:::


## Linux y Unix

Linux es un sistema operativo (SO) como Microsoft Windows o MacOS. Un SO es un programa de computadora que administra cómo ésta se conecta al hardware (pantalla, teclado, etc.), también administra sus archivos y le permite ejecutar aplicaciones de software. Un SO generalmente vendrá como una interfaz gráfica de usuario (GUI), la interfaz gráfica es la parte con la que interactúa el usuario (o sea tu).

Ahora un poco de historia... El término Linux se refiere a una familia de sistemas operativos de código abierto similares a Unix basados en el kernel de Linux, el cual fue desarrollado por Linus Torvalds y lanzado por primera vez en 1991. Unix en sí se refiere a una familia de SO multitarea y multiusuario todo derivado del AT&T Unix original que se desarrolló a fines de la década de 1970. En la práctica, aunque Unix se refiere estrictamente a un sistema operativo comercial y Linux se refiere a un sistema operativo de código abierto disponible gratuitamente, las dos palabras tienden a usarse indistintamente.



## La terminal
::::{margin}
:::{admonition} Terminus
:class: note
Aquí un enlace para una terminal online
<br>
<a href = "https://web.mit.edu/mprat/Public/web/Terminus/Web/main.html"> Terminus </a>
:::
::::

La terminal es un software que permite la interacción de usuario con la computadora escribiendo simples comandos de texto. Todas las computadoras con SO Linux contienen una terminal, Mac OS también tienen su equivalente, sin embargo, las versiones actuales de Windows no.

## Linea de comandos

La línea de comando es la línea actual dentro del terminal que se puede usar para ingresar comandos de texto. Cada comando se ejecuta a través de un shell, un programa que envía comandos a la computadora para que los interprete. Los shells comunes incluyen `bash`, `zsh`, `tcsh / csh` y `ksh`. En este curso, nos centraremos en el shell bash. Los comandos básicos tienden a ser los mismos en todos los shells, pero algunos de los comandos más avanzados pueden variar un poco en sintaxis entre ellos.

## Comandos básicos para el manejo de archivos y directorios

````{margin}
```{note}
Fichero = Archivo
<br>
Directorio = Carpeta
```
````

Es importante mencionar que los directorios en una carpeta están jerarquizados (ver figura), es decir, que un directorio puede estar dentro de otro y así sucesivamente hasta tener uno principal. Además, cada directorio y/o fichero tienen un ruta que indica el sitio donde se encuentran. Tomar en cuenta lo anterior permitirá que no te pierdas entre el laberinto de directorios y ficheros que puedas tener en tu computadora.

<br>

```{figure} ../img/directory_tree.png
---
height: 350px
name: arbol de directorios
---
Árbol de directorios
```


Utilizar la terminal y manejar archivos y directorios a través de comandos es importante porque es más eficiente y al trabajar con grandes datos biológicos, los recursos de hardware de una computadora personal no son suficientes. En cambio, se utiliza un servidor, y los servidores en general no tienen interfaz gráfica, por lo que no tenemos más opción.
