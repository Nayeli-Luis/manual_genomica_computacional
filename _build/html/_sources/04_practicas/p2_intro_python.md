# Práctica 2. Fundamentos de programación e introducción a Python
**Autoras: Marisol Navarro y M. Nayeli Luis-Vargas**

:::{admonition} Objetivo
:class: tip
* Que el estudiante aplique los conocimientos aprendiendos sobre fundamentos de programación con el lenguaje Python.
:::

La entrega de ésta práctica es individual y a través del Classroom de la clase. 

1.  Escribir un programa que me permita aplicar el 10% de descuento si la compra total es mayor a $100.

2. Se sabe que la fórmula para obtener el área de un triángulo es a = (b x h) / 2, donde b es la longitud de la base del triángulo, y h es su altura. Escribir un programa que permita realizar el cálculo del área de un triángulo. Si el área contiene valores decimales, imprimir el resultado con dos dígitos.

3.  La fórmula para el Índice de Masa Corportal es IMC = kg/m2 donde kg es el peso de la persona en kilogramos y m2 es la altura en metros al cuadrado. Realizar un programa que calcula el IMC cuando se le provee el peso y la altura

4. Analiza el siguiente código:

```{code-block} python
curso = str(input("Ingresa el nombre de tu curso (Genomica Computacional o Plantas I): "))
cali_teoria = float(input("Ingresa tu calificación de la sección de teoría: "))
cali_practica = float(input("Ingresa tu calificación de la sección de práctica: "))

if(curso == "Plantas I" or curso == "plantas I"):
    if(cali_teoria > 5 or cali_teoria > 5):
        print("Por favor revisa la calificación ingresada")
    else: 
        print("Calificación válida. Tu calificación total es: ", cali_teoria + cali_practica)             
elif(curso == "Genomica Computacional" or curso == "Genomica Computacional"):
    if(cali_teoria > 6 or cali_practica > 4):
        print("Por favor revisa la calificación ingresada.")
    else: 
        print("Calificación válida. Tu calificación total es: ",cali_teoria + cali_practica)
else: 
    print("Curso no reconocido. Ingresa la calificación de tu curso (Plantas I o Genomica Computacional)")
```

Contesta las siguientes preguntas:

* ¿Qué es lo que hace éste programa? 
* Explica línea por línea el programa. 
* ¿Para qué se usan los operadores `or`? 