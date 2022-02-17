# Flujo de trabajo para análisis de genomas
**Autoras: M. Nayeli Luis-Vargas y Marisol Navarro**

:::{admonition} Objetivo
:class: tip
* Conocer el flujo de trabajo general que se lleva a cabo en un análisis genomico, así como las principales herramientas bionformáticas utilizadas en cada paso. 
* Comprender los archivos input y output conseguidos en cada paso del proceso.
:::

Cuando hablamos de un análisis genómico, nos referimos al ensamble del genoma de un organismo. Después de secuenciar nuestras muestras, recibimos un archivo de texto plano con los fragmentos de DNA (que llamamos lecturas) correspondientes al organismo en cuestión. Estos fragmentos deben ser ensamblados, es decir, unidos como si se tratará de armar un rompecabezas, con el fin de conocer la composición genética del organismo que nos interesa. A partir de un genoma ensamblado podemos saber que tipo de genes tiene, para qué protéina codifican o podemos comparar su composición genética con la de otro organismo (organimos de referencia) y así identificar variaciones. 

Los fragmentos de DNA obtenidos a partir del secuenciador son conocidos como lecturas y cada plataforma de secuenciación produce distitnos tamaños de estos. 

El proceso para ensamblar un genoma se muestra en la siguiente figura (da click en ésta para que puedas visualizarla mejor): 

```{figure} images/intro_analisis_bioinfo/workflow-genomic.png
---
height: 750px
---
Flujo de trabajo en un análisis genómico.
```


## Análisis de calidad

:::{admonition} Archivos
:class: warning
**Archivo input**: Archivo `.fastq` obtenido del secuenciador.
<br>
**Archivo output**: No hay archivo como tal, sino un reporte en `HTML` que indica la calidad de lase secuencas.
:::

El proceso de secuenciación puede tener algunos errores, algunos de éstos pueden ser: 

* La variación en la preparación de la muestra
* Algun tipo de contaminación 
* Duplicados por PCR
* Recombinación
* Amplificación selectiva
* Error por sustitución de bases 
* Inserciones y deleciones

De manera que es importante saber si nuestras secuencias tienen una calidad aceptable para poder continuar con su análisis. El software màs utilizado para llevar a cabo éste proceso es <a href = "https://www.bioinformatics.babraham.ac.uk/projects/fastqc/"></a> `FASTQC`.

### `FastQC` 

Tiene como objetivo proporcionar una manera simple de hacer algunas comprobaciones de control de calidad de datos de secuencias procedentes de metodologías de secuenciación de alto rendimiento. En el software se ingresa un archivo `.fastq` y a partir de éste arroja una reporte en `HTML` el cual indica si los datos tienen algún problema de calidad que deba ser tomado en cuenta antes de realizar cualquier análisis posterior.

Las principales funciones de FastQC son:

* Proporcionar una visión general y rápida que identifique en qué áreas puede haber problemas.
* Gráficos y tablas para evaluar rápidamente los datos.
* Operación fuera de línea para permitir la generación automática de informes sin ejecutar la aplicación de forma interactiva.

:::{admonition} Intepretación del reporte de FASTQC
Para saber cómo se interpretan los resultados del reporte arrojado por FASTQC puedes ver el vídeo <a href = "https://www.youtube.com/watch?v=bz93ReOv87Y">Using FastQC to check the quality of high throughput sequence</a>
:::

## Limpieza

:::{admonition} Archivos
:class: warning
**Archivo input**: Archivo `.fastq` obtenido del secuenciador.
<br>
**Archivo output**: Archivo `.fastq` "limpio".
:::

Durante éste paso se eliminan los adaptadores que se colocaron durante la secuenciación, así mismo pueden eliminarse secuencias sobrerrepresentadas o hacer algún corte en donde la secuencia haya reflejado una mala calidad. Existen diversas herrameintas para llevar a cabo esta limpieza desde un archivo `.fastq`. Algunas de éstas herramientas son: 

