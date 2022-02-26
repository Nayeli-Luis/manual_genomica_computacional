# Explorando directorios desde la terminal
**Autora: M. Nayeli Luis-Vargas**

:::{admonition} Objetivo
:class: tip
* Identificar la arquitectura jerárquica que tienen los directorios en una computadora.
* Entender los comandos `pwd`, `cd`, `ls`, `mkdir`.
:::

::::{margin}
:::{admonition} Shortcuts
:class: tip
Algunos shortcuts para hacer más fluído tu uso de la terminal:
* `tab`: Completa el nombre de un fichero o directorio existente.
* `Ctrl + a`: Ir al principio de la línea.
* `Ctrl + e`: Ir al final de la línea.
* `Ctrl + l` o comando `clean`: Limpiar pantalla.
* Uso de flechas del teclado permite ver el historial de comandos recientes.
* `Ctrl + r`: Espera que des un patrón de búsqueda. Te regresa las líneas que has ejecutado que contengan ese patrón. 
:::
::::


## Comandos básicos para manejo de directorios

A continuación se presentan algunos comandos básicos para el manejo y exploración de directorios:

`pwd`
: "print working directory": Indica la ruta (path) en la que se encuentra tu archivo.

`mkdir`
: "make directory": Crea un directorio nuevo.

`cd`
: "change directory": se utiliza para cambiar de directorio. Ejemplo de sintaxis: `cd nombre_directorio`.

`ls`
: "list": Enlista los archivos que hay en un directorio.

`rm`
: "remove": Elimina un fichero o un directorio. Ejemplo de sintaxis: rm `nombre_fichero/directorio`.

`mv`
: "move": Mueve un fichero o directorio a otra ruta. Ejemplo de sintaxis: `mv archivo.txt ./nueva_carpeta`. También se puede cambiar el nombre de un fichero o directorio, ejemplo: `mv nombre_feo.txt nombre_cool.txt`.

`man`
: "manual": Muestra el manual de uso de un comando en particular.

`cp`
: "copy": Copia un archivo a un directorio. Ejemplo: `cp archivo.txt /mi/ruta/directorio`.


## Sintaxis de los comandos

Para la exploración de directorios y el manejo de archivos a través de la terminal requiere el uso de comandos específicos y éstos comandos a su vez tienen su propia sintaxis. La sintaxis es la siguiente: 

```
comando opcion argumento 
```

Y cada elemento está separado por simples espacios. 


### Opciones y argumentos 

En Bash es posible modificar el comportamiento de los comandos utilizando opciones (parámetros) y argumentos. Por ejemplo, cuando utilizamos `mkdir` es necesario escribir después el nombre de la carpeta que vamos a generar, esto es un **argumento**. Cada argumento se separa mediante un espacio. 

```
mkdir carpeta_nueva
```

Algunos argumentos son obligatorios, como el nombre de un archivo para `file` , por otr lado, algunos argumentos son **opcionales**. Por ejemplo, el comando `ls` funciona sin problema, sin importar en que carpeta nos encontremos. 

Los comandos también tienen **opciones** y las opciones están indicadas por un guión o dos antes de una letra, por ejemplo la opción `-n` para el comando `head`, gracias a esa opción nosotros podemos especificar el número de líneas que queremos ver de un archivo. ¿Cómo sabemos qué opciones tiene un comando? para eso existe el comando `man` al cual le pasamos como argumento el nombre de otro comando. Lo haremos con  `head`: 

```
man head
```
Cuando escribimos eso en terminal aparecerá una sección llamada `DESCRIPTION`, la cual indica las opciones con las que contamos.

```
DESCRIPTION
     This filter displays the first count lines or bytes of each of the
     specified files, or of the standard input if no files are specified.  If
     count is omitted it defaults to 10.

     The following options are available:

     -c bytes, --bytes=bytes
             Print bytes of each of the specified files.
    -n count, --lines=count
             Print count lines of each of the specified files.

     If more than a single file is specified, each file is preceded by a header
     consisting of the string “==> XXX <==” where “XXX” is the name of the file.

```

## Directorio de trabajo 

::::{margin}
:::{note}
Fichero = Archivo

Directorio = Carpeta
:::
::::

Los directorios en una computadora están jerarquizados ({ref}`arbol de directorios`), es decir, que un directorio puede estar dentro de otro y así sucesivamente hasta tener uno principal. Además, cada directorio y/o fichero tienen un **ruta** que indica el sitio donde se encuentran. El **directorio de trabajo** o (***working directory***) es la carpeta en nuestra computadora en donde se encuentran los archivos y scripts con los que estamos trabajando actualmente. 


```{figure} ../img/arbol_directorios.png
---
height: 350px
name: arbol de directorios
---
Árbol de directorios
```

::::{margin}
:::{admonition} El directorio `root` y `home`
:class: note

