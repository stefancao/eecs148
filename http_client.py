from socket import *
import sys

# get servername, port and filename from argument
serverName = sys.argv[1]
serverPort = int(sys.argv[2])
filename = sys.argv[3]

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

# send a get request
clientSocket.send(bytes("GET /" + filename + " HTTP/1.1\r\n\r\n", 'utf-8'))

response = clientSocket.recv(1024)

print ('Ressponse from Server:', response)