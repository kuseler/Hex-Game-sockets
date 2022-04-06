import time
import socket

def sendeStr(komm_s, liste):
    liste = bytes(liste, 'utf-8')
    komm_s.sendall(liste)

def sendeTrennByte(komm_s):
    trennByte = bytes([0])
    komm_s.sendall(trennByte)

def empfangeStr(komm_s):
    weiter = True
    datenBytes = bytes()

    trennByte = bytes([0])
    
    datenStr = str(komm_s.recv(1024), 'utf-8')


    return datenStr

turn=True
role = str(input("host/client"))
if role == "host":  
    s = socket.socket()
    s.bind(('', 5000))
    s.listen(10)
    komm_s, client_adresse = s.accept()

if role == "client":
    s = socket.socket()
    ip=input("Enter host ip:")
    ip = "172.16.0.46"
    s.connect((ip, 5000))
    time.sleep(0.1)
    komm_s = s
    print(empfangeStr(komm_s))

"""def generateField(liste):
def generateList():"""


"""
while turn=True:
    if button Pressed end turn:
        sendeStr(komm_s,generateList())
        turn=False
    else:
        time.sleep(10)

new = komm_s.recv(1024)

    


sendeTrennByte(komm_s)
komm_s.close()
"""
