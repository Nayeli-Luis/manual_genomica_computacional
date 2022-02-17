# Formatos de archivos
**Autora: M. Nayeli Luis-Vargas**

A lo largo de el análisis de datos de origen biológico te vas a encontrar con diferentes formatos de los archivos resultantes de la secuenciación de tus muestras o de un proceso bioinformático. Por tanto, es importante que conozcas el tipo de información que guarda los principales formatos con los que te puedes encontrar.

## GENBANK

Es el formato de archivo más antiguo y clásico. Sus extensiones son `.gb`, `.gbff`, `.genbank`. Está diseñado para que sea fácilmente entendido por seres humanos. Aquí un ejemplo: 

```{code-block} none
LOCUS       CP010822             2158963 bp    DNA     circular BCT 19-OCT-2015
DEFINITION  Thermus aquaticus Y51MC23, complete genome.
ACCESSION   CP010822
VERSION     CP010822.1
DBLINK      BioProject: PRJNA274060
            BioSample: SAMN02441811
KEYWORDS    .
SOURCE      Thermus aquaticus Y51MC23
  ORGANISM  Thermus aquaticus Y51MC23
            Bacteria; Deinococcus-Thermus; Deinococci; Thermales; Thermaceae;
```

## FASTA

Es un formato de texto plano que contiene las secuencias crudas, este formato es el que otorgan las plataformas de secuenciación. Puede tener las siguientes extensiones: `.faa`, `.fna`, `.fasta`. El formato es: 

* Un encabezado por secuencia que inicia con el símbolo mayor que (>) y que contiene texto que puede ser el nombre de la secuencia, una descripción, etc.
* La secuencia tal cual

Aquí un ejemplo: 

```{code-block} none
>NZ_CP010822.1 Thermus aquaticus Y51MC23 chromosome, complete genome
GTGGCCTTGACGCACGAGGCGGTCTGGCAGCACGTTCTGGAGCACATCCGCCGCAACATCACCGAGGTGGAGTACCACAC
CTGGTTTGAAAGGATCCGCCCCCTGGGTATCCGGGAAGGGGTTTTGGAGCTGGCGGTGCCCACCTCCTTCGCCCTGGACT
GGATCAAGCGGCACTACGCCCCCCTGATCCAGGAGGCTTTAGGCCTCCTGGGGGCCCAGGTACCCCGCTTTGAGCTTTTG
GTGGTGCCCGGAGCCGCCCAGCCGGTCCAGGTGGACATCTTCCAGGCCGTCCCCCAGGCCGACCAGGGGAAGTCCAAGCT
CAACCCCAAGTACACCTTTGAGAACTTCGTGGTGGGGCCCAACAACAACCTGGCCCACGCCGCGGCCGTGGCCGTGGCCG
AGTCGCCCGGCAAGGCCTACAACCCCCTTTTCATCTACGGGGGGGTGGGCCTGGGCAAGACCCACCTCATGCACGCCGTG
GGCCACTCGGTAGCCAAGCGGTTCCCCAGCCTCAAGATTGAGTACGTCTCCACCGAAACCTTCACCAACGAGCTCATCAA
CGCCATCCGCGAGGACCGCATGGCGGAGTTCCGGGAGCGGTACCGCTCCGTGGACCTCCTCCTGGTGGACGACATCCAGT
TCATCGCCGGCAAGGAAAGGACGCAGGAGGAGTTCTTCCACACCTTCAACGCCCTCTTTGAGGCCCACAAGCAGATCATC
```

## FASTAQ

<!-- Hacer un anexo del score de Phred-->

Es una variante del formato FASTA, solo que tiene asociado datos sobre la calidad de cada secuencia. Los archivos con formato FASTAQ consisten en 4 secciones: 

1. Un encabezado por secuencia que inicia con arroba (@), seguido por el ID de la secuencia y más texto opcional como la descripción. 
2. La segunda sección contiene la secuencia, generalmente solo utiliza una línea. 
3. la tercera línea inicia con símbolo más (+) y puede contener texto opcional. 
4. LA cuarta contiene los valores de calidad codificados en caracteres <a href = "https://www.ascii-code.com/" >ASCII</a> y tiene la misma longitud que la secuencia. Cada caracter representa un número y la codificación puede ser diferente, en general se utiliza el score de calidad Phred. Para entender en qué consiste el score de calidad Phred puedes leer el anexo de éste manual *Score de calidad Phred*.

De manera que los archivos FASTAQ se pueden ver de la siguiente forma: 

