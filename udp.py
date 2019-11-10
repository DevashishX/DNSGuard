import socket
from dns import rdata
from dnslib import DNSRecord
from dnslib import RR
import dns.resolver
from urllib.parse import urlparse
import resolver
import blacklist
import argparse
from pprint import pprint
print = pprint

def FQDN(question):
    qname = str(question.get_qname())
    parsedq = urlparse(qname)
    if parsedq.netloc == "":
        FQDN = parsedq.path
    else:
        FQDN = parsedq.netloc
    return FQDN
    pass

def allowed(fqdn, B):
    if B.search(fqdn) == True:
        return False
    return True
    pass

def DNSGuard(ip, port, blacklist):
    octetsize = 512
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    data = None
    addr = None
    R = resolver.Resolver()
    print("DNSGuard SERVER ACTIVE ON {}:{}".format(ip, port))
    while True:
        data, addr = sock.recvfrom(octetsize)
        packet = DNSRecord.parse(data)
        question = packet.get_q()
        fqdn = FQDN(question)
        if allowed(fqdn, blacklist):
            zones = R.resolveZone([fqdn])
            print(zones)
            reply = packet.reply()
            for zone in zones:
                reply.add_answer(*RR.fromZone(zone))
                sock.sendto(DNSRecord.pack(reply), addr)
            pass
    pass



if __name__ == "__main__":
    argp = argparse.ArgumentParser()
    argp.description = "A DNS server which runs on localhost to block Advertisements and Malicious Websites, Just point your system or browser DNS queries to localhost:53 and Voila! No more ads and bad websites! Customizable: Blacklist can include any website you want! "
    argp.add_argument("-ip", "--ip", help="Select the ip on which the DNS server is to be active")
    argp.add_argument("-p", "--port", type=int, help="Select the port number on which the DNS server is to be active")
    argp.add_argument("-bl", "--blacklist", help="Select the file from which the blacklist is to be read")

    args = argp.parse_args()
    if args.ip == None:
        ip = "localhost"
    else:
        ip = args.ip

    if args.port == None:
        port = 53
    else:
        port = args.port

    if args.blacklist == None:
        blackfile = "blacklist.txt"
    else:
        blackfile = args.blacklist

    B = blacklist.Blacklist(blackfile)
    DNSGuard(ip, port, B)
    pass