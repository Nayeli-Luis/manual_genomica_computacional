# Guía de Markdown

:::{admonition} Objetivo
:class: tip
* Conocer la sintaxis de Markdown para dar formato a un archivo.
:::

::::{margin}
:::{admonition} Recursos
:class: tip
[Ésta](https://www.markdownguide.org/basic-syntax/) es la guia original de Markdown.
:::
::::

`Markdown` es un lenguaje de marcado ligero creado por Jhon Gruber, que consiste en dar formato a un texto mediante el uso de etiquetas. Es el lenguaje más utilizado para la documentación de código y tiene sus variantes como Rmarkdown y [MySt](https://myst-parser.readthedocs.io/en/latest/). De hecho, todo este manual está creado con `Markdown`. 

Ésta sección solo es una guía de referencia para que tengas a la mano las etiquetas que debes utilizar para darle formato a un texto. 

## Encabezados

El símbolo de numeral o gato o hashtag (`#`) indica los encabezados, el número de gatos que coloque es la jerarquía de los encabezados en cuestión. 

```
# Encabezado 1
## Encabezado 2
### Encabezado 3
#### Encabezado 4
##### Encabezado 5
###### Encabezado 6
```

Recuerda siempre dejar un espacio entre el gato (`#`) y la palabra de tu encabezado. 

## Negritas e italicas 

Para colocar palabras en negritas o cursivas se utilizan los asteriscos (`*`) o los guiones bajos (`_`). Por ejemplo: 

```
*Palabra 1 en italicas*
_Palabra 2 en italicas_

**Palabra 1 en negritas**
__Paabra 2 en negritas__

***Palabra 1 en negritas e italicas***
___Palabra 2 en negritas e italicas___

```

Lo anterior se vería de la siguiente forma: 

*Palabra 1 en italicas*
_Palabra 2 en italicas_

**Palabra 1 en negritas**
__Paabra 2 en negritas__

***Palabra 1 en negritas e italicas***
___Palabra 2 en negritas e italicas___

## Salto de línea

Para dar un salto de línea debes dejar una línea vacia en tu documento .md. Por ejemplo: 

```
-¿Después de tanto tiempo?-inquirió Dumbledore al ver las lágrimas sobre el rostro de Snape.

-Siempre.
``` 

Lo cual se ve de la siguiente forma:

-¿Después de tanto tiempo?-inquirió Dumbledore al ver las lágrimas sobre el rostro de Snape.

-Siempre.

## Citas 

Para escribir un parrafo como cita debes colocar un símbolo de mayor que al comienzo del texto, por ejemplo: 

```
> Primero pienso, luego escribo código. - Yo
```
Lo cual da como resultado: 

> Primero pienso, luego escribo código. -Yo


## Listas 
Existe dos tipos de listas: las ordenadas y las desordenadas. Para las listar ordenadas puede utilizar números o letras, mientras que, para las listas desordenadas los carácteres a utilizar son astericos (`*`), guiones medios (`-`) y símbolos de suma (`+`). 

```
# Ejemplo de lista ordenada 

1. azul 
2. rojo
3. verde 

# Ejemplo de lista desordenada
* azul
- rojo
+ verde
```

Esto da como resultado: 

Lista ordenada: 

1. azul 
2. rojo
3. verde 

Lista desordenada: 

* azul
- rojo
+ verde

## Código
Para dar formato a código se utilizan los acentos graves: (\`), esto se utiliza para escribir comandos de una sola línea, nombres de software y bloques de código. 

## Links/ URL

Para links o urls se debe utilizar: 

```
[Descripción](url)
```

Por ejemplo, colocaré el link de la facultad: 

```
[Facultad de ciencias](https://www.fciencias.unam.mx/)
```

Lo cual se ve de la siguiente manera: 
[Facultad de ciencias](https://www.fciencias.unam.mx/)

También puedes colocar links crudos encerrandolos en `<>`. 

## Imágenes

Para las imágenes se utiliza la siguente sintáxis: 

```
![Texto](ruta de tu computadora donde se encuentra la imagen "Título opcional")
```

El `Texto` es el texto que saldría en caso de que haya un error al cargar la imagen. 

Por ejemplo, el archivo .md se escribe lo siguiente: 

```
![Imagen de ejemplo](../img/bioinformatics3.png "Imagen de ejemplo")
```

Y sale lo siguiente: 

![Imagen de ejemplo](../img/bioinformatics3.png "Imagen de ejemplo")