* <a href = "http://www.usadellab.org/cms/?page=trimmomatic">Trimmomatic</a>
* <a href = "https://cutadapt.readthedocs.org/en/stable/">CutAdapt</a>
* <a href = "https://github.com/linneas/condetri">Condetri</a>
* <a href = "http://erne.sourceforge.net">ERNE-filter</a>
* <a href = "http://hannonlab.cshl.edu/fastx_toolkit/download.html">FASTX-tools</a>
* <a href = "http://prinseq.sourceforge.net">PRINTSEQ</a>
* <a href = "https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/">Trimgalore</a>

## Ensamble

Después de los procesos mencionados (calidad y limpieza de las secuencas) el ensamble del genoma puede llevarse a cabo de dos maneras: a partir de un genoma de referencia o sin un genoma de referencia, es decir *de novo*. ¿En qué se diferencian? Imagina que estás armando un rompecabezas, si tienes la imagen del rompecabezas (la que viene en la caja), todo será más sencillo, puedes puedes ir comparando las piezas con la imagen y darte una idea. Ahora, imagina que no tienes la imagen...Se vuelve más complicado porque no tienes idea de cómo luce, ni que figuras tiene, ni los patrones ni nada de nada. Si estuvieras en éste caso, pues tendrás que buscar otras estrategias.

### Ensamble sin genoma de referencia: *de novo*

:::{admonition} Archivos
:class: warning
**Archivo input**: Archivo `.fastq` "limpio".
<br>
**Archivo output**: Archivo `.fasta`.
:::

En general, el ensamble *de novo* se basa en la simple suposición de que los fragmenos de DNA (las lecturas) con bastante similitud se originan de la misma posición dentro del genoma. De ésta manera, la similitud entre secuencias de DNA se usa para conectar fragmentos individuales en secuencias contiguas más largas, denominadas *contigs* (secuencias consenso obtenidas a partir del ensamblaje de los fragmentos de DNA).

```{figure} images/intro_analisis_bioinfo/ensamble_de_novo.png
---
height: 350px
---
Proceso general en un ensamble *de novo*.
```

En el ensamble *de novo* las lecturas de corta longitud (como las que se obtienen a partir de tecnologías de secuenciación masiva) constituyen un problema cuando hay repeticiones en el genoma, es decir, segmentos de DNA que aparecen más de una vez a lo largo del genoma. Cuando una lectura proviene de una región repetitiva, y es más corto que la región completa, no se sabe con certeza de cuál copia de la repetición se obtuvo. Es por ello que durante el ensamblaje, se pueden crear falsas uniones en las regiones de repetición. Para evitar este problema se han empleado algunas estrategias computacionles, éstas son: 

`OLC (*Overlap-Layout-Consesus*)`
: Éste método identifica todos los pares de lecturas que se solapan lo suficientemente bien y organiza ésta información en un grafo (una red), en la cual hay  uno nodo por cada par de lecturas de ellos y un enlace. Ésta estructura permite que se tome en cuenta la relación global entre las lecturas. De ésta manera, se definen caminos que corresponde con los segmentos del genoma que están siendo ensamblados. Se reconstruye el genoma mediante la búsqueda de un único camino que atraviese todos los nodos de una sola vez  {cite}`Aguilar-Bultet2015`. 

`Gráficos De Brujin`
: Descompone las lecturas en k-meros, <a href = "https://es.wikipedia.org/wiki/K-mero#Ensamblaje_de_secuencias">los k-meros</a> son subcadenas de longitud *k* contenidas dentro de una secuencia biológica. De manera que se modela la relación entre subcadenas exactas de logitud *k* dentro de las lecturas. En el grafo de De Brujin los nodos son k-meros y los enlaces indican qué k-meros adyacentes se solapan por *k-1* letras, por lo que la longitud del k-mero se correlaciona con la longitud del solapamiento que el ensamblador es capaz de detectar. La mayoría de los ensambladores usan la información global de las lecturas para refinar la estructura del gráfico, resolver repeticiones y eliminar patrones no consistentes. Además, incorporan métodos de corrección de errores para mejorar la calidad del ensamblaje {cite}`Aguilar-Bultet2015`. 

