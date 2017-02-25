#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM) 

#Prepare a sever socket
serverPort = 6789
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

#Fill in end
while True:
	#Establish the connection 
	print('Ready to serve...') 
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(1024)
		filename = message.split()[1]
		f = open(filename[1:], "rb")
		outputdata = f.read() 

		#Send one HTTP header line into socket
		connectionSocket.send(b'HTTP/1.1 200 OK\r\n\r\n')

		#Send the content of the requested file to the client 
		for i in range(0,len(outputdata)):
			connectionSocket.send(outputdata[i:i+1])
		connectionSocket.send(b'\r\n\r\n')
		connectionSocket.close() 
	except IOError:
		#Send response message for file not found
		connectionSocket.send(b'HTTP/1.1 404 Not Found\r\n\r\n')
		connectionSocket.send(b'<!DOCTYPE html><html><head></head><body><h1>404 Not Found</h1></body></html>\r\n')
		#Close client socket
		connectionSocket.close()
		
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data