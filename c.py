import socket  
import os
clear = lambda : os.system('clear')

s = socket.socket()   
s.connect(("localhost", 9999))  

grafics = "--START--"
marcador = "O"
print("Your mark is -> {}".format(marcador))
print(grafics)

def mostrar(data):
    for i in range(0,9,3):
        print(data[i:i+3])


def marcar(entrada, marcador):
    global grafics
    while(grafics[entrada-1] != '*'):
        entrada = int(input("Posición ocupada, ingrese una nueva posición >> "))
    grafics = grafics[:entrada-1]+marcador+grafics[entrada:]

def validar():
    global grafics
    global marcador

    respuesta = grafics[:3]==(marcador*3) or grafics[3:6] ==(marcador*3) or grafics[6:9] == (marcador*3)

    for i in range(3):
        c = set([grafics[j] for j in range(i,9,3)])
        respuesta = respuesta or (len(c) == 1 and c.pop() == marcador )

    a = set([grafics[0],grafics[4],grafics[8]])
    b = set([grafics[2],grafics[4],grafics[6]])
    x = len(a) == 1 and a.pop() == marcador
    y = len(b) == 1 and b.pop() == marcador 

    respuesta = respuesta or x or y

    if respuesta:
        return True
    else:
        return False

def game():
    global grafics
    entrada = int(input("Insert the position >> "))
    marcar(entrada,marcador)
    if(validar()):
        grafics += ("\nyiyi")
    #grafics = (" | "+entrada)
    return grafics

def wait():
    
    global grafics
    
    
    recibido = s.recv(1024)
    recibido = recibido.decode('utf-8')
    clear()
    print("-----wait-----")
    print("--------------------")
    mostrar(recibido)
    print("--------------------")
    
    if (recibido[-4:] == "yiyi"):
        print("game over, You lose :c")
        return True
    else:
        grafics = recibido
        return False

def myturn():
    
    global grafics
    mensaje = game()
    clear()
    print("-----myTurn-----")
    print("--------------------")
    mostrar(grafics)
    print("--------------------")
    
    s.send(grafics.encode())
    if (mensaje[-4:] == "yiyi"):
        print("Good game, You win c:")
        return True
    else:
        return False

turntoplay = False
grafics = "*********"
print("--------------------")
mostrar(grafics)
print("--------------------")
while True:
    
    if(turntoplay):
        if(myturn()):
            break
    else:
        if(wait()):
            break
    turntoplay = not turntoplay  
    
print("adios")
  
s.close() 