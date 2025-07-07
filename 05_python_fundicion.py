#Tipos de Fundiciones o conversion de tipos de datos
#La fundición de tipos es el proceso de conversión de un tipo de datos a otro

#Tipos de Fundiciones o conversion de tipos de datos
#Implicitas
#La conversión de tipo de datos implícita la realiza automáticamente el compilador de Python para evitar la pérdida de datos. Convertirá, por ejemplo, un "int" a "float" si selecciona que el valor insertado es un decimal. Es importante tener en cuenta que Python solo podrá convertir valores si los tipos de datos son compatibles. "int" y "float" son compatibles pero "strings" e "int" no lo son.

#Explicitas
#La conversión de tipo de datos explícita la realiza el programador. El programador debe especificar el tipo de datos al que desea convertir un valor. Por ejemplo, si desea convertir un "float" a "int", debe usar la función "int()". Si desea convertir un "string" a "int", debe usar la función "int()" y asegurarse de que el "string" contenga un valor numérico válido.

str(123)  # Convierte un int a un string
int("123")  # Convierte un string a un int
float("123.45")  # Convierte un string a un float
bool(1)  # Convierte un int a un bool (True)
bool(0)  # Convierte un int a un bool (False)
tuple((1, 2, 3))  # Convierte una lista a una tupla
list((1, 2, 3))  # Convierte una tupla a una lista
set([1, 2, 3])  # Convierte una lista a un conjunto 
dict([(1, 'a'), (2, 'b')])  # Convierte una lista de tuplas a un diccionario