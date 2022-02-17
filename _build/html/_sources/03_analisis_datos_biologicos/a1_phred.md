# Score de calidad Phred
**Autora: M. Nayeli Luis-Vargas**

:::{admonition} Objetivo
:class: tip
* Comprender en qué consiste el score de calidad Phred.
:::

El score de calidad Phred es una medidad de la calidad de la identificación de las nucleobases generadas por la secuenciación de DNA. El score de calidad Phred es calculado a partir de la siguiente fórmula 

:::{admonition} Recuerda
:class: tip
El score de calidad de las secuencias en los archivos `FASTQ` se encuentran en la cuarta línea.

```{code-block} none
@ERR059938.60 HS9_6783:8:2304:19291:186369#7/2
GTCTCCGGGGGCTGGGGGAACCAGGGGTTCCCACCAACCACCCTCACTCAGCCTTTTCCCTCCAGGCATCTCTGGGAAAGGACATGGGGCTGGTGCGGGG
+
7?CIGJB:D:-F7LA:GI9FDHBIJ7,GHGJBKHNI7IN,EML8IFIA7HN7J6,L6686LCJE?JKA6G7AK6GK5C6@6IK+++?5+=<;227*6054
```
:::

```{math}
Q  = 10logP
```

En donde Q es el valor de calidad y es un número entero, mientras que P es la probabilidad de que la base en la secuencia sea incorrecta. 

|    Q (Score de calidad Phred) |  P (Probabilidad de que una base esté incorrecta)| Porcentaje de presición |
| ------------ | ----------------|-----------------------|
|    10      | 1 en 10| 90%|
|    20      | 1 en 100 | 99%|
|    30      | 1 en 1000 |99.9 % |
|    40      | 1 en 10,000 | 99.99%|
|    50      | 1 en 100,000| 99.999%|
|    60      | 1 en 1,000,000| 99.9999% |


El score de calidad va a depender de la codificación de la plataforma de secuenciación, sin embargo, la codificación estándar es la de Sanger/Illumina 1.8 +. En esta codificación se utilizan los caracteres de <a href = "https://support.illumina.com/help/BaseSpace_OLH_009008/Content/Source/Informatics/BS/QualityScoreEncoding_swBS.htm" >ASCII</a> del 33 al 73. Y cada uno de estos caracteres tienen un valor en el score Phred. Por ejemplo, el caracter signo de exlamación (!) tiene el valor 33 en ASCII y tiene un valor Q igual a 0. La siguiente figura muestra un ejemplo, donde se puede ver la secuencia, el código ASCII, el valor que tiene en ASCII y el valor de Q.

```{figure} images/intro_analisis_bioinfo/phred.png
---
height: 100px
name: phred
---
Representación del score Phred para Sanger/Illumina 1.8+
```

:::{admonition} Para saber más..
Sobre Phred y otras codificaciones en función de la plataforma de secuenciación puedes llegar <a href = "https://en.wikipedia.org/wiki/FASTQ_format">ésta</a> página de Wikipedia.
:::

Entonces, con todo esto, para decir que una base secuenciada tiene una buena calidad el valor de Q debe estar entre 30-40, esto implica que la tasa de precisión va del 99.9% al 99.99% , y en nuestra cuarta línea deben aparecer caracteres ASCII de ?, @ y letras mayúsculas desde la A-I.