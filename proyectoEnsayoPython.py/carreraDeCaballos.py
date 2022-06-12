import random
import msvcrt
import time

meta=False
caja = ['bastón', 'espada', 'oro', 'copa', 'che', 'mate']


def máquina(barril):
    deduc = random.randint(0, 5)
    return barril[deduc]


print('\n♘ bastón\n♞ espada\n♘ oro\n♞ copa\n♘ che\n♞ mate')
caballo0 = input('\nselecciona un caballo: ')
caballo1 = máquina(caja)


print('\nla máquina ha elegido:', caballo1,'\ny tú:', caballo0)
def elije(caballo):
   if caballo=='bastón' or caballo==0:
      eleccion=caballo
   elif caballo=='espada' or caballo==1:
      eleccion=caballo
   elif caballo=='oro' or caballo==2:
      eleccion=caballo
   elif caballo=='copa' or caballo==3:
      eleccion=caballo
   elif caballo=='che' or caballo==4:
      eleccion=caballo
   elif caballo=='mate' or caballo==5:
      eleccion=caballo
   else:
      raise ValueError
   return eleccion

def F_elijeMistica(caballo, alea): #perdón, no retornaba un True
   if caballo==alea:
      return True
   else:
      return False
   # elif caballo=='espada' or caballo==1:
   #    eleccion=caballo
   # elif caballo=='oro' or caballo==2:
   #    eleccion=caballo
   # elif caballo=='copa' or caballo==3:
   #    eleccion=caballo
   # elif caballo=='che' or caballo==4:
   #    eleccion=caballo
   # elif caballo=='mate' or caballo==5:
   #    eleccion=caballo
   # else:
   #    raise ValueError
   # return True

caballo0 = elije(caballo0)
caballo1 = elije(caballo1)


# def galope(equino, que):
#     Mazo=random.randint(0, 5)
#     if equino==que(Mazo): #si caballo 0 == fun elije (en random 0 a 5):
#        return True
#     else:
#        return False



ico2='♘ '
ico1='♞ '
pistaLugar1=[ ]
pistaLugar2=[ ]
def avanza(afirmativo, ico, ju):
    if afirmativo:
       ju.append(ico)
       verificador=ju.count(ico)
       if verificador==2:
           ju.remove(ico)
       re=ju
    else:
       ju.append(' ')
       re=ju
    return re


c=int(input('indica distancia de la meta:'))
w=int(input('indica velocidad de los caballos:'))
print('presiona una tecla aleatoria para avanzar turnos.')
turno=0
while 0<(c-w):#meta == False:
    turno+=1
    print('turno:',turno)
#    Mazo=random.randint(0, 5)
    herradura=F_elijeMistica(caballo0, máquina(caja))
    print(avanza(herradura, ico1, pistaLugar1))
#    Mazo=random.randint(0, 5)
    herradura=F_elijeMistica(caballo1, máquina(caja))
    print(avanza(herradura, ico2, pistaLugar2))
    c-=w
    time.sleep(1)
   #  ings=msvcrt.getch()#alternar tiempo/tipeo
print('turno final:', turno+1)#(parche malo)
print(avanza(herradura, ico1, pistaLugar1))
print(avanza(herradura, ico2, pistaLugar2))



corcel1 = pistaLugar1.index(ico1)
corcel2 = pistaLugar2.index(ico2)
def cuatemocDeTecnotitlan(z, a):
   
    if z > a:
      return 'El 1ª jinete({}) ha ganado'.format('♞ ')
    elif z < a:
      return 'El 2ª jinete({}) ha ganado'.format('♘ ')
    else:
      return 'Los jinetes han empatado'
time.sleep(2)
print(cuatemocDeTecnotitlan(corcel1, corcel2))
print('programa finalizado, presiona una tecla aleatoria para concluirlo.')
msvcrt.getch()



# pista=pista.replace(' ','♞ ', 1)
# pista=pista.replace(' ','♘ ', 3)