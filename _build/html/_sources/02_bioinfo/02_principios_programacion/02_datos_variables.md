# Datos, variables y operadores

## Variables

Una variable es una posición o espacio de memoria en la cual se almacena un dato. Y su valor puede cambiar en cualquier momento. De hecho, podemos ver las variables como cajas que pueden contener datos de algún tipo y a su vez, posee un identificador. En Python la asignación de variables se lleva a cabo con el signo igual (=). De hecho, podemos ver las variables como cajas, que van a contener datos de algún tipo y que vamos a poder nombrar.


### Nombrado variables: buenas prácticas

* El primer elemento debe ser una letra.

* Se puede colocar guión bajo (_) si queremos poner dos palabras. 

* El nombre debe ser descriptivo. 

* No utilizar palabras reservadas del mismo lenguaje de programación.

* No dejar espacios en blanco


## Datos y tipos de datos
Un dato es una representación simbólica (un número, letra, una palabra, etc.) de una característica de un elemento y prácticamente ese elemento puede ser cualquier cosa: una persona, una bacteria, un gen, etc.

Vamos a generar una variable que contenga el nombre de un organismo 

```python
bacteria1 = "E. coli"
```

También podemos asignar muchas variables en una sola línea, por ejemplo: 

```python
bacteria2, bacteria3 = "S. haemolyticus", "S. aureus"
```

### Tipos de datos

En general, existen los siguientes tipos de datos:

* **Datos alfanuméricos**.
También conocidos como cadenas o strings.

* **Datos numéricos**.
Dos tipos: enteros y reales (flotantes)

* **Datos lógicos**.
También conocidos como boolenos.


### Datos numéricos

Tenemos de dos tipos: enteros (`integer`) y reales (`float`/flotantes) y se componen únicamente de números y signos positivo o negativo.


* Números enteros:

```python
# variable llamada entero que contiene un numero entero (3412)
entero = 3412
entero_negativo = -1234

print(type(entero), entero)
```

* Números reales/flotantes
```python
flotante = 4.532
print(type(flotante), flotante)
```

### Datos alfanuméricos

También conocidos como caracter o cadena (`strings`). Se componen de la combinación de todos los caracteres conocidos. **NOTA**: Las cadenas de DNA están caracterizadas como **strings**. 

```python
DNA_corto = "ATCGTAGCTG"
```

#### Indexar y rebanar

**Indexar**: Consiste en referencia cada elemento de un objeto al asignarle un número, ún índice. Python comienza a indexar desde la posición cero. 

**Rebanar**: Consiste en tomar solo algunos de los elementos de un objeto considerando el índice de esos elementos. 

Escribe éste código y observa que pasa.

```python
DNA_corto = "ATCGTAGCTG"

DNA_corto[0]

DNA_corto[-1]

DNA_corto[1:4]
```

### Datos lógicos

También conocidos como booleanos. Son datos que solo toman uno de dos posibles valores: `True/1` (verdadero) o `False/0` (falso). 

```python
booleano = True
print(type(booleano), booleano)
```

## Operadores y expresiones

Un operador es un **símbolo** que permite realizar una operación con los datos que se encuentren almacenados en la variables. 
Existen tres tipos: 

* Aritméticos
* Relacionales
* Lógicos 

Mientras que, una **expresión** es una instrucción que puede estar compuesta de operadores, 
variables, números y que generalmente **produce un resultado**, ya sea numérico o lógico

### Operadores aritméticos 

Realizar operaciones aritméticas entre **datos de tipo entero o flotante**.
Regresa un **resultado numérico**.


|    Símbolo    |   Significado     |
| ------------ | ----------------|
|        +      |        suma       |
|        -      |       resta       |
|        *      |  multiplicación   |
|        /      |      división     |
|       //      |      división entera     |
|        %      | residuo o módulo  |
|       **      |      potencia     |

Ejemplo: 

```python

no_oxigeno = 1
no_hidrogeno = 2

masa_oxigeno = 15.99
masa_hidrogeno = 1

masa_agua = no_oxigeno * masa_oxigeno + no_hidrogeno * masa_hidrogeno
print('El peso molécular del agua (H2O es: ', masa_agua)

```

### Operadores relacionales

Realizan **operaciones de comparación**, al utilizarlos en una expresión el 
**resultado** que arroja es de tipo **booleano** (`True` o `False`).


