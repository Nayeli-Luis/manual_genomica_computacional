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


```{code-block} bash
mkdir 01_archivos
cd 01_archivos
pwd
```

Una vez que estés dentro de tu directorio de trabajo, vamosa a crear un fichero. Para crear archivos solo basta con utilizar el comando `touch`:


```{code-block} bash
touch archivo01.txt
```

Y para asegurarnos que fue creado podemos ingresar el comando `ls`:

```{code-block} bash
ls
```

Podras observar que ya aparece tu archivo. También podemos crear varios ficheros en una sola línea. Imaginemos que deseamos crear 10 archivos, lo que escribiríamos a continuación sería:


```{code-block} bash
touch archivo0{2..9}.txt
```

Lista de nuevo para comprobar que se han creado.

Ahora, vamos a utilizar el comando `echo` para pasar una linea de texto como un argumento y guardarlo en un archivo.


```{code-block} bash
echo "Aprender bioinformatica es bueno para la salud" > archivo02.txt
```

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

```{figure} ../img/04_archivos/nano.png
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


## `cat`

El comando `cat` tiene diferentes funciones: 

* Crear archivos
* Escribir un archivo
* Ver el contenido de un archivo (es la más utilizada)
* Concatenar archivos

Primero, vamos a crear un archivo llamado `planetas`

```
cat > planetas
```
Podras escribir contenido, después de escribirlo, puedes guarda con `ctrl + d` y puedes comprobar que se ha creado con `ls`. 

Para ver el contenido solo escribe `cat planetas`, te aparecerá algo como:

```
(base) usuario@computadora ~ % cat planetas
mercurio
venus
tierra
```

Ahora agregamos `marte` en otra línea: 

```
cat >> planetas
marte

# ctrl + d para cerrar y guardar
```
Visualiza que se haya agregado el planeta nuevo. 

Ahora crearemos con `cat` otro archivo llamado `planetas2`: 

```
cat > planetas2
jupiter
saturno
urano
neptuno
pluton

# ctrl + d
```

Para unir o concatenar los archivos podemos escribir: 

```
cat planetas planetas2 > planetas_todos
```

## `head` y `tail`

Muestran el contenido de un archivo por terminal. `head` muestra las 10 primeras líneas, al menos que se específique otro numero y `tail` muestra las 10 últimas líneas. Para especificar debes agregar `-n`.

```
# Ver primeras dos líneas
head -n 2 planetas_todos

# Ver últimas dos líneas
tail -n 2 planetas_todos
```

## Creación de ligas (links)

En los sistemas Linux es posible crear ligas o *links* entre archivos, es como crear un acceso directo o "*shortcut*." Existen dos tipos de ligas las *hard* y las *soft* o simbólicas.

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


El comando para crear ligas es `ln` y para crear ligas *soft* se utiliza con la opción `-s`.  Cuando trabajas en un servidor externo, la mayoría de las veces solo podrás crear *soft links*. Por tanto, vamos a crear un *soft link* del 'archivo01.txt' en nuestra carpeta llamada 'genomica'. Para esto, primero accederemos a la carpeta donde queremos el link y luego lo generaremos escribiendo el comando `ln` con la opción `-s` y la ruta relativa correspondiente:

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

