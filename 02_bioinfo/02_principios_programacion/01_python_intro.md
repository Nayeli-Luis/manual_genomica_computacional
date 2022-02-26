# Introducción a Python
**Autora: M. Nayeli Luis-Vargas**

:::{admonition} Objetivo
:class: important
* Que el estudiante conozca qué es Python y cómo instalarlo.
:::

Python es un leguaje de programación de alto nivel, es decir, que su lenguaje es más parecido al que tenemos los humanos que al que tienen las máquinas. Es fácil de enteder y por tanto, fácil de leer y escribir. 

Actualmente, Python es utilizado en diversas áreas de la computación como en el desarrollo de aplicaciones, videojuegos, así como en el análisis de datos masivo. Además cuenta con una enorme comunidad y gran cantidad de paquetes que nos facilitan la vida (como `conda` y `pip`). En ésta sección vamos a ver la sintaxis básica de Python. 

## Instalación de Python

### Entornos globales de Python

* Python común (*stock Python*): Es el Python que se instala en el sistema operativo y se puede usar el interprete del lenguaje desde la consola del mismo sistema operativo. Este lo puedes descargar desde <https://www.python.org/>, además el gestor de paquetes es local con `pip`, es decir, `pip` solo gestiona paquetes de Python. 

* Python a través de un sistema de gestión de paquetes (como `conda`): En este caso, `Conda` gestiona paquetes para toda la pila de software (c++, R, Git) requerida por los usuarios, incluyendo Python y varias paqueterías. Además, `conda` puede cambiar y administrar múltiples entornos virtuales con diferentes versiones de Python si es necesario. `conda` tiene dos instaladores Miniconda y Anaconda, la diferencia entre `conda`, Miniconda y Anacoda son: 

```{figure} ../img/python/conda_mini_ana.png
---
height: 300px
---
Diferencias entre conda, Miniconda y Anaconda. 
```

:::{admonition} Recomendación
:class: caution
Instala Anaconda: <https://repo.anaconda.com/>, si tienes poco espacio entonces Miniconda: <https://docs.conda.io/en/latest/miniconda.html>
:::

## ¿Y luego?: Aprende a usar Python

Una vez que tengas instalado Anaconda puedes usar el **interprete**, es decir, abrir la terminal de tu computadora y teclear **python**, y te aparecerá algo similar a esto: 


```{figure} ../img/python/interprete.png
---
height: 300px
name: interprete
---
Interprete de Python
```
Como puedes notar, la línea comienza con >>>, es aquí donde puedes escribir tu código en Python. 

También puedes utilizar un modo interactivo (<a href = "https://es.wikipedia.org/wiki/IPython">IPython</a>) como Jupyter Notebook. Jupyter Notebook es una aplicación web que te permite crear y compartir documentos que contienen código, ecuacione, visualizaciones y texto. Para crear una libreta de Jupyter Notebook, solo debes escribir en una nueva terminal (NO en el interprete de Python) `jupyter-notebook`. Te abrirá una ventana en tu navegador que te mostrará los archivos de tu computadora: 

```{figure} ../img/python/jupyter-notebook.png
---
height: 300px
name: jupyter-botebook
---
Jupyter Notebook
```
Aquí podrás moverte como si fuera el gestor de archivos de tu computadora y crear una nueva libreta dando click en el boton `New` > `Python 3`, que se encuentra en lado superior derecho. Aquí es donde podrás escribir código, para luego guardarlo y visualizarlo. 


