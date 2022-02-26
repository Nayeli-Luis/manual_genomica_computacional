# Estructuras de control de flujo

El control de flujo se refiere al orden en el que se ejecutan las instrucciones de un programa. El orden de ejecución puede incluir la evaluación de una expresión lógica, de manera que, en caso de ser cierta, se ejecuten ciertas instrucciones. Pero vamos por partes, los flujos de control que existen son: 

* Flujo de control secuencial
* Flujo de control condicional o selección
* Flujo de control iterativo o en bucle. 

## Flujo de control secuencial (`if-else`)
Este tipo de flujo de control hace referencia a los algoritmos cuyas instrucciones se ejecutan una tras otra, sin interrupción de algún tipo. Por ejemplo: 

```python
num1 = 3748
num2 = 123

# Sumar los numeros 
sum = num1 + num2

# Imprimir resultado 
print(f"La suma de {num1} y {num2} es de {sum}")
```
## Flujo de control selectivo o condicional 
En éste tipo de flujo de control el algoritmo debe considerar una expresión lógica para ejecutar o no  un bloque de código en específico, en otras palabras, el programa deber tomar una decisión. Para crear un programa condicional, se utilizan las palabras reservadas `if-else` y `elif`. Y en pseudocódigo, pueden leerse como `Si-SiNo`. 

La sintaxis en Python es la siguiente: 

```python
if expresion_logica == True: #si
    Ejecutar este bloque de codigo
else:  #sino
    Ejecuta este bloque de codigo
```

Por ejemplo: 
Crearemos un algoritmo que imprima un mensaje en función de si un estudiante aprobó o no aprobó la materia. 

```python
calificacion = float(input("Ingrese su calificación: "))
resultado_final =  ""

if calificacion < 5:
    resultado_final = "Reprobado"
else calificacion > 5:
    resultado_final = "Aprobado"

print(f"Tu calificación final es de {calificacion}, por tanto tu status es de {resulatado_final}")
```

¿Qué sucede cuando deseamos colocar más opciones? Podemos: Crear un algortimo con `if-else` anidado o podemos utilizar la palabra reservada `elif` (que es la mejor opción). 

```python
calificacion = float(input("Ingrese su calificación: "))
resultado_final = ""

if calificacion <= 5:
    resultado_final = "Reprobado"
elif calificacion >= 6 and calificacion <= 8:
    resultado_final = "Aprobado (alumno regular)"
elif calificacion > 8: 
    resultado_final = "Aprobado (alumno ñoño)"

print(f"Tu calificación final es de {calificacion}, por tanto tu status es de {resultado_final}")
```

## Flujo de control iterativo 

Iterar significa llevar a cabo una acción de manera repetida. En programación, podemos repetir las instrucciones de un bloque de código en función de una secuencia o de una expresión lógica. Existen dos maneras con bucles `for-in` y `while`.

Conceptos importantes:

* **Contador**: Una variable con un valor inicial de cero, el cual va a cambiar con cada iteración al incrementar su valor de 1 en 1. 
* **Evento**: Se utiliza cuando queremos que el código se ejecute (o deje de ejecutarse) hasta que ocurra un evento en específico. 

### `for-in`

`for-in` permite la ejecución de un bloque de código un número determinado de veces. La sintaxis en Python es la siguiente: 

```python
for elemento in conjunto_de_elementos:
    Ejecuta este bloque de codigo
```

Es común que en lugar de elemento o alguna otra palabra, se escriba "i", porque de esta manera se hace referencia al elemento i-esimo del conjunto de elementos que se tenga. 

```python
for i in conjunto
    Ejecuta este bloque de codigo
```

Por ejemplo: 

```python
variedades_maiz = ["mushito","arrocillo", "iniap", "zapalote grande"]

for variedad in variedades_maiz:
    print(variedad, len(variedad))
```

Para conocer el primer elemento de cada string: 

```python
for variedad in variedades_maiz:
    print(variedad[0])
```

¿Cuándo se termina el bucle? Cuando se terminen los elementos que involucren la iteración. Podemos untilizar `for` con un rango de número si llamamos a la función `range()`. 

```python
numero = int(input("Escribe un número: "))

for i in range(numero):
    print(numero * 3)
```

Ahora, podemos utilizar algún contador, que nos indique la posición de una secuencia:

```python
secuencia = "ATCGTACGT"
indice = 0

for i in range(len(secuencia)):
    print(str(indice) + " " + secuencia[indice])
```

#### Listas de comprehensión (*list comprehensions*)
Permite crear listas en una misma línea de código y son muy utilizadas en la generación de matrices, involucra ciclos `for`  para su construcción. Por ejemplo:

```python
cuadrados = []

for num in [1, 2, 3, 4, 5]: # Se ejecuta un protocolo de iteración
    squares.append(x ** 2)  # Genera una lista nueva (append() agrega elementos a la lista)

cuadrados

```

Es comun escribir las listas de comprehensión en una sola línea de código y no utilizan la función `.append()`: 

```python
cuadrados = [num ** 2 for num in [1 , 2, 3, 4, 5]]
cuadrados
```

### `while`

`while` evalua una expresión lógica, mientras el resultado de la expresión sea verdadero, se ejecutará un bloque de código en específico. La sintaxis en Python es: 

```python
while expresion_logica == True:
    Ejecuta este bloque de codigo
```

Por ejemplo: 

```python
# contador
contador = 0

while contador < 100: # Hasta que esto sea False
    print(contador)
    contador = contador + 10
```

Ejemplo con evento: 

```python
especie = str(input("Ingrese el nombre de la especie avistada\n(escriba '-1' para salir):\n" ))

lista_especies = []

while especie != '-1':
    lista_especies.append(especie)
    especie = str(input("Ingrese el nombre de la especie avistada\n(escriba '-1' para salir:)\n" ))

print("Las especies que se avistaron son:")
print(lista_especies)
```
