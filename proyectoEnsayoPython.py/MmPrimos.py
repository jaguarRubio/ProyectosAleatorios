def principal():
    numero=int(input('n:'))
    primos=primos1()
    primador(numero, primos)
    
    print (primos)
    pass



def primos1():
    primos=[2]         #3, 5, 7, 11, 13
    
    return primos    #la función irá llenandosé de elementos primos únicamente





def primador(num, primos):
    for x in range(3, num+1):
        for z in primos:
            if x % z == 0:
                break
            elif (x//z)>=z:
                continue
            else:
                primos.append(x)
                break

    return primos    #comprobará que los números sean primos, si el residuo es 0 no y escapa, si el cociente n÷z es mayor que el divisor omite al siguiete divisor (primo) contenido en la lista
# la misma si pasa n÷z>divisor_z implicaría un primo y lo añadé como un elemento de la lista y escapa de la lista primos para seguir.
principal()