```{code-block}
@ERR059938.60 HS9_6783:8:2304:19291:186369#7/2
GTCTCCGGGGGCTGGGGGAACCAGGGGTTCCCACCAACCACCCTCACTCAGCCTTTTCCCTCCAGGCATCTCTGGGAAAGGACATGGGGCTGGTGCGGGG
+
7?CIGJB:D:-F7LA:GI9FDHBIJ7,GHGJBKHNI7IN,EML8IFIA7HN7J6,L6686LCJE?JKA6G7AK6GK5C6@6IK+++?5+=<;227*6054

```


## GFF/GTF
Los formatos de *General Feature Format* (GFF) y *General Transfer Format* (GTF), 
son archivos que contienen las anotaciones de los genes después de haber llevado a cabo un ensamble, donde cada línea corresponde a un gen o un objeto. Existen varias versiones de los archivos con formato GFF y en particular, un archivo GTF es idéntico a un archivo GFF versión 2. Estos archivos contienen nueve columnas separadas por tabuladores que arrojan información sobre: el nombre de la secuencia, la fuente de procedencia de la anotación, la característica de gen, los nucleótidos de inicio del gen , los nucleótidos de  fin del gen, el grado de confianza, la hebra de DNA que se transcribe, la fase de anotación de los codones y  una columna con otros atributos del gen. 


Aquí un ejemplo de un archivo con formato GTF: 

```{code-block} none
#gtf-version 2.2
#!genome-build ASM139977v1
#!genome-build-accession NCBI_Assembly:GCF_001399775.1
#!annotation-date 12/11/2020 01:41:48
#!annotation-source NCBI RefSeq
NZ_CP010822.1 RefSeq  gene  7 1326  . + . gene_id "TO73_RS00005"; transcript_id ""; gbkey "Gene"; gene "dnaA"; gene_biotype "protein_coding"; locus_tag "TO73_RS00005"; old_locus_tag "TO73_0001"; 
```

A continuación se describe cada columna: 

 
`[seqname]`
: Nombre de la secuencia, usualmente es el identificador del cromosoma en donde se encuentra el gen. 

`[source]`
: Etiqueta que indica la fuente de la cual procede la anotación, puede ser el nombre del programa de predicción o la base de datos. 

`[feature]`
: Característica de la secuencia anotada puede ser: “<a href = "https://www.uniprot.org/help/cds_protein_definition#:~:text=A%20CoDing%20Sequence%20(CDS)%20is,ends%20at%20a%20STOP%20codon.">CDS</a>”, “start_codon”, “stop_codon”, "gene".

`[start]` y `[end]`
: Indican los nucleótidos de inicio y final del gen.

`[score]`
: Indica el grado de confianza en la existencia y las coordenadas del objeto (gen). El valor no tiene una escala global, pero puede tener importancia relativa cuando en [source] se indica el programa utilizado para hacer la predicción, si es así se puede usar un número, de lo contrario puede reemplazarse por un punto. 
 
`[strand]`
: Puede representarse con signo más (+) para forward ó menos (-).

`[frame]`
: Se representa como 0, 1 o 2. 0 indica que el objeto comienza con un codón completo en la base 5’. 1 significa que hay una base extra antes del primer codón completo (la tercera base de un codón anterior) y 2 significa que hay dos bases extra (la segunda y la tercera base de un codón anterior) antes del primer codón completo.

`[attribute]`
: Una lista separada por punto y coma (;) de otros atributos del gen como un identificador global del gen, un identificador global del transcrito, entre otros.

:::{admonition} Paraq saber más...
:class: note
sobre los archivos con formato `GFF` puedes visitar la documentación en la siguientes páginas: 

* <a href = "http://gmod.org/wiki/GFF2" >GFF versión 2</a>

* <a href = "https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md" >GFF versión 3</a>
:::


## SAM/BAM
Los formatos SAM/BAM son conocidos como mapas de alineamiento de secuencias (*Sequence Alignment Maps*). Estos archivos representan los resultados de alineamiento de un FASTQ con un archivo FASTA de referencia y describe las alienaciones individuales por pares que se encontraron. Diferentes algoritmos pueden crear alineamientos (archivos SAM/BAM). La diferencia entre una archivo SAM y uno BAM, es que el BAM es el formato binario del SAM, es decir, es más pequeño y necesita un interprete para poder ser leído por humanos.

Visión de un archivo BAM:

