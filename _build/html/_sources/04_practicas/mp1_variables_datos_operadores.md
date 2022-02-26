# Repasando variables, datos y operadores

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