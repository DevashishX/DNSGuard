import socket

def UDP_server(ip, port):

    octetsize = 512
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    data = None
    addr = None

    while True:
        data, addr = sock.recvfrom(octetsize)
        print("Addr:\n{}\nData:\n{}\n".format(addr, data))

    pass



if __name__ == "__main__":
    ip = "localhost"
    port = 53
    UDP_server(ip, port)
    pass