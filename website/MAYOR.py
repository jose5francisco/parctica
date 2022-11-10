
a = input("ingrese un numero: ") 
b = input("ingresa un numero: ")
c = input("ingresa un numero: ")
d = input("ingresa un numero: ")


if a.isdigit() !=True:
 print("no se aceptan caracteres" )
if a > b and a > c and a > d:
    print("el numero mayor es: " + a )

if b.isdigit() !=True:
     print("no se aceptan caracteres" )
elif  b > a and b > c and b > d:
    print("el numero mayor es: " + b)

if c.isdigit() !=True:
    print("no se aceptan caracteres" )
if  c > a and c > b and c > d:
    print("el numero mayor es: " + c)

if d.isdigit() !=True:
     print("no se aceptan caracteres" )
if d > a and d > b and d > c:
    print("el numero mayor es: " + d)
elif a == b and a== c and c == d:
    print("todos los numeros son iguales")

"""" 
jose elias francisco mar
valeria abigail 
israel rodriguez lopez
martin aban rodriguez lopez
"""