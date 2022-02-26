# Git y Github
**Autora: M. Nayeli Luis-Vargas**

:::{admonition} Objetivo
:class: tip
* Entender la diferencia entre Git y Github.
* Conocer los comandos básicos de Git para actualizar repositorios en GitHub
:::

::::{margin}
:::{admonition} Videos
:class: note
[What is Version Control?](https://git-scm.com/video/what-is-version-control)
::::

## Sistema de control de versiones

Un **sistema de control de versiones** es un sistema que registra los cambios de un archivo o un conjunto de archivos a lo largo del tiempo, de manera que puedas acceder a alguna versión antigua posteriormente. Todes hemos generado copias de un archivo para posteriormente modificarlo y así guardar la versión anterior, de manera similar funcionan los sistema de control de versiones. Cuando trabajas solo, generar copias de tus archivos puede funcionar, pero... ¿Qué pasa si estás generando un proyecto en conjunto con otras personas?, para ésto se inventaron los **sistema de control de versiones centralizados** (ver {ref}`control_versiones`), estos tienen un solo servidor que contiene todos los archivos y sus versiones, de manera que los usuarios puede extraer, cosultar o modificar archivos desde ese sitio central. El problema que tenemos ahora es que todo se encuentra en un sólo servidor, si éste falla se corre el riesgo de perder todos esos archivos.

En ésta parte de la historia entra los **sistemas de control de versiones distribuidos** como Git, Mercurial, Bazaar o Darcs. En estos sistemas los clientes no solo revisan la última version de los archivo, más bien ellos pueden ver todo el repositiorio completo con sus versiones. Además, si algún servidor muere el resto de los colaboradores tienen un clon de los archivos, literalmente un copia de seguridad completa de todos los datos (ver {ref}`control_versiones`).


```{figure} ../img/git_github/control_versiones.png
---
height: 500px
name: control_versiones
---
Diferencia entre control de versiones (centralizado y distribuido).
```

## Git

<a href = "https://git-scm.com/">Git</a> es un sistema de control de versiones  distribuido.  Git piensa en sus datos como una serie de copias instantáneas (*snapshots*) de un sistema de archivos en miniatura. Con Git, cada vez que se confirma o se guarda el estado de un proyecto, Git literamente toma una foto de cómo se ven todos sus archivos en ese momento y almacena una referencia a esa *snapshot*. Además, para aumentar su eficiencia, Git no vuelve a almacenar el archivo, solo un enlace al archivo idéntico al anterior ya almacenado. Además, Git sólo necesita archivos y recursos locales para trabajar.


### Los tres estados de Git

Ahora, es importante recalcar que Git tiene tres estados principales en los que se pueden encontrar los archivos:


* *Modified* (modificado): Significa que ha cambiado un archivo pero aún no se ha enviado a la base de datos.
* *Staged* (en espera): Significa que ha marcado un archivo modificado en su versión actual para que vaya en tu próxima confirmación.
* *Commited* (confirmado): Significa que los datos ya se almacenan de forma segura en su base de datos.

Est nos lleva a las tres secciones principales de un proyecto Git: el directorio de trabajo, el área de preparación  (*staging area*) y el directorio Git (ver {ref}`arbol_git`)

```{figure} ../img/git_github/arbol_git.png
---
height: 400px
name: arbol_git
---
Secciones de un proyecto Git.
```

El directorio de Git es donde se alamacenan los metadatos y la base de datos objetos para tu proyecto. El directorio de trabajo es una copia de una versión del proyecto y el área de preparación almacena la información acerca de lo que va a ir en tu próximo `commit` (confirmación), el área de preparación es como el sitio de espera.

Entonces el flujo de trabajo de Git es el siguiente:
1. Se modifican archivos en tu directorio de trabajo.
2. Se eligen los archivos que desea que formen parte de su próxima versión, en el área de preparación.
3. Se hace una confirmación, que toma los archivos tal como están en el área de preparación y se alamcena una *snapshot* permanente en su directorio de Git.


### Instalación de Git

Para instalar Git en sistema Linux:


```{code-block} bash
sudo dnf install git-all
```

o

```{code-block} bash
sudo apt install git-all
```


En macOS, se debe tener instalado <a href = "https://brew.sh/">Homebrew</a> o <a href = "https://developer.apple.com/xcode/">Xcode</a> para posteriormente
<a href = "https://git-scm.com/download/mac">instalar Git</a>.

### Comandos de `git`

`git init`
: Crea un repositorio vació en la carpeta actual (directorio de trabajo).

`git add`
: Agregar archivo al repositorio

`git commit -m "mensaje"`
: Guarda los cambios en el repositorio local. El mensaje es opcional

`git log`
: Ver el historial de los *commits* que se han hecho en un proyecto.

`git status`
: Conocer el estado de todos los archivos de un repositorio.

`branch`
: Conocer en que rama te encuentras actualmente

`git branch nombre_rama`
: Crear una nueva rama en tu repositorio local.

`git checkout nombre_rama`
: Cambiar de rama.

`git merge nombre_rama`
: Unir una rama en específico con la rama principal (master branch).

::::{margin}
:::{admonition} Buscador de comandos
<a href = "https://git-scm.com/docs">Aquí</a> la documentación de Git, para que busques y revises los comandos que necesites.
:::
::::


## GitHub

<a href = "https://github.com/">GitHub</a> es el host más grande para los repositiorios Git y es el punto central de colaboración de millones de desarrolladores y proyectos.

## Primeros pasos con Git y GitHub

Primero, para poder utilizar Git y Github desde tu computadora debes crear un token de acceso personal, el cual utilizarás como contraseña en la línea de comandos, para ellos debes seguir <a href = "https://docs.github.com/es/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token">este tutorial</a>. Guarda tu token en un lugar seguro, no lo compartas.

Ahora, vamos a iniciar sesión en Github y a crear un nuevo repositorio.

```{figure} ../img/git_github/01_nuevo_repositorio.png
---
height: 400px
name: 01_nuevo_repositorio
---
Generar nuevo repositorio.
```

Podemos nombrar, dar una descripción de nuestro repositorio, elegir si deseamos que sea público o privado y elegir si queremos que se generen automáticamnte algunos archivos (recomiendo que des click en "Learn more" para saber de qué va cada uno). Una vez que hayamos configurado nuestro nuevo repositorio, damos click en "Create repository".


```{figure} ../img/git_github/02_nombrar_repositorio.png
---
height: 500px
name: 02_nombrar_repositorio
---
Configurar repositorio.
```

Nos llevará a una ventana en donde nos mostrará la dirección de nuestro repositorio y algunas opciones que podemos configurar desde nuestra línea de comandos. 

```{figure} ../img/git_github/03_direccion.png
---
height: 450px
name: 03_direccion
---
URL de nuestro repositorio.
```

Lo ideal es tener un repositorio local en nuestra computadora en donde ya hayamos iniciando un repositorio con `git init`, y hayamos agregado archivos (con `git add` y luego `git commit`). de ésta manera podremos utilizar la opción *... or push an existing repository from the command line* en donde solo tenemos que seguir las instrucciones indicadas en ésta opción. De manera que cuando escribamos `git push`, se nos pedirá el usuario y contraseña por línea de comandos. Tu usuario de Github aparece en la URL: https://github.com/nombre-usuario, en mi caso https://github.com/Nayeli-Luis, entonces mi usuario seria Nayeli-Luis. Por otro lado, la contraseña es el token que has creado previamente, NO es la contraseña de tu cuenta de Github.

Si entramos a GitHub (a través de un navegador) debemos ver el archivo que hemos subido, el mensaje cuando hicimos `commit` y desde hace cuánto tiempo lo subimos:


```{figure} ../img/git_github/04_archivo_github.png
---
height: 200px
name: 04_archivo_github
---
Archivo en GitHub.
```

Además, también podemos ver el status de los commits que realicemos y dónde se encuentran con `git log`y te aparecerá algo similar a esto:

```{figure} ../img/git_github/05_git_log.png
---
height: 150px
name: 05_git_log
---
Mensaje en terminal de git log.
```

En donde te la clave del `commit`, el autor quien lo llevó a cabo y la fecha.


Para conocer el status de todos tus archivos en general, podemos escribir en terminal:

```{code-block} bash
git status
```

:::{admonition} Para saber más
:class: attention
Éste capítulo es un resumen de parte del libro de <a href = "https://git-scm.com/book/en/v2">Git Pro</ao>
:::
