#simple server 

import socket

s = socket.socket()
host = socket.gethostname()      #local machine name
port = 12345             #reserve a port
s.bind ((host, port))  #bind to the port

s.listen(5)       #wait for client connection 
while True:
	c, addr = s.accept()   #establish connection with client
	print "Got connection from ", addr
	c.send("Thank you for connecting")
	c.close()       
		