# -*- coding: utf-8 -*-

import socket

IP_Address = (('192.168.0.202'),5005) #Addresse IP du serveur et port du serveur

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sock.settimeout(1.0) #Temps avant la fin de la connection

sock.connect(IP_Address) #Connection au serveur en utilisant la variable IP_Address
sock.send("cinema") #Envoie le message "Cinema" 


trameReponse, addr = sock.recvfrom(1024) #Reçoit les données sous la variable "trameReponse"

print "Réception de la trame de réponse", trameReponse.encode("hex") #Decodage de la trame 

b3=ord(trameReponse[3]) #La variable b3 = 4ème octet envoyé de trameReponse 
b2=ord(trameReponse[2]) #La variable b2 = 3ème octet envoyé de trameReponse 
b1=ord(trameReponse[1]) #La variable b1 = 2ème octet envoyé de trameReponse 
b0=ord(trameReponse[0]) #La variable b0 = 1er octet envoyé de trameReponse 

code = b3<<24 | b2<<16 | b1<<8 | b0 #Décalage de la variable b3 de 24 bits a gauche
									#Décalage de la variable b2 de 16 bits a gauche
									#Décalage de la variable b1 de 8 bits a gauche

print code #Affichage du contenu de la variable "code"


