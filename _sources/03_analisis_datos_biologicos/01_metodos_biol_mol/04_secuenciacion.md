# Secuenciación del DNA
**Autora: M. Nayeli Luis-Vargas**

:::{admonition} Objetivo
:class: tip
* Conocer las diferencias entre las tecnologías de primera, segunda y tercera generación.
:::

## ¿Qué es secuenciar?

**Secuenciar** significa determinar el orden exacto de los pares de bases de los nucleótidos de un fragmento de DNA. Recuerda que el orden de pares de bases determina el orden de síntesis de los aminoácidos y por tanto, de la construcción de una proteína. Existen diversos métodos que nos permiten conocer la secuencia de pares de bases del DNA. Los métodos de secuenciación se han clasificado por generaciones, siendo las últimas las que tienen mayor precisión.

## Métodos de primera generación: Sanger

El método de Sanger, lo inventó Frederick Sanger en 1977, y fue la base fundamental para el desarrollo del Proyecto del Genoma Humano, de hecho, Sanger ganó el Nobel en 1980. Este método se basa en el proceso de replicación del DNA, es decir,  en la síntesis, de forma secuencial, de una hebra de DNA complementaria a una hebra de cadena simple. Se requiere de DNA polimerasa, un primer marcado, dNTPS (nucleótidos normalitos) y de unos nucleótidos especiales llamados **dideoxinucleótidos** (ddNTPs). Los dideoxinucleótidos también son conocidos como nucleótidos de parada, ya que carecen de un grupo -OH en la orientación 3', sin éste grupo se impide la adición de un nucleótido más, por lo que la actividad de la polimerasa se detiene.  Esto conlleva a que se obtengan fragmentos secuenciados de diferente tamaño, según donde se coloquen los dideoxinucleótidos.

El proceso sería el siguiente:

1. Se llevan a cabo cuatro reacciones distintas en tubos diferentes. Cada tubo contiene una mezcla del mismo DNA molde, DNA polimerasa, un primer marcado, los dNTPS normales y uno de los cuatro ddNTPs (es decir, A, T, G o C).
2. Se inicia la polimerazación con el primer marcado, y en cuando la polimerasa se encuentre a un ddNTPs, se detiene y se libera la cadena secuenciada. Éste comportamiento genera cadenas de diferentes tamaños.
3. Los fragmentos de DNA se analizan por electroforesis, es decir, tomando en cuenta su peso  molecular. De manera que, la lectura del gel (de abajo hacia arriba) nos dará la secuencia complementaria del DNA molde.
4. A partir de la lectura del gel de electroforésis se reconstruye la secuencia.

```{figure} ../img/sanger.png
---
height: 450px
name: Sanger
---
Método de secuenciación de Sanger.
```


::::{margin}
:::{admonition} Video: Sanger
:class: tip
Te recomiendo ver el siguiente video sobre el método de secuenciación por Sanger.
<a href = "https://www.youtube.com/watch?v=oeJoTZCRrvU&t=140s&ab_channel=BrandonOrtizCasas">Secuenciación Sanger: Conceptos básicos</a>
:::
::::

## Métodos de segunda generación (NGS)

::::{margin}
:::{admonition} Video: NGS
:class: tip
Te recomiendo ver el siguiente video sobre NGS
<a href = "https://www.youtube.com/watch?v=jFCD8Q6qSTM&ab_channel=AppliedBiologicalMaterials-abm">1) Next Generation Sequencing (NGS): - An Introduction</a>
:::
::::


A los métodos de segunda generación también se les conoce como métodos de secuenciación de nueva generación (*Next Generation Sequencing*, NGS) y es un grupo de tecnologías para secuencias gran cantidad de segmentos de DNA de forma masiva, en paralelo, en menor cantidad de tiempo y a un menor costo por base {cite}`Rubio2020`. Existen tres métodos principales para la secuenciación masiva: pirosecuenciación, secuenciación por síntesis y secuenciación por ligación. En donde la secuenciación por síntesis  es la más utilizada en los últimos años.
<br>

En general, todas las técnicas NGS siguen estos pasos:

1. Fragmentación del DNA y marcaje del DNA con primers o adaptadores que indica el punto de partida de la replicación.
2. Amplificación del DNA marcado por PCR.
3. Lectura de los fragmentos de DNA.
4. Alineamiento y análisis de datos

```{figure} ../img/ngs-illumina.png
---
height: 600px
name: ngs
---
Secuenciación de segunda generación por síntesis.
```

:::{admonition} Para saber más
:class: note
Para conocer más sobre los métodos NGS puedes consultar el artículo de <a href = "https://drive.google.com/file/d/1yRMEmjYNChjMwW020_fn9O5gs-lEXgC5/view?usp=sharing">Goodwin et al., 2016.</a>
:::

## Métodos de tercera generación
Los métodos de primera y segunda generación requieren que el tamaño del fragmento sea pequeño, además dependen de un paso previo de amplificación. Las tecnologías de tercera generación permiten secuenciar fragmentos de DNA de gran tamaño, una secuenciación monitorizada en tiempo real y secuenciar sin amplificar. El hecho de que se pueda secuenciar lecturas más largas, permite que el análisis y ensamble de genomas sea más sencillo. Sin embargo, a pesar de las ventajas mencionadas, tienen menor fidelidad en comparación con algunos métodos de segunda generación {cite}`Valderrama2020`. Actualmente existen tres métodos de tercera generación: secuenciación de en tiempo real de una sola  molécula (*Single-Molecule Real-Time*, SMRT) y tecnología de secuenciación por nanoporo (*Nanopore Sequencing Technology*, ONT) {cite}`Xiao2020`.  

## Plataforma de secuenciación
Una plataforma de secuenciación hace referencia al tecnología específica que va a secuenciar los fragmentos de DNA de una muestra. Con "tecnología específica", me refiero a la compañía que lleva a cabo la secuenciación. Cada plataforma de secuenciación se diferencia en el método que utiliza, el número de pares de bases promedio de cada lectura (fragmento de DNA), el costo, el tiempo de secuenciación (también conocido como tiempo de corrida) y la tasa de error.


## Referencias

```{bibliography}
:style: plain
```
