import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    message = str(input('Type get poem (and Return) to get a random poem\n-> '))
    
    while message != 'q':
        #message = message.encode()
        s.send(message.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        #data = data.decode()
        print("Received from server:\n" + data)
        message = str(input('\nType get poem (and Return) to get a random poem or q to quit\n-> '))
    s.close()

if __name__ == '__main__':
    Main()
        
