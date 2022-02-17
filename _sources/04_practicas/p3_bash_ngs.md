# Práctica 3. Manejo de datos de secuenciación con `Bash`.

:::{admonition} Objetivo
:class: important
* Que el estudiante practique el manejo de archivos y directorios con `bash`.
* Que el estudiante comience a familiarizarse con los formatos más comunes utilizados en la bioinformática.

:::

## Indicaciones 
La práctica está compuesta de cinco partes para repasar los comandos de Bash que se vieron en clase y se resuelve de manera **INDIVIDUAL**.

### Entregables

1. Los archivos se entregan en un directorio que deberá estar en su `GitHub`, corrobora que se encuentre toda la información.
2. **TODOS** los comandos utilizados, las líneas de código y/o outputs de terminal deberán entregarse en un archivo te texto plano en <a href = "https://www.markdownguide.org/basic-syntax/">Markdown</a>. El nombre del archivo será: `comandos_p03.md`. Y la estructura del archivo será la siguiente:


```{code-block} none
# Comandos de la Práctica 01
**Nombre(s) Apellido(s)**

## Parte I. 

**Respuesta 1:** Creación de directorios y archivos.
Comandos: 

**Respuesta 2:** Tipo de shell.
Comando:
[comando] [opciones] [argumentos]

Output:


**Respuesta 3:** Creación de directorios para proyecto bioinformático.

Comandos:
[comando] [opciones] [argumentos]

**Respuesta 4:**

...

## Parte II.
...

## Parte III.
...

## Parte IV.

...
```

:::{admonition} IMPORTANTE
:class: caution
Tanto el link de la carpeta como el archivo con los comandos debe enviarse a través del Classroom de la clase antes de que cierre la asignación
:::

## Parte I. 

**Pregunta 1**: Creación de directorios y archivo de comandos: Inicia la terminal y colócate en el directorio de tu *home* (`computadora@usuario:~/home/`) o del escritorio (`computadora@usuario:~/Desktop/`). Crea un directorio llamado `GenomicaComputacional` (sin tilde), ingresa en este nuevo directorio y crea uno nuevo que lleva la inicial de tu nombre, tu apellido en minúsculas y sin espacio, guión bejo, p03. Ejemplo: `nluis_p03`. Ahora, crea el archivo `comandos_p03.md`

**Pregunta 2**:  Indica qué tipo de shell tiene tu computadora. Si no recuerdas el comando, recuerda que posiblemente alguien ya preguntó eso alguna vez. Puedes visitar el siguiente sitio: <a href = "https://askubuntu.com/questions/590899/how-do-i-check-which-shell-i-am-using">How do I check whic shell I am using</a>

**Pregunta 3**:  Un proyecto bioinformático que se quiere publicar debe estar bien organizado y documentado para que éste se vuelva reproducible. Colócate dentro del directorio que creaste con tu inicial y apellido. Ahora crea **en una sola linea** los siguientes directorios para la organización de tu proyecto bioinformático: `data/`, `filtered/`, `raw_data/`, `meta/`, `scripts/`, `figures/` y `archive/`. Mueve los directorios necesarios para obtener la siguiente esctructura: `data/filtered` y `data/raw_data`.

