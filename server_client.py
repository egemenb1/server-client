#CLIENT

import socket
import sys

s = socket.socket()
s.connect(('192.168.1.25',300))
f = open ("/Users/Egemen/Desktop/Odev.txt", "rb")
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
s.close()

--------------------------------------------------


#SERVER
import socket               

s = socket.socket()         
host = "192.168.1.25" 
port = 300
print(host)
s.bind((host, port))        
f = open('gelen.txt','wb')
s.listen(5)                 
while True:
    c, addr = s.accept()     
    print ('Baglanti Aliniyor..', addr)
    print ("Aliniyor...")
    l = c.recv(1024)
    while (l):
        print ("Aliniyor...")
        f.write(l)
        l = c.recv(1024)
    f.close()
    print ("Dosya Alimi Basarili...")
    
    c.close()                