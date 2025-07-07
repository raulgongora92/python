#Tipos de Cadenas

#Una linea
#comillas dobles
varA ="Hello world"
print(type(varA), varA)  

#comillas simples
varA ='Hello Mundo'
print(type(varA), varA)  

#Multilinea
multilinea = "Esto es \
una cadena de \
texto multilinea"
print(type(multilinea), multilinea)  # <class 'str'>

#Asigancion de variables
name = "Jhon"
print(name)
#Reasignacion de variables
name = "Raul"
print(name)


#imprimir el indice 0 de la variable name
print(name[0])

#imprime la cantidad de caracteres de la variable name
print(len(name))

#concatenacion de cadenas
firstName = "Lili"
lastName = "Miranda"
print(firstName + " " + lastName)

