import socket
import sys

port = int(sys.argv[2])
host = sys.argv[1]
bufferSize = 1024

def setup():
	clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return clientSock


def talking(clientSock):
	while True:
		Message = input("Message for Server: ")
		clientSock.sendto(str.encode(Message),(host,port))
		msgFromServer = clientSock.recvfrom(bufferSize)
		msg = "Server: "+ msgFromServer[0].decode('utf-8')
		print(msg)


def main():
	#print("python main function")
	sock = setup()
	talking(sock)


if __name__ == '__main__':
	main()	
