# Algoritmos y funciones

## Algoritmos
Un algoritmo es un conjunto de acciones o pasos finitos, ordenados de forma lógica y que se utilizan para resolver un problema o para obtener un resultado. Si te detienes a pensarlo por un momemto, podrás darte cuenta que nuestra vida cotidiana está dirigida por algortimos. Hasta pedir una pizza es un algoritmo, el dogma central de la biología molecular es un algortimo. Los algoritmos tienen que cumplir tres características:

1. **Ordenado**. El orden en la ejecución de sus pasos debe ser riguroso, algunos tendrán que ser ejecutados antes que otros, de manera lógica. Por ejemplo, no puedes pedir la pizza sin antes haber llamado o haber abierto la app de comida a domicilio. No puede haber traducción sin antes haber transcripción.

2. **Definido**. Si el algoritmo se ejecuta en repetidas ocasiones, usando los mismos datos, debe producir siempre el mismo resultado

3. **Finito**. Todo algoritmo posee un inicio, de igual forma debe tener un final, la ejecución de sus instrucciones debe terminar una vez procese los adtos y entregue resulta

Los algoritmos deben ser representados de alguna forma para que puedan ser más entendibles para nosotros como humanos. Debe usarse una notación simple y lo suficientemente clara para que no haya ambiguedades. Estas notaciones son muy útiles para entender la lógica de lo que estamos haciendo y poder luego traducirlas a cualquier lenguaje de programación. La notación que veremos es la **narrada**. En la **notación narrada** los pasos o instrucciones se describen mediante un lenguaje natural, usando palabras, verbos, frases normales en forma de una lista ordenada. 

## Funciones
Una función es un bloque de código que puede llevar a cabo una tarea en específico y que puede ser reutilizado a lo largo de un algoritmo. La creación de funciones permite que el código pueda dividirse en módulos. En Python tenemos tres vías para utilizar funciones: 

1. Usando funciones integradas
2. Crear funciones propias
3. Utilizar funciones de módulos o paqueterías

**Conceptos importantes**:

* **Parámetro**: Es una variable que se definió durante la creación de una función. 
* **Argumento**: Es el valor que se pasa aun parámetro para poder utilizar una función. 

### 1. Funciones *built-in* 
Python tienen integradas muchísimas funciones que podemos utilizar, [aquí una pequeña lista de algunos](https://docs.python.org/3/library/functions.html). Y al ser funciones, pues incluyen sus parámetros, los cuales podemos explorar con la función `help()`. Por ejemplo, la función `all()`:

```python
help(round)
```

### 2. Funciones propias
La opción dos es crear nuestras propias funciones, es decir, declarar desde el nombre de la función, hasta los parámetros y argumentos de la misma. Para definir una función, utilizamosla siguiente sintaxis: 

```python
def nombre_funcion(parametro1, parametro2):
    Bloque de codigo

# Llamar a una funcion
nombre_funcion(parametro1 = argumento1)
```

Problema: 

Crear una función que verifique si una secuencia de DNA es válida. 

Algoritmo:
```
1. Determinar cuáles son las letras válidas (A, T, C, G).
2. Guardar cadena de DNA en una variable.
3. Convertir la cadena a mayusucula.
4. Leer cada base de la cadena de DNA ingresada.
5. Si la base es válida seguir leyendo cadena. 
6. Si la base es inválida terminar lectura. 
7. Arrojar mensaje que indique si la secuencia es válida o no.
```

Al pasar esto a código: 

```python
# 1. Determinar cuales son las letras válidas
nucleotidos_validos = ["A", "T", "C", "G"]

# 2. Guardar cadena de DNA en una variable
secuencia = "ATCGTTTATC"

# 3. Convertir la cadena a mayusucula.
secuencia_mayus = secuencia.upper()

# 4. Leer cada base de la cadena de DNA ingresada. 
for base in secuencia_mayus:
    # 5. Si la base es válida seguir leyendo cadena.
    if base in nucleotidos_validos:
        continue 
    # 6. Si la base es inválida terminar lectura.
    else:
        print(f"La base {base}, no existe.")
        break
# 7. Arrojar mensaje que indique si la secuencia es válida o no.
print("Secuencia válida")
```

Ahora, podemos pasar éste bloque de código a una función, de manera que cuando quieras utilizarlo no tengas que escribirlo todo de nuevo. Entonces: 

```python
def validar_dna(secuencia):
    
    secuencia_mayus = secuencia.upper()
    
    for base in secuencia_mayus:
        if base in nucleotidos_validos:
            continue
        else:
            return False
    return True

# Llamar funcion 
validar_dna(secuencia = "ATCGFR")
```

### 3. Funciones de librerías de Python

Las librerías en Python son un conjunto de funciones ya creadas, existen 137 mil librerías aproximadamente, es decir, un millón de opciones para resolver un problema. ¿Cómo se utilizan? Pasos: 

1. Instalar la librería vía `conda` o vía `pip`

```
conda install pandas
```
2. Para poder utilizar las funciones, llamamos a la librería. 

```python
import pandas as pd
```

## Mini-práctica 2. El dogma central de la biología molecular.

Ésta mini-práctica se entrega por Classroom, en una libreta de Jupyter Notebook (.ipynb) y con la siguiente estructura en el nombre: mp12_Apellidos_Nombres.

a) Genera una cadena de DNA de 350 pares de bases con la siguiente función:

```python
from random import choice

def generar_secuencia(tamaño = int(), codigo = "CGTA"):
    return''.join(random.choices(codigo, k = tamaño))
    
```

Guarda la cadena arrojada en una variable llamada `dna`. 

b) Genera la cadena de DNA complementaria. Agrega el código que generaste, no sólo el resultado. 

c) Genera la cadena de DNA transcrita. Agrega el código que utilizaste, no solo el resultado.

d) Escribe en notación narrada un algoritmo para traducir la cadena transcrita.