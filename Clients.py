import socket

UDP_IP = "10.160.108.3"
UDP_PORT = 5005
MESSAGE = "Client connecté"
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

while True :
    data, addr = sock.recvfrom(1024)
    print ("Serveur : ", data.decode())
    MESSAGE = input("Réponse : ")
    sock.sendto(MESSAGE.encode(), addr)
    
