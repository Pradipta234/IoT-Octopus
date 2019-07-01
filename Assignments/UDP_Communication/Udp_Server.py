import socket

port = 5500
bufferSize = 1024

msgFromServer = "Message Received"
bytesToSend = str.encode(msgFromServer)

def setup():
	# Create a datagram socket
	serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# Bind to address and ip
	host = sys.argv[1]
	serverSock.bind((host,port))
	print("UDP server up and listening")

# Listen for incoming datagrams 
def talking():
	data, addr = serverSock.recvfrom(bufferSize)
	clientMsg = "Message from Client:{}".format(data)
    clientIP  = "Client IP Address:{}".format(addr)

    print(clientMsg)
    print(clientIP)
    #bytesToSend = input("Enter Server Message")
    serverSock.sendto(bytesToSend,addr)

def main():
	#print("python main function")
	setup()
	while True:
		talking()


if __name__ == '__main__':
	main()
