# Opciones y argumentos 

En Bash es posible modificar el comportamiento de los comandos utiliznado opciones y argumentos. Por ejemplo, cuando utilizamos `touch` es necesario escribir después el nombre del archivo que vamos a generar, esto es un **argumento**. Cada argumento se separa mediante un espacio. 

```
touch archivo_nuevo.txt
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
