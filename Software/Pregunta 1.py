#LAB 1.1 PROCESAMIENTO DE STRING EN PYTHON
#Pregunta 1
#Generando cadena aleatoria de ADN
#Rodrigo Alfonso Gonzales Cabrera
#Código: 20174676

def generar(n):
    import random
    #validación
    while n<20 or n>1000:
        print("\nERROR! El tamaño debe estar entre [20, 1000] ")
        n=int(input('Ingrese nuevamente la longitud de la cadena: '))
    cad=''
    print('\nLongitud de cadena válida!')
    for i in range (n):
        nuc=random.choice('CGTA')
        cad=cad+nuc
    return cad
#Programa principal
tam=int(input('Ingrese la longitud de la cadena: '))
w=generar(tam)
print('La cadena ADN es: ',w)
              
