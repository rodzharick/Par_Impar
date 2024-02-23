#Ejercicio N.4 programa para verificar si un numero es par o impar

#input

X=int(input("digite el valor de x: "))

#Processing

R= X%2

if R==0:
    rta= "par"

else:
    rta= "impar"

# output

print("el numero" + str(X)+ " es " + rta)