**Pregunta 4**:  Visita el siguiente repositorio y contesta ¿A qué se debe el nombre y la organización de los directorios que acabamos de crear? [BioinfinvRepo](https://github.com/u-genoma/BioinfinvRepro/blob/master/Unidad2/Unidad2_Organizacion_proyecto_bioinf.md)

## Parte II. 

**Pregunta 1**:  Entra al directorio `scripts/`, crea un archivo de texto `delay.sh` y abrelo con un editor de texto desde la terminal para escribir las siguientes líneas de código:

:::{admonition} NOTA
:class: warning
Antes de continuar, verifica que tu ruta de bash es la misma que en el cuadro de código usando `which bash`, si obtuviste `/bin/bash` continúa. De lo contrario, modifica la primer línea con lo que se imprimió `#!<ubicación_bash>`. Como notaste, los caracteres `#!` antes de la ubicación del programa bash, son indispensables, a estos se les conoce como [shebang](https://es.wikipedia.org/wiki/Shebang).
:::

```
#!/bin/bash
echo "Después de la Parte I. necesito un descanso de exactamente 30 segundos."
```

**Pregunta 2**:  Dar permisos de ejecución. Deseas ejecutar el script, por lo que tienes que darle (al menos) al usuario permisos de ejecución.

**Pregunta 3**:  Verificar permisos. Verifica los permismos de `delay.sh`. Una vez que te aseguraste de que tiene permiso de ejecución, ahora puedes ejecutarlo de alguna de las dos formas que vimos en clase.

**Pregunta 4**:  Dar pausa de 30 seg. 03. Quieres que después de la segunda línea, haya una pausa de 30 segundos. Ya conoces el comando que permite *dormir* un proceso, si no recuerdas la unidad de tiempo que maneja, visita su manual `man <comando>`. Edita el archivo tomando como guía el siguiente cuadro de código. No olvides reportar el comando que agregaste: 

```
#!/bin/bash
echo "Después de la Parte I. necesito un descanso de exactamente 30 segundos."
# < AQUÍ VA EL COMANDO QUE PERMITE DORMIR POR 30 SEGUNDOS >
echo "Ya puedo continuar!"
```
**Pregunta 5**:  Imagina que en lugar de poner 30, escribiste 300. Hazlo y ejecutalo en *background*. Como no queremos esperar 5 minutos, *cancela* el proceso utilizando su PID.

## Parte III. 

En esta parte, trabajarás con secuencias genómicas del virus SARS-CoV-2 que provoca la enfermedad Covid-19. Si necesitas un contexto general de los datos, también puedes consultar el siguiente [video sobre Covid-19](https://www.youtube.com/watch?v=BtN-goy9VOY&feature=youtu.be). 

:::{admonition} NOTA IMPORTANTE
:class: warning
Para llevar a cabo ésta parte deberás

*  Tener descargados los archivos que se indica en la sección *¿De dónde obtenemos datos biológicos*  >> *Obtención de secuencias del NCBI*.

* Descargar los archivos `SRR10971381_R1.fastq.gz`, `SRR10971381_R2.fastq.gz` y `sarscov2_assembly.fasta.gz` que están disponibles en el <a href = "https://github.com/solnavss/Genomica_Computacional/tree/master/practica01">GitHub de la clase</a>. 
:::

**Pregunta 1**:  Resumen. Elabora un resumen de 120 palabras sobre la siguiente conferencia respecto a la [estructura molecular del SARS-Cov-2](https://www.youtube.com/watch?v=I0AbpnFP1g8). También puedes apoyarte en el siguiente [texto](https://www.nytimes.com/interactive/2020/04/03/science/coronavirus-genome-bad-news-wrapped-in-protein.html) publicado por The New York Times. El resumen deberá estar escrito en un archivo `SarsCov-2.txt` dentro del directorio creado para la práctica Ej. `~/home/GenomicaComputacional/mnavarro_p01/meta`

**Pregunta 2**:  Mueve los **ocho** archivos `sarscov2_genome.fasta`, `sarscov2_genome.gff3`, `splike_c.faa`, `splike_b.faa`, `splike_a.faa`, `SRR10971381_R1.fastq.gz`, `SRR10971381_R2.fastq.gz` y `sarscov2_assembly.fasta.gz` a tu directorio `data\raw_data`.

## Parte IV.

**Pregunta 1**: Ligas simbólicas. Realiza tres ligas simbólicas suaves de los archivos `splike_c.faa`, `splike_b.faa` y `splike_a.faa` en el directorio `data/filtered`.

**Pregunta 2**:  Dentro de `data/filtered` crea un nuevo archivo llamado `glycoproteins.faa`.

**Pregunta 3**:  Obten la primera línea de los tres archivos y repórtalas (en `comandos_p01.md`). 

**Pregunta 4**:  Usando el comando adecuado, redirecciona el contenido de los tres archivos `splike_*.faa` a `glycoproteins.faa` de tal forma que obtengas el orden siguiente: 

```
>pdb|6VYB|A Chain A, spike glycoprotein
MGILPSPGMPALLSLVSLLSVLLMGCVAETGTQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHST
QDLFLPFFSNVTWFHAIHVSGTNGTKRFDNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDSKTQSLLIVN
...(resto de la proteína)
>pdb|6VYB|B Chain B, spike glycoprotein
MGILPSPGMPALLSLVSLLSVLLMGCVAETGTQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHST
QDLFLPFFSNVTWFHAIHVSGTNGTKRFDNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDSKTQSLLIVN
... (resto de la proteína)
>pdb|6VYB|C Chain C, spike glycoprotein
MGILPSPGMPALLSLVSLLSVLLMGCVAETGTQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHST
QDLFLPFFSNVTWFHAIHVSGTNGTKRFDNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDSKTQSLLIVN
... (resto de la proteína)
```
**Pregunta 5**:  Mueve lo archivos `data/raw_data/splike_*.faa` al directorio `archive/`. ¿Qué pasó con las ligas simbólicas suaves?. 

:::{admonition} Nota
:class: note
Como te habrás dado cuenta algunos de los archivos que descargaste tienen una extensión `.gz` lo que quiere decir que estan comprimidos. Si abres el archivo con los comandos `less`, `more` o `cat` te darás cuenta que estan en binario. Inténtalo. Para poder acceder a ellos sin necesidad de descomprimirlos, puedes usar el siguiente ejemplo `zless archivo.gz | <comando> | <comando>`. 
:::

**Pregunta 6**:  Dentro del directorio `data/raw_data`, explora los archivos `sarscov2_genome.fasta` y `sarscov2_assembly.fasta.gz`. Ya que los exploraste. usa el comando adecuado para ver en la terminal las primeras 3 líneas de los archivos. Repórtalas. 

**Pregunta 7**:  Pudiste notar en los archivos que el nombre/header de las secuencias esta delimitado por el caracter '>'. Cuenta cuántos headers tienen ambos y reporta el número.

**Pregunta 8**:  De igual manera abre el archivo [.fastq](https://nayeli-luis.github.io/manual_bioinformatica/12_formatos.html) `SRR10971381_R2.fastq.gz` y obten las primeras 12 líneas. Repórtalas. Observa el patrón e identifica qué caracter te podría ayudar a obtener un conteo de las secuencias. Utiliza el patrón que elegiste para contar la cantidad de secuencias que hay. Repórtalo.

**Pregunta 9**:  Explica la diferencia entre los formatos `.faa`, `.fastqc` y .`fasta`: ¿Las secuencias hacen referencia a nucleótidos o aminoácidos? 

**Pregunta 10**: Abre el archivo [.gff3](https://nayeli-luis.github.io/manual_bioinformatica/12_formatos.html) de las siguientes formas `less sequence.gff3` y `less -S sarscov2_genome.gff3`. Observa las diferencias. Repórtalas en un enunciado. 

**Pregunta 11**:  Filtra el tercer campo del archivo `sarscov2_genome.gff3` por la categoría `gene` y reporta la cantidad de genes que tiene el archivo. ¿A qué corresponde el campo tres? ¿Cuál es la diferencia entre `gene` y `CDS` de acuerdo a la información proporcionada por la <a href = "https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md">documentación</a> del campo 3? 


## Parte V. 

**Pregunta 1**:  Cambia al directorio `figures/` y crea una liga simbólica suave del archivo `sarscov2_genome.gff3`

**Pregunta 2**:  Identifica cuántas categorías distintas existen en el campo 3 y cuántas veces aparecen. Redirecciona la salida a un archivo que se llame `barplot_data.txt`

**Pregunta 3**:  Limpia tu archivo `barplot_data.txt` de tal forma que sólo te queden las categorías que corresponden al campo 3.

**Pregunta 4**: Crea un script de python `gff_barplot.py` con los datos que obtuviste. Asegúrate de que el shebang corresponda a la ubicación de python en tu computadora. 

```
#!/Users/solouli/opt/anaconda3/bin/python

import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

# Crea el dataset con << tus datos obtenidos en barplot_data.txt >>
frecuencias = [3, 12, 5, 18, 45]
categorias = ['Categoría A', 'Categoría B', 'Categoría C', 'Categoría D', 'Categoría E']
categorias = [ '\n'.join(wrap(l, 11)) for l in categorias]

y_pos = np.arange(len(categorias))

# Gráfico de barras
plt.bar(y_pos, frecuencias)

# Nombres en el eje-x
plt.xticks(y_pos, categorias)

# Mostrar la gráfica
plt.show()
```

**Pregunta 5**:  Guarda la figura que obtuviste en `figures/`