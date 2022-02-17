# Archivos, permisos y usuarios
**Autora: M. Nayeli Luis-Vargas**

:::{admonition} Objetivo
:class: tip
* Aprender a crear y editar archivos desde la terminal.
* Comprender el significado de lo símbolos de permisos y ser capaza de cambiarlos.
* Comprender las diferencias entre las ligas *soft* y *hard*.
:::

Un archivo o fichero  en Linux puede definirse como una colección de datos que aparecen al usuario como un bloque de información.

:::{admonition} Nota
:class: warning
Te recomiendo siempre hacer carpetas para cada prueba/ejercicio que vayas a realizar y conozcas la dirección exacta. En este caso, seguiré utilizando Sandbox, pero tu puedes utilizar la terminal de tu computadora o del ambiente Linux que hayas creado.
:::


## Crear archivos

Primero, crearemos un directorio para guardar todo lo que hagamos en este apartado, ingresaremos en ese nuevo directorio, crearemos una carpeta dentro e imprimiremos la ruta:

<br>

```{code-block} bash
mkdir 01_archivos
cd 01_archivos
mkdir genomica
pwd
```
<br>

Una vez que estés dentro de tu directorio de trabajo, vamosa a crear un fichero. Para crear archivos solo basta con utilizar el comando `touch`:

<br>

```{code-block} bash
touch archivo01.txt
```
<br>

Y para asegurarnos que fue creado podemos ingresar el comando `ls`:

<br>

```{code-block} bash
ls
```
<br>

Podras observar que ya aparece tu archivo. También podemos crear varios ficheros en una sola línea. Imaginemos que deseamos crear 10 archivos, lo que escribiríamos a continuación sería:

<br>

```{code-block} bash
touch archivo0{2..9}.txt
```
<br>

Lista de nuevo para comprobar que se han creado.

Ahora, vamos a utilizar el comando `echo` para pasar una linea de texto como un argumento y guardarlo en un archivo.

<br>

```{code-block} bash
echo "Aprender bioinformatica es bueno para la salud" > archivo02.txt
```
<br>

Si te das cuenta, utilicé el símbolo de "mayor que" para poder indicar en donde quería guardar la linea de texto.

Vamos a comprobar que `archivo02.txt` se creó correctamente, para esto lo abriremos y usaremos el comando `file`.

```{code-block} bash
file archivo02.txt
```

`file` determina el tipo y formato de un archivo, en este caso es un fichero que utiliza el formato de codificación ASCII que es el Código Estadounidense Estándar para el Intercambio de Información y es el código que se utiliza en los ficheros generados por métodos de secuenciación masiva. <a href = "https://elcodigoascii.com.ar/">Aquí</a> puedes hallar cada símbolo.

Podemos cambiar el nombre de un archivo con el comando `mv`.


```{code-block} bash
mv archivo02.txt archivo02_mod.txt
```

Vuelve a listar para comprobar que el cambio se llevó a cabo.

## Editar archivos
Para editar algún archivo desde la terminal se utilizan editores de texto. **GNU nano** es un editor de texto para entornos similares a Unix y otros sistemas operativos que utilizan una línea de comandos de terminal. Existen otros editores como **vi**, **vim**, **Emacs** y **pico**, en este caso usaremos **Nano**.

Primero, vamos a crear un nuevo archivo con el siguiente ejemplo:


```{code-block} bash
nano datos_alumnos.txt
```

Te abrirá una ventana de éste estilo:

```{figure} images/04_archivos/nano.png
---
height: 450px
name: ventana nano
---
Ventana de Nano
```

Ahora ingresaremos una tabla donde separaremos cada valor por tabuladores `tab`. Es decir, nombre + tab + apellido + tab + correo.

```{figure} images/04_archivos/01.png
---
height: 450px
name: valores
---
Valores ingresados en Nano
```


Ahora darás `control + x` para salir del editor nano, y te aparecerá un menú que te preguntará si deseas guardar lo que has modificado, le pondrás que si presionando la tecla `y` y luego `Enter`.

## Explorar archivos


## Permisos y usuarios

Cada archivo o fichero tiene un propietario individual (por  lo general, el usuario que lo creó) y un amplio conjunto más amplio de propietarios que pertenece a un grupo Unix en particular. **Un grupo Unix** es un conjunto de usuarios que tienen permiso para acceder a un software o archivos particulares. Los grupos también se utilizan para garantizar que solo determinados usuarios puedan utilizar comnados que pueden afectar todo el sistema Linux. Para ver en qué grupos se encuentra.

Primero veremos que usuario somos, para ello ingresaremos en terminal:

```{code-block} bash
whoami
```

Este comando desplegará el nombre de tu usuario, si te encuentras realizando ésta práctica en <a href = "https://sandbox.cs50.io/">CS50 Sandbox </a>, tu usuario será 'root'.

Ahora para conocer los permisos de un archivo se escribe en terminal `ls -l`. Veamos los permisos de los archivos que creamos:

