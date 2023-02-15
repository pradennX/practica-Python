'''
Programar una función que reciba su nombre y carrera, ingresados en el programa principal,  y lo muestre 

Partiendo de los valores 0 y 1, generar la sucesión de Fibonacci, hasta la posición 30 

Recorrer la lista generada y pasar, a una segunda lista, aquellos  valores que sean menores al promedio entero, de toda la serie generada 

Ordenar esta segunda lista de mayor a menor y mostrarla 

 

De la segunda lista, obtener una tercer lista, en el programa principal, con aquellos valores que sean primos. 

Si el número es primo deberá determinarlo una función 

Mostrar la lista obtenida con los valores separados por 5 espacios 
'''
#función saludo
def saludo():
    print("nombre: ",nom,"\ncarrera: ",car)

#función primos
def primos(a):
    div, contdiv = 1,0
    while div<a:
        if a%div==0:
            contdiv = contdiv + 1
        div = div + 1
    if contdiv <= 2:
        return 1

#inicializo variables
nom = input("ingrese su nombre: ")
car = input("ingrese su carrera: ")
prom = 0

#inicializo listas
fibo,listamenores,listaprimos = [0,1],[],[]

#bucles for
for i in range(2,30):
    fibo.append(fibo[i-1]+fibo[i-2])

for i in range(len(fibo)):
    prom = prom + fibo[i]

for i in range(len(fibo)):
    if fibo[i]<prom:
        listamenores.append(fibo[i])

for i in range(len(listamenores)-1):
    for j in range(len(listamenores)-1):
        if listamenores[j]<listamenores[j+1]:
            aux = listamenores[j]
            listamenores[j] = listamenores[j+1]
            listamenores[j+1] = aux

for i in range(len(listamenores)):
    res = primos(listamenores[i])
    if res == 1:
        listaprimos.append(listamenores[i])

print(listamenores)
print()

for i in range(len(listaprimos)):
    print(listaprimos[i], end="     ") 

saludo()