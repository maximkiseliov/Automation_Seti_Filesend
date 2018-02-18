import socket
import randomm

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()
    print("Connection from: " + str(addr))
    while True:
        data = c.recv(1024).decode('utf-8')
        #data = data.decode()
        
        if not data:
            break
        elif data == 'get poem':       
            print("From connected user: " + data)
            data = randomm.random_poem()       
            print("Sending: " + data)
            #data = data.encode()
            c.send(data.encode('utf-8'))
        else:
            print("From connected user: " + data)
            data = 'Sorry, no such command :('       
            print("Sending: " + data)
            #data = data.encode()
            c.send(data.encode('utf-8'))
    c.close()

if __name__ == '__main__':
    Main()
