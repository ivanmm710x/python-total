from os import system

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

# Windows, si fuese otro SO seria clear
system('cls')


print(f"Tu nombre es {nombre} y tu edad es {edad} años")