```{code-block} none
MT_orang  0 MT_human  577 60  14M2D4M3I37M1D85M1D232M1I559M1D6M1I550M1D2M1D146M2I3M1D3M1D132M1D3M1I40M3I13M1D1M1D335M3I4M1D3M2D342M1D52M1I13M3I1M2D52M1I592M1D3M1I485M1D5M1I974M3I4M3D230M1D59M1D156M1D31M1I98M1I26M14I329M3I7M3D1203M1D4M1I70M1D345M1D9M1I398M7I8M8I1M1I9M3I2M1I2M1D390M1I5M1D193M1I6M1D195M1D7M1I1826M1D10M1I1256M1D49M1D157M3D5M3I48M2I1M1I3M3D1203M1I2M2D1M1I44M2D2M1I2M1I38M2D16M2I2079M1I5M1D50M1D3M1I43M5I57M1I54M4D19M1I39M2D8M1I7M1I22M1I5M1I4M1D5M1I2M2D29M2I20M1D13M2I1M1D8M1D45M1D15M1I5M2D17M1D56M1D2M1I131M1I38M474S  * 0 0 GTTTATGTAGCTTATTCTATCCAAAGCAATGCACTGAAAATGTCTCGACGGGCCCACACGCCCCATAAACAAATAGGTTTGGTCCTAGCCTTTCTATTAGCTCTTAGTGAGGTTACACATGCAAGCTCTCAACAACCCTACCCCATCAACCCAACAAAATCCAATTTTTATCTTTAGGCTATGTGCACTTTCAACAGGCACCCCTCAACTAACACAATCTCCTTCTTATCCCACCCACCAACCCCCCCCCCCCCTTCCTCCCTCTTTCTCCATTTTCCCCACAAACACCGCTACTACCCCCACACCCCAGACCAACCCAACCCAAAAGACACCCCGCACG * NM:i:2322 ms:i:18279  AS:i:18198  nn:i:0  tp:A:P  cm:i:342  s1:i:3187 s2:i:0  de:f:0.1405 rl:i:0
```

## VCF

El formato VCF (*Variant Call Format*) es un archivo delimitado por tabuladores y describe la variación de alineaciones con respecto a una referencia. Este archivo se genera a partir de un archivo BAM. Las extensiones de éste formato son `.vcf`, `.bcf`. 

Visión de un archivo VCF

```{code-block} none
#CHROM POS ID REF ALT QUAL FILTER INFO FORMAT NA00001 NA00002 NA00003
20 14370 rs6054257 G A 29 PASS NS=3;DP=14;AF=0.5;DB;H2 GT:GQ:DP:HQ 0|0:48:1:51,51 1|0:48:8:51,51 1/1:43:5:.,.
20 17330 . T A 3 q10 NS=3;DP=11;AF=0.017 GT:GQ:DP:HQ 0|0:49:3:58,50 0|1:3:5:65,3 0/0:41:3
20 1110696 rs6040355 A G,T 67 PASS NS=2;DP=10;AF=0.333,0.667;AA=T;DB GT:GQ:DP:HQ 1|2:21:6:23,27 2|1:2:0:18,2 2/2:35:4
20 1230237 . T . 47 PASS NS=3;DP=13;AA=T GT:GQ:DP:HQ 0|0:54:7:56,60 0|0:48:4:51,51 0/0:61:2
20 1234567 microsat1 GTC G,GTCT 50 PASS NS=3;DP=9;AA=G GT:GQ:DP 0/1:35:4 0/2:17:2 1/1:40:3

```

El significado de cada columna es el siguiente: 

`[CHROM]`
: Identificador del genoma de referencia. Todas las entradas para un CHROM específico deben formar un bloque dentro del archivo. 

`[POS]`
: La posición de referencia, las posiciones se ordenan numéricamente en orden creciente dentro de cada secuena de referencia CHROM. 

`[ID]`
: Lista de identificadores únicos separados por punto y coma. 

`[ALT]`
: Lista separada por comas de los alelos alternativos que no son de referencia invocados en al menos una de las muestras. 

`[QUAL]`
: Puntaje de calidad. 

`[FILTER]`
: PASS si la posición ha pasasado todos los filtros. De lo contrario se arroja una lista separada por punto y coma para los filtros que fallan.

`[INFO]`
: Serie de claves cortas separadas por punto y coma con valores opcionales en el formato <clave> = <datos> [, datos]. 


:::{admonition} Para saber más...
:class: caution
Para saber con más detalle qué significa cada parámetro de los archivos BAM/SAM y VCF te recomiendo leer con detenimiento los documentos de la página <a href = "https://samtools.github.io/hts-specs/">*SAM/BAM and related specifications*</a>.
:::
