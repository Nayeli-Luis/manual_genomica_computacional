#!/usr/bin/env python
# coding: utf-8

# # Control de flujo con cadenas de DNA.
# 
# Ésta práctica se entrega por Classroom en una libreta de Jupyter (`.ipynb`) con la siguiente estructura en el nombre: 
# 
#     mp2_Apellidos_Nombres.ipynb
#     
# Para generar secuencias de DNA de diferente tamaño te sugiero utilizar la siguiente función:

# In[1]:


import random

def generar_secuencia(tamaño = int(), codigo = "CTGA"):
    return''.join(random.choices(codigo, k = tamaño))

# generar secuencia de 50 pb y guardar en variable
DNA = generar_secuencia(50)


# * Crea un programa en el que un usuario ingrese un codón y el programa arroje un mensaje que diga si se trata de un codón de stop, de inicio o ninguno de los dos. 

# In[2]:


# Tu respuesta



# * Crea un programa que arroje la frecuencia de A, T, C y G de una cadena de DNA de 300 nucleotídos. Punto extra (en algo) si logras hacerlo con bucles for y diccionarios.

# In[3]:


# Tu respuesta 



# * Listas de comprehensión. 
#     1. Crea una lista que contenga 5 cadenas de DNA de 50 nucleótidos cada una. 
#     2. Extrae de cada cadena el codón número 3
#     3. El programa debe dar como resultado una lista con los codones que extrajíste
#     
# Resuelve éste problema utilizando tanto un ciclo `for` con la función `append()` y utilizando la estructura de las listas de comprehensión.
# 
# Piensa/resuelve por partes!

# In[4]:


# Tu respuesta con for y append()



# In[5]:


# Tu respuesta con lista de comprehensión


