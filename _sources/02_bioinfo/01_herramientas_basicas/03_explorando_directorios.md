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

## Comandos básicos

A continuación se presentan algunos comandos básicos para el manejo y exploración de directorios:

`pwd`
: "print working directory": Indica la ruta (path) en la que se encuentra tu archivo.

`cd`
: "change directory": se utiliza para cambiar de directorio. Ejemplo de sintaxis: `cd nombre_directorio`.

`ls`
: "list": Enlista los archivos que hay en un directorio.

`rm`
: "remove": Elimina un fichero o un directorio. Ejemplo de sintaxis: rm `nombre_fichero/directorio`.

`mv`
: "move": Mueve un fichero o directorio a otra ruta. Ejemplo de sintaxis: `mv archivo.txt ./nueva_carpeta`. También se puede cambiar el nombre de un fichero o directorio, ejemplo: `mv nombre_feo.txt nombre_cool.txt`.

`mkdir`
: "make directory": Crea un directorio nuevo.

`man`
: "manual": Muestra el manual de uso de un comando en particular.

`cp`
: "copy": Copia un archivo a un directorio. Ejemplo: `cp archivo.txt /mi/ruta/directorio`.


Una vez que ya conoces los comandos básicos para usar en terminal, vamos a practicar un poco. Para este ejercicio utilizaremos una terminal virtual llamada <a href = "https://sandbox.cs50.io/">CS50 Sandbox </a>, al dar click te aparecerá la siguiente ventana:

```{figure} images/03_explorando_direc/1.png
---
height: 400px
name: ventana Sandbox
---
Ventana de la terminal virtual Sandbox
```

<br>
Da click en crear para poder acceder a la terminal virtual.

<br>

:::{admonition} Nota
:class: warning
Para poder acceder debes tener una cuenta de <a href = "https://github.com/">GitHub</a>, sino la has creado, ahora es el momento perfecto.
:::

<br>
En seguida te aparecerá la siguiente interfaz:

<br>

```{figure} ../img/03_explorando_direc/2.png
---
height: 450px
name: interfaz
---
Interfaz de la terminal virtual Sandbox.
```

<br>

Vamos a crear un directorio con el comando de ***make directory*** (`mkdir`), para ello escribirás lo siguiente en la terminal y darás 'Enter'.
<br>

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
<br>

Accede a tu carpeta 'dir3' y teclea el comando para imprmir la ruta o dirección.
<br>

```{code-block} bash
cd dir3
pwd
```

Te aparerá algo así:


```{code-block} bash
/root/sandbox/mi_directorio/dir1/dir3
```

Ésta es tu directorio de trabajo (***working directory***), te encuentras en el directorio llamado 'dir3', y si creas más directorios o archivos, se colocarán aquí.

Ahora ¿Qué pasa si quieres volver al directorio anterior?, la isntrucción que darás es la siguiente:

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

## Rutas absolutas y rutas relativas

Una **ruta absoluta** de un directorio nos indica todo el camino que hay que recorrer para llegar a él. Mientras que, una **ruta relativa** apunta a una referencia y luego indica el camino a partir de esa referencia. Imagina que invitas a un@ amig@ a tu casa, no es lo mismo darle instrucciones si el punto de partida es su casa; a darle instrucciones si el punto de partrida es desde la tienda más cercana a tu casa. Acá sucede lo mismo.

<br>

Considerando el ejercicio que hemos estado realizando, nuestro árbol de directorios se vería así:

<br>

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

