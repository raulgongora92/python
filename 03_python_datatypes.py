#Tipos de datos en Python

#los 5 tipos principales clasificados literales son:
#Numerico, Secuencia, Diccionario, Booleano, Conjunto

#Tipos Numericos

# int: Enteros, por ejemplo, 1, 2, 3
a = 5
print(type(a),a)  # <class 'int'>

# float: Números de punto flotante, por ejemplo, 1.0, 2.5, 3.14
b = 3.14
print(type(b),b)  # <class 'float'>

# complex: Números complejos, por ejemplo, 1 + 2j
c = 1 + 2j
print(type(c),c)  # <class 'complex'>


#Tipos de Secuencia

# str: Cadenas de texto, por ejemplo, "Hola", 'Python'
d = "Hola, Python"
print(type(d),d)  # <class 'str'>

# list: Listas, por ejemplo, [1, 2, 3], ['a', 'b', 'c']
e = [1, 2, 3, 'a', 'b', 'c']
print(type(e),e)  # <class 'list'>
print(e[0])  # Acceso al primer elemento de la lista

# tuple: Tuplas, por ejemplo, (1, 2, 3), ('a', 'b', 'c')
f = (1, 2, 3, 'a', 'b', 'c')
print(type(f),f)  # <class 'tuple'>
print(f[0])  # Acceso al primer elemento de la tupla


#Tipos de Diccionario

# dict: Diccionarios, por ejemplo, {'clave1': 'valor1', 'clave2': 'valor2'}
g = {'clave1': 'valor1', 'clave2': 'valor2'}    
print(type(g),g)  # <class 'dict'>
print(g['clave1'])  # Acceso al valor asociado a 'clave1'


#Tipos Booleanos

# bool: Booleanos, por ejemplo, True, False
h = True
print(type(h),h)  # <class 'bool'>


#Tipos de Conjunto

# set: Conjuntos, por ejemplo, {1, 2, 3}, {'a', 'b', 'c'}
i = {1, 2, 3, 'a', 'b', 'c'}
print(type(i),i)  # <class 'set'>
