import cbc as cli
import sbc as srv
from _thread import *
import threading
import time

def sobeServer(startS):
    print('Subindo Thread Server BC')
    #global runS
    runS = startS
    s = srv.SServerBC()
    s.connect('', cli.cfg.BCASTPORT)
    while runS:
        message = input()
        s.send(message)
        if startS:
            break

def sobeClient(startC):
    print('Subindo Thread Cliente BC')
    #global runC
    runC = startC
    c = cli.SClientBC()
    c.connect('', cli.cfg.BCASTPORT)
    while runC:
        var = c.receive()
        print ('\n',var)
        if startC:
            break


global playS, playC
playS = playC = True

tC = threading.Thread(target=sobeClient, args = (playC,))
tS = threading.Thread(target=sobeServer, args = (playS,))

tC.start()
tS.start()
time.sleep(3)
playS = playC = False
tC.join()
tS.join()
print('Saindo do BC')


      



time.sleep(3)