::::{margin}
:::{admonition} Para entender mejor
:class: warning
En qué consiste un grafo y cómo funciona el método OLC puedes ver el vídeo <a href = "https://www.youtube.com/watch?v=yPJ7yHRk2OI&ab_channel=BenLangmead">ASD1: Overlap graphs</a>.
<br>
Cómo funciona el algoritmo de De Brujin puedes ver el vídeo: <a href = "https://www.youtube.com/watch?v=TNYZZKrjCSk&ab_channel=BenLangmead">ADS1: Gráficos de Brujin y paseos eulerianos</a>.
:::
::::

#### Software para ensamble de genomas *de novo*

Los softwares más utilizados para el ensamble son <a href = "https://www.ebi.ac.uk/~zerbino/velvet/">`Velvet`</a> y <a href = "https://kbase.us/applist/apps/kb_SPAdes/run_SPAdes/release?gclid=CjwKCAiAvriMBhAuEiwA8Cs5ldzaiatuD4vl4JH2BCsz02ajLpdv7YHc2wdqiuMQn--w-Xq4uCa58xoCtlwQAvD_BwE"> `SPAdes`</a>. Sin embargo puedes consultar <a href = "https://bioinformaticshome.com/tools/wga/wga.html">ésta página</a> para consultar todas las herramientas que actualmente existen para ensamblar un genoma.

### Ensamble con genoma de referencia
:::{admonition} Archivos
:class: warning
**Archivos input**: Archivo `.fastq` "limpio" y archivo `.fasta` que es el genoma de referencia.
<br>
**Archivo output**: Archivo `.sam`/`.bam`/`.cram`.
:::

Cuando se tiene un genoma de referencia, se hace un mapeo o alineamiento de los fragmentos de DNA de nuestra muestras con un genoma de referencia, es decir, con un genoma previamente ensamblado y cuyas secuencias podemos descargar del NCBI o que podemos obtener de estudios anteriores. A partir de éste mapeo se hace el ensamble. Cuando se hace un ensamble de éste tipo, uno de los objetivos puede ser comparar ambos genomas, ¿En qué genes se diferencian? y hacer un estudio conocido como llamado de variantes genéticas *variant calling*. La llamada de variantes implica identificar polimorfismo de un solo nucleótido (SNPs) y pequeñas inserciones y deleciones de los datos.


## Anotación de genes

:::{admonition} Archivos
:class: warning
**Archivo input**: Archivo `.fasta`.
<br>
**Archivo output**: Archivo `.gff`/`.gtf`.
:::

La anotación de genes es el proceso de identificar cualquier elemento funcional a lo largo de la secuencia. La anotación da significado al genoma al proporcionar la ubicación y la función de genes y regiones reguladoras. Los programas más utilizados actualmente para anotar genes en procariontes son <a href = "https://github.com/tseemann/prokka">`Prokka`</a> y <a href = "https://rast.nmpdr.org/">`RAST`</a>.

:::{admonition} Recursos recomendados
* Artículos: <a href = "https://drive.google.com/file/d/1lxPBCvvzzv5f4lsO5uT6x3PGtydzhpQJ/view?usp=sharing">Sequence assembly demystified</a> y <a href = "https://drive.google.com/file/d/1gMNXuJLjRKatzLcOqTe2zm_SL4QzbZ7R/view?usp=sharing">Twelve quick steps for genome assembly and annotation in the classroom</a>
* Libro: <a href = "https://drive.google.com/file/d/15DAnHmjR8I9V4vRerBmGxg6MyDYvxui2/view?usp=sharing">Next Generation Sequencing and Sequence Assembly</a>
:::

## Referencias
```{bibliography}
:style: unsrt
```