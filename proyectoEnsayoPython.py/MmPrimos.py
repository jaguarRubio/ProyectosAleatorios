def principal():
    numero=int(input('n:'))
    primos=primos1()
    primador(numero, primos)
    
    print (primos)
    pass



def primos1():
    primos=[2]         #3, 5, 7, 11, 13
    
    return primos





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

    return primos

principal()
    
