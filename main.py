from network import *
from garfoClass import *
from filosofoClass import *
from displayClass import *
from latency import *

def garfo_process(identifier, address, port):
    garfo = Garfo(identifier, address, port)
    garfo.start()

def filosofo_process(identifier, fork_left, fork_right, portNear, portFar):
    philosopher = Philosopher(identifier, fork_left, fork_right, portNear, portFar)
    philosopher.start()

def limpemos():
    print('Saindo')

def jantemos():
# Fazer a busca por garfos rodando o vetor de servers
    info = listOfPeers()
    selfIp = info[0][1]
    selfPorta = info[0][2]
    selfName = info[0][3]
    garfoPertoIp = info[1][1]
    portaPerto = info[1][2] 
    garfoLongeIp = info[2][1]
    portaLonge = info[2][2]
    
    garfoServer1 = multiprocessing.Process(target=garfo_process, args=('Garfinho', selfIp, selfPorta,))
   
    filosofo1 = multiprocessing.Process(target=filosofo_process, args=(selfName, garfoPertoIp, garfoLongeIp, portaPerto, portaLonge,))
    
    garfoServer1.start()
    
    filosofo1.start()

if __name__ == "__main__":
    try:
        jantemos()
    except KeyboardInterrupt:
        limpemos()
