#Entrada de datos por teclado
#input() es una función que permite al usuario ingresar datos desde el teclado.
str1 = input("Enter the first name: ")
str2 = input("Enter the last name: ")

#primera forma de mostar el resultado
#sep: Especifica el separador entre los argumentos de la función print.
#end: Especifica el carácter que se imprimirá al final de la salida. Por defecto, es un salto de línea (\n).
print("Hello, " + str1 + " " + str2, sep=" ",end="\n")

#segunda forma de mostar el resultado
print("Hello, {} {}".format(str1, str2), end="*")
print()

#operacion matematica
num1 = int(input("Enter the first number: "))   
num2 = int(input("Enter the second number: "))

print(num1 + num2) 
print()

#la concatenacion funciona con el operador + para cadenas de texto y enteros, pero no con cadenas de texto y flotantes.
n1 = input('First number is: ')
n2 = input('Second number is: ')
user_sum = float(n1) + float(n2)
print("The sum of " + str(n1) + " and " + str(n2) + " is " + str(user_sum))