* El directorio */root* es como el directorio */home* del superusuario, es decir, del administrador del servidor. 
* En el directorio */home* de un servidor se encuentran el resto de los usuarios. 
:::
::::


### Rutas relativas y absolutas

Una **ruta absoluta** de un directorio nos indica todo el camino que hay que recorrer para llegar a él. Mientras que, una **ruta relativa** apunta a una referencia y luego indica el camino a partir de esa referencia. Imagina que invitas a un@ amig@ a tu casa, no es lo mismo darle instrucciones si el punto de partida es su casa; a darle instrucciones si el punto de partida es desde la tienda más cercana a tu casa. En el caso de los directorios, funciona igual, si quisieramos acceder al directorio */bioinfo* podríamos hacerlo desde */root* y eso sería su *ruta absoluta*. Sin embargo, si nos encontramos dentro del directorio de */katara*, la ruta está tomando de referencia ésta carpeta y entonces sería una *ruta relativa*. 

```{figure} ../img/tipos_rutas.png
---
height: 400px
name: tipos-rutas
---
Ruta absoluta y relativa. 
```


## Ejercicio en clase

Una vez que ya conoces los comandos básicos para usar en terminal, vamos a practicar un poco. Para este ejercicio utilizaremos la terminal virtual <a href = "https://sandbox.cs50.io/">CS50 Sandbox </a> que te presenté en la sección anterior.

Vamos a crear un directorio con el comando de ***make directory*** (`mkdir`), para ello escribirás lo siguiente en la terminal y darás 'Enter'.

```{code-block} bash
mkdir mi_directorio
```

En seguida te aparecerá el directorio que creeaste en el árbol de directorios:

```{figure} ../img/03_explorando_direc/3.png
---
height: 300px
name: directorios
---
Árbol de directorios de la terminal virtual de Sandbox.
```

Ahora accedamos a ese directorio con el comando ***change directory*** (`cd`):

```{code-block} bash
cd mi_directorio
```

y vamos a crear dos directorios aquí:

```{code-block} bash
mkdir dir1 dir2
```

Si das click en tu carpeta principal 'mi_directorio', en el árbol de directorios te aparecerán tus dos nuevas carpetas. Pero si queremos verlas desde la terminal, podemos dar la instrucción de que las liste (`ls`).

```{code-block} bash
ls
```

¿Qué notas? Si pones atención en la terminal, los diectorios aparecen marcados de azul y con una diagonal (/) al final del nombre.

```{figure} ../img/03_explorando_direc/4.png
---
height: 300px
name: nombres directorios
---
Nombre de los directorios aparecen resaltados.
```

Bien, ahora entremos al 'dir1' y creemos un par de directorios más.


```{code-block} bash
cd dir1
mkdir dir3 dir4
```
¿Notaste que pude crear dos directorios de golpe?

Si no tuvieramos la pestaña del árbol de directorios pero quisieramos saber en dónde se encuentra nuestra carpeta 'dir3', utilizariamos `pwd`.

Accede a tu carpeta 'dir3' y teclea el comando para imprimir la ruta o dirección.

```{code-block} bash
cd dir3
pwd
```
Te aparerá algo así:

```{code-block} bash
/root/sandbox/mi_directorio/dir1/dir3
```

Ésta es tu directorio de trabajo (***working directory***), te encuentras en el directorio llamado 'dir3', y si creas más directorios o archivos, se colocarán aquí.

Ahora ¿Qué pasa si quieres volver al directorio anterior?, la instrucción que darás es la siguiente:

```{code-block} bash
cd ..
```

Y si imprimes la ruta verás que ahora te encuentras en 'dir1'.

```{code-block} bash
/root/sandbox/mi_directorio/dir1
```

Por último, si quisieramos volver al directorio raíz, es decir, a 'root/sandbox', tendríamos que escribir:

```{code-block} bash
cd
```

Imprime de nuevo la ruta para que te asegures:

```{code-block} bash
/root/sandbox
```

Ahora veamos como se ven las rutas absolutas y relativas desde la terminal. Considerando el ejercicio que hemos estado realizando, nuestro árbol de directorios se vería así:

```{figure} ../img/03_explorando_direc/arbol_ejercicio.png
---
height: 400px
name: arbol arbol_ejercicios
---
Representación gráfica del árbol de directorios para éste ejercicio.
```

Si quisieramos acceder a 'dir3' desde la terminal y escribiendo su ruta absoluta, ésta sería:

```{code-block} bash
cd /root/sandbox/mi_directorio/dir1/dir3
```

Sin embargo, si estuvieramos en 'dir2' y quisieramos acceder a 'dir3', estamos apuntando ahora a una referencia. Tendríamos primero que volver a 'mi_directorio' para luego ingresar a 'dir1' y finalmente a 'dir3', por tanto, la ruta relativa se vería así:

```{code-block} bash
cd ../dir1/dir3
```
Nota que no escribí 'mi_directorio', en linea de comandos `../` indica "volver a la carpeta superior".
