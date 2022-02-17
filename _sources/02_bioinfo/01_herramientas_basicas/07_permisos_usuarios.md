# Permisos y usuarios

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

## Cambiar permisos

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

## Super usuarios

Todas las versiones de UNIX tienen un super-usuario el cual tiene TODOS los derechos y privilegios sobre el SO y los archivos dentro del mismo. Este usuario es **root** y pertenece al grupo del mismo nombre, siendo su UID y GID 0. Existe un comando especial llamado `sudo` (*super user do*) que al utilizarlo permite al usuario actual tener privilegios de super-usuario temporales. No te emociones, muchas veces se te solicita una contraseña cuando utilizar este comando.

<br>

```{code-block} bash
usuario@computadora: ~$ sudo [comando]
```