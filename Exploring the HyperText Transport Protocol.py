import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

headers_received = False

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    decoded_data = data.decode()
    if not headers_received:
        headers = decoded_data.split('\r\n\r\n')[0]
        print("Headers:")
        print(headers)
        headers_received = True
    print(decoded_data, end='')

mysock.close()
