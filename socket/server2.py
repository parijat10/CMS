# Tcp Chat server
 
import socket, select
 
#Function to broadcast chat messages to all connected clients
def broadcast_data (sock, message):
    #Do not send the message to master socket and the client who has send us the message
    #for socket in CONNECTION_LIST:
    j=0
    for i in range(0,len(CONNECTION_LIST)):
     

        if CONNECTION_NAME[i][1]== "server" and sock==CONNECTION_LIST[i] :
        # sock=CONNECTION_LIST[0]
          #  print "loop1inside"
            try :
                msglist=message.split(',');
                #for j in range(0,len(CONNECTION_LIST)):
                # print "message=", msglist
                # print "length" , len(CONNECTION_LIST)
                j=int(msglist[0])
                # print "j=",j
                CONNECTION_LIST[j].send(message)                                                          
            except :
                        # broken socket connection may be, chat client pressed ctrl+c for example
                CONNECTION_LIST[j].close()
                CONNECTION_LIST.remove(CONNECTION_LIST[j])
                CONNECTION_NAME.remove(CONNECTION_NAME[j])
            return 
    
    for socket in CONNECTION_NAME:

        # print "loop2"        
        if socket[0] == sock :
            try :
                message = socket[1] + message
                
                CONNECTION_LIST[1].send(message)
            except :
                # broken socket connection may be, chat client pressed ctrl+c for example
                socket[1].close()
                CONNECTION_LIST.remove(socket[1])
                CONNECTION_NAME.remove(socket)
 





if __name__ == "__main__":
     
    # List to keep track of socket descriptors
    CONNECTION_LIST = []
    CONNECTION_NAME = []
    RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
    PORT = 5000
     
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this has no effect, why ?
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(10)
 
    # Add server socket to the list of readable connections
    CONNECTION_LIST.append(server_socket)
    CONNECTION_NAME.append([server_socket,"server_socket"])
 
    print "Chat server started on port " + str(PORT)
 
    while 1:
        # Get the list sockets which are ready to be read through select
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
        print "loop"
        for sock in read_sockets:
            #New connection
            if sock == server_socket:
                # Handle the case in which there is a new connection recieved through server_socket
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                if(len(CONNECTION_NAME)==1):
                    CONNECTION_NAME.append([sockfd,"server"])
                    sockfd.send("You are server")
                else:
                    CONNECTION_NAME.append([sockfd,"robot"+`len(CONNECTION_NAME)`])
                print "Client (%s, %s) connected" % addr
                
                print CONNECTION_NAME 
                # broadcast_data(sockfd, "[%s:%s] entered room\n" % addr)
             
            #Some incoming message from a client
            else:



                # for i in CONNECTION_LIST:
                #     print i
                # Data recieved from client, process it
                try:
                    #In Windows, sometimes when a TCP program closes abruptly,
                    # a "Connection reset by peer" exception will be thrown
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        # print  "\r" + '<' + str(sock.getpeername()) + '> ' + data 
                        broadcast_data(sock,data)                
                 
                # except:
                #     try:
                #         msg = sys.stdin.readline()
                #         # msglist = msg.split(',')
                #         broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + msg)





                except:
                    broadcast_data(sock, "Client (%s, %s) is offline" % addr)
                    print "Client (%s, %s) is offline" % addr
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue


 
                # try:
                #     msg = sys.stdin.readline()
                #     msglist = msg.split(',')
                #     broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data) 
                
                # except:
                #     # broadcast_data(sock, "Client (%s, %s) is offline" % addr)
                #     # print "Client (%s, %s) is offline" % addr
                #     # sock.close()
                #     # CONNECTION_LIST.remove(sock)
                #     continue

                        
    server_socket.close()