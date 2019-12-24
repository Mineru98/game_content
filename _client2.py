# import socket

# def run_client(host='127.0.0.1', port=7788):
#     with socket.socket() as sock:
#         sock.connect((host, port))
#         for _ in range(10):
#             data = input(">>")
#             sock.sendall(data.encode())
#             if data == 'bye':
#                 sock.close()
#                 break
#             res = sock.recv(1024)
#             print(res.decode())

# if __name__ == '__main__':
#     run_client()
import socket

HOST = socket.gethostname()
PORT = 50000
ADDR = (HOST, PORT)
BUFF_SIZE = 1024

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(ADDR)

with open('2.png', 'wb') as f:
    print ('file opened')
    while True:
        print('receiving data...')
        data = clientSocket.recv(BUFF_SIZE)
        print('(data)', data)
        if not data:
            f.close()
            print ('file close')
            break
        f.write(data)

print('Successfully get the file')
clientSocket.close()
print('connection closed')