|    Símbolo    |   Significado     |
| :------------ | ----------------: |
|        <      |    menor que      |
|        >      |    mayor que      |
|       <=      | menor o igual que |
|       >=      | mayor o igual que |
|       !=      |    diferente de   |
|       ==      |      igual que    |


Ejemplos:

```python
planeta1 = "Marte"
planeta2 = "Jupiter"


planeta1 == planeta2

len(planeta1) >= len(planeta2)

```

### Operadores lógicos

Al utilizarlos en una expresión el **resultado es lógico**. 
Son usados cuando queremos evaluar dos expresiones. Además, los operadores lógicos obeceden a las tablas de verdad.


|    Símbolo    |   Significado     |
| :------------ | ----------------: |
|    and     |    conjunción     |
|     or    |    disyunción     |
|    not   |     negación      |

`and`: Todas las espresiones evaluadas deben ser ciertas, para que el resultado sea cierto. 

`or`: Solo  una de las expresiones debe ser cierta para que el resultado sea cierto. 

`not`: El resultado será el contrario a lo que indique la expresión. 

 
### Operadores especiales 

* **Operadores de pertenecia**: Evalúan sin un valor está dentro de una secuencia. Palabras reservadas `in` e `in not`. El resultado es un booleano. 

```python

especie1 = "Amanita muscaria"
especie2 = "Ustilago maydis"

"a" in especie1
```

* **Operadores de identidad**: Checa si dos valores o variables están localizadas en la misma posición de la memoria y las palabras reservadas son: `is` e `is not`. 

```python
agua = "H2O"
agua_oxigenada = "H2O2"

agua is agua_oxigenada

agua is not agua_oxigenada

```

## Estructuras de datos
### Listas
Las listas permiten contener un conjunto de datos del mismo o de diferente tipo. Se definen utilizando paréntesis cuadrados y cada elemento se separa por comas. Se puede accede a cada elemento mediante el método de indexado.

```python
Lista = [1, 2, 3, "hola", "genomica", "computacional", 3.4]

Lista[0]
```

Además, las listas pueden contener listas y podemos acceder a las listas con la siguiente sintaxis: `nombre[]`. 

```python
y = [5, 6, 7, ["A", "B", "C"]]
y[3]

len(y)
```

### Diccionarios
Es otro contenedro que permite la asociación entre clave y valores. Cada clave debe ser única. Los diccionarios se denotan con llaves (`{}`) y cada llave:valor se separan por comas. 

```python
# Esto es un diccionario vacio
numero_texto = {}

# Diccionario con elementos "clave": valor
numero_texto = {"uno":1, "dos":2, "tres":3}
```

Podemos acceder a los valores utilizando la sintaxis de `nombre[]`. 

```python
numero_texto["uno"]
```

Cambiar un valor:

```python
numero_texto["dos"] = 22
```

Eliminar algún valor:

```python
del numero_texto["uno"]
```

## Mini-práctica 1
Ésta mini-práctica se entrega por Classroom, en una libreta de Jupyter Notebook y con la siguiente estructura en el nombre: mp1_Apellidos_Nombres.

**Parte I**

Explorando funciones integradas de Python. 
a) ¿Qué es una función integrada (en inglés son conocidas como *built-in function*)?

b) Crea una variable que se llame `dna` que contenga la siguiente cadena de caracteres: `caacggcgggtccctcataggatgaataggtgaaactgtctgaatgcttaggaactggttatggttaccacttcatcaaatatcaattgaacgatacagc`. Ahora escribe lo siguiente:

```python
dna.upper()
dna.find("catag")
dna.count()
dna.replace("g", "x")
```
c) ¿Qué hace cada una de las funciones anteriores?


**Parte II**

Trabajando con operadores y expresiones 
Escribe y ejecuta las expresiones que se encuentran a continuación y responde para cada una: 

a) ¿Qué tipo de dato se está utilizando?

b) ¿Qué tipo de operador?

c) Justifica el resultado que se obtenga de cada expresión

```python
# Variables
x = 1234
y = 5879
z = 89

mamifero1 = "Ornitorrinco"
mamifero2 = " Ornitorrinco"

# Expresion 1
x > y 

# Expresion 2
mamifero1 == mamifero2

# Expresión 3
x = y or y > z

# Expresion 4
y != x and y > z

# Expresion 5
# Tipo: Tal vez en este requieras hacer un poco de investigación
not x
```


