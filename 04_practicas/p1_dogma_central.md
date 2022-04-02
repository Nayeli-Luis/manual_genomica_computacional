# Práctica 1. El dogma central de la biología molecular.

Ésta práctica se lleva a cabo en **parejas** que deben estar compuestas por un/a biologo/a + un/a computólogo/a. El formato consiste en un script de Python (.py) que va a contener un programa. A pesar de que se  hace en parejas la entrega es individual y se hace por Classroom.  El archivo debe tener  la siguiente estructura en el nombre: `p1_Apellidos_Nombres`. Además en la parte inicial del script debe aparecer los nombres de equipo, ejemplo: 

```
# Equipo: 
# Apellidos Nombres
# Apellidos Nombres
```

## Características del programa

El programa debe pedir al usuario una cadena de DNA y el usuario puede ingresar la cadena en minúsculas o mayúsculas, el programa debe: 

1. Validar la cadena, si la cadena no es válida indicarlo en un mensaje y terminar programa. 
2. Arrojar la cadena complementaria. 
3. Arrojar la cadena transcrita (mRNA), **SIN** utilizar `str.replace()`.
4. Verificar que la cadena tenga un codón de inicio, sino es así, que arroje un mensaje. Asuman que estará en el primer codón (sin tomar en cuenta regiones para promotores ni nada por el estilo.)
5. Si la cadena tiene un codón de inicio, entonces que arroje la cadena de aminoácidos (cadena traducida). Es probable que no todos los codones de la cadena de DNA que ingrese un usuario codifiquen para un aminoácido, para éstos codones que el porgrama arroje un - (guión medio). 

## Reglas
 
 No pueden utilizar paqueterías de Python. 
 Y ya.

 
