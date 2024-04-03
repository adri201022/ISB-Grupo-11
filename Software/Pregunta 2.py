#LAB 2.1 Listas en Python Parte 2
#Pregunta 2
#Analizando datos y eliminando valores
#Rodrigo Alfonso Gonzales Cabrera
#Código: 20174676

import random
def elimina(lst,n):
    #retorna una nueva lista con 2*n valores eliminados
    #eliminamos los n más grandes
    for i in range(n):
        mayor=max(lst)
        lst.remove(mayor)
        
    #eliminamos los n más pequeños
    for i in range(n):
        menor=min(lst)
        lst.remove(menor)

    return lst

################################################
#programa principal

m=int(input('Ingrese el tamaño de la lista= '))
while m<4:
    print('Error')
    m=int(input('Ingrese el tamaño de la lista= '))
lst=[]
for i in range(m):
    item=random.randint(-20,20)
    lst.append(item)
    
print(lst)
n=int(input('n= '))

while 2*n>m:
    print('Error, muy alto')
    n=int(input('n= '))

#llamamos a la función elimina
nuevaLista=elimina(lst,n)
print(nuevaLista)