```{figure} images/04_archivos/permisos.png
---
height: 300px
name: permisos
---
Permisos
```
Como se puede ver en la imagen (o en tu propia pantalla), aparece una especie de tabla con siete columnas.

 * La primera columna tiene 10 caracteres, el caracter en la posición 1 indica si el archivo tiene un estatus especial, si primero tiene una 'd', entonces el archivo listado es un directorio. En este caso, el directorio 'genomica'. De la posición 2-4 son los permisos del propietario, de la posición 5-7 son los permisos para el grupo, de la posición 8-10 son los permisos para el resto de los usuarios o público. Ahora los permisos son:
    * `r`: read - permiso para leer el archivo.
    * `w`: write - permiso para escribir en el archivo, es decir, editar.
    * `x`: executable - permiso para ejecutar en caso de ser un script o programa, todas las carpetas son ejecutables, por tanto el permiso para abrir la carpeta 'genomica' está concedido.

* La segunda columna indica el número de links que tiene ese archivo.

* La tercera columna el usuario propietario.

* La cuarta columna el rango de usuario que tiene el propietario del archivo.

* La quinta columna el peso del archivo en bytes.

* La sexta columna la fecha y hora de creación.

* La séptima columna el nombre del archivo.

### Cambiar permisos

Para cambiar los permisos se utilizan los comandos `chown`, `chgrp` y `chmod`. Te recomiendo ver más especificaciones de cada uno con el comando `man`.

`chown`
: *change owner*. En general sólo lo utilizan quienes tienen permiso de administrador.

`chgrp`
: *change group* .Se utiliza para cambiar el grupo propietario.

`chmod`
: *change mode*. Permite cambiar los permisos de acceso de un fichero o directorio. La sintaxis que se utiliza es numérica, por ejemplo, si se quiere dar permiso de lectura, escritura y ejecución de un archivo para todos la sintaxis sería:


```{code-block} bash
chmod 777 archivo01.txt
```


Si vuelves a listar ( `ls -l`) podrás ver que los permisos para tu 'archivo01.txt' han cambiado. Ahora en la primera columna deberá aparecerte `-rwxrwxrwx`. Para saber el número que deberías poner para cambiar los permisos puedes utilizar la siguiente <a href = "https://sandbox.cs50.io/">calculadora de `chmod`</a>.


Otra manera de usar `chmod` es de manera simbólica, donde se usan las letras `u` (usuario), `g` (grupo) y `a` (*all*, todos), los simbolos `+` (más) o `-` (menos) y las letras `r` (*read*, leer), `w` (*write*, escribir) o `x` (*executable*, ejecutar) para cambiar los permisos. Por ejemplo, supongamos que tenemos un script (un programa) llamado 'script.sh' que deseamos ejecutar, para cambiar los permisos escribiríamos en terminal:


```{code-block} bash
chmod a+x script.sh
```

### Super usuarios

Todas las versiones de UNIX tienen un super-usuario el cual tiene TODOS los derechos y privilegios sobre el SO y los archivos dentro del mismo. Este usuario es **root** y pertenece al grupo del mismo nombre, siendo su UID y GID 0. Existe un comando especial llamado `sudo` (*super user do*) que al utilizarlo permite al usuario actual tener privilegios de super-usuario temporales. No te emociones, muchas veces se te solicita una contraseña cuando utilizar este comando.

<br>

```{code-block} bash
usuario@computadora: ~$ sudo [comando]
```

## Creación de ligas (links)

En los sistemas Linux es posible crear ligas o *links* entre archivos, es como crear un acceso directo o "*shortcut*." Existen dos tipos de ligas las *hard* y las *soft* o simbólicas.

<br>
Los enlaces *soft* o simbólicos:
* Pueden cruzar todo el sistema de archivos
* Generan un acceso directo a los archivos
* Tienen diferentes permisos con respecto al archivo original
* Si cambian los permisos o la ubicación del archivo original, estos no se actualizan.
* Contienen solo la ruta del archivo original no el contenido.


Por otro lado, los enlaces *hard* :
* No pueden cruzar todo el sistema de archivos
* No crean un acceso directo *sensu sctricto*
* Tienen los mismos permisos que el archivo original
* Si la ubicación o los permisos del archivo original, estos se actualizarán.
* Contienen todo el contenido del archivo original, por lo que podrás seguir viendo el contenido aunque el archivo original sea eliminado o modificado.


El comando para crear ligas es `ln` (consulta `man` si quieres saber más) y para crear ligas *soft* se utiliza con la opción `-s`.  Cuando trabajas en un servidor externo, la mayoría de las veces solo podrás crear *soft links*. Por tanto, vamos a crear un *soft link* del 'archivo01.txt' en nuestra carpeta llamada 'genomica'. Para esto, primero accederemos a la carpeta donde queremos el link y luego lo generaremos escribiendo el comando `ln` con la opción `-s` y la ruta relativa correspondiente:

```{code-block} bash
cd genomica
ln -s ../archivo01.txt
```
Si enlistas tu carpeta, aparecerá el archivo y generalmente aparece resaltado en otro color:


```{figure} ../img/04_archivos/soft_link.png
---
height: 100px
name: soft_link
---
Liga simbólica o *soft link*.
```

Y si exploras el contenido con `file`, deberá aparecerte vacio (*empty*) debido aque solo es un acceso directo del archivo original.
