# Funciones. El dogma central de la biología molecular.

Ésta mini-práctica se entrega por Classroom, en una libreta de Jupyter Notebook (.ipynb) y con la siguiente estructura en el nombre: mp12_Apellidos_Nombres.

a) Genera una cadena de DNA de 350 pares de bases con la siguiente función:

```python
from random import choice

def generar_secuencia(tamaño = int(), codigo = "CGTA"):
    return''.join(random.choices(codigo, k = tamaño))
    
```

Guarda la cadena arrojada en una variable llamada `dna`. 

b) Crea una función que genere la cadena de DNA complementaria. Agrega el código que creaste, no sólo el resultado. 

c) Crea una función que genere la cadena de DNA transcrita. Agrega el código que utilizaste, no solo el resultado.

d) Escribe en notación narrada un algoritmo para traducir la cadena transcrita.