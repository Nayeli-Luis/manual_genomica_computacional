# ¿De dónde obtenemos datos biológicos?
**Autoras: M. Nayeli Luis-Vargas y Marisol Navarro**

Como vimos en una sección anterior, podemos obtener secuencias de DNA mediante experimentos, otra opción es el uso de bases de datos.

## Repositorios de secuencias de DNA, RNA y/o proteínas

::::{margin}
:::{admonition} Rercuerda que
:class: caution
En este curso nos enfocamos al análisis de secuencias de DNA.
:::
::::

El *International Nucleotide Sequence Database Collaboration* (<a href = "https://www.insdc.org/">INSDC</a>) ha hecho varios esfuerzos por mantener las secuencias de DNA originales de diversas investigaciones. Los miembors de éstas organizaciones son: 

*  <a href = "https://www.ncbi.nlm.nih.gov/">NCBI</a>: National Center for Biotechnology Information
*  <a href = "https://www.ebi.ac.uk/">EMBL</a>: European Molecular Biology Laboratory
* <a href = "https://www.ddbj.nig.ac.jp/index-e.html">DDBJ</a>: DNA Data Bank of Japan

El INDSC propuso ciertas reglas para almacenar información contenida en DNA. Y quienes cumplen con estas reglas son los siguientes repositorios:

* <a href = "https://pubmed.ncbi.nlm.nih.gov/23193287/">Gene Bank</a>: contiene toda la información de secuencias de DNA anotadas e identificadas. 
* <a href = "https://www.ncbi.nlm.nih.gov/sra">SRA</a> (*Short Read Archive*): que contiene mediciones de experimentos de secuenciación de alto rendimiento. 
* <a href = "https://www.uniprot.org/">UniProt</a> (*Universal Protein Resource*): Repositorio de secuencias de proteínas. 
* <a href = "https://www.rcsb.org/">Protein Data Bank</a>: Repositorio de información estructural 3D de macromoléculas biológicas.  

:::{admonition} Más repositorios
:class: note
Si quieres saber de más sitios donde puedes obtener datos de origen biológico te recomiendo el artículo de <a href = "https://drive.google.com/file/d/12B8FbkLM1hBVWFrIJrzraKwaopvmP6ND/view?usp=sharing">Database resources of the National Center for Biotechnology Information</a> (2019) de Sayers y colaboradores.
:::

## Obtención de secuencias del NCBI

En ésta sección aprenderás a descargar secuencias desde el *National Center for Biotechnology Information* (NCBI). Te sugerimos llevar a cabo el ejercicio, pues las secuencias que descargues las necesitarás para realizar la *Práctica 3*: 

### Descargar secuencias de DNA

* Entra a la página del NCBI <https://www.ncbi.nlm.nih.gov/>. Escribe en el buscador el organismo que deseas, en este caso buscaremos el genoma del virus que provocó la pandemia actual. Da click en "buscar".


```{figure} ../img/intro_analisis_bioinfo/ncbi1.png
---
height: 350px
---
```

* Te redirigirá a otra página con los datos del organismo. Da click en el recuadro que dice "Reference genome". 

```{figure} ../img/intro_analisis_bioinfo/ncbi2.png
---
height: 300px
---
```

*  En seguida te redirigirá a una página con un formato de GeneBank (en el siguiente apartado vemos los formatos). Da clcik en "Send to:" y selecciona las opciones "Complete Record" y "File". Te desplegará un pequeño apartado que dice "Format" primero seleccionaras el que diga `FASTA` y darás click en "Create File". Te descargará un archivo con nombre `sequence.fasta`. Repetirás el proceso para ahroa descargar un archivo con formato `GFF3`, tendrás un segundo archivo con nombre `sequence.GFF3`. Renombra los archivos `sequence.fasta -> sarscov2_genome.fasta` y `sequence.gff3 -> sarscov2_genome.gff3`.

```{figure} ../img/intro_analisis_bioinfo/ncbi3.png
---
height: 350px
---
```

### Descargar secuencias de proteínas

* Entra a la página del NCBI <https://www.ncbi.nlm.nih.gov/g>. Escribe en el buscador la proteína  que deseas, en este caso buscaremos una proteína del virus que provocó la pandemia actual (*sars cov-2 spike ectodomain*). Luego, despliega el menú en donde dice "All Databases" y selecciona "Structure". Da click en "buscar".

```{figure} ../img/intro_analisis_bioinfo/ncbi4.png
---
height: 350px
--- 
```

* Da click en la opción 2: *Structure of the SARS-CoV-2 spike glycoprotein (closed state)[VIRAL PROTEIN]* . Te redirigirá a otro sitio y ahí da click en "Download sequence data". 

```{figure} ../img/intro_analisis_bioinfo/ncbi5.png
---
height: 350px
--- 
```

* Descargarás las cadenas A, B y C. Para esto:
    1. selecciona la cadena, 
    2. da click en "Send to:", 
    3. Selecciona "File", 
    4. seleccciona en archivo `FASTA` y "default order" y, por último 4. Click en "create file". 
    5. Renombra los archivos que descargaste, el de la cadena A como `splike_a.faa`, el de la cadena B como `splike_b.faa` y el de la cadena C como `splike_c.faa`

:::{admonition} Atención
:class: caution
Debes seleccionarlas y descargarlas una por una, para que al final tengas tres archivos.
:::

```{figure} ../img/intro_analisis_bioinfo/ncbi6.png
---
height: 400px
--- 
```