#simpleClient

import socket   #get the socket in the script.  

s = socket.socket  #create the socket object to go in class socket. 
host = socket.gethostname()  #get machine name
port = 12345

s.connect((host, port))
print s.recv(1024)
s.close 		#close ze socket. 

