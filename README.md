# DNSGuard
A DNS server which runs on localhost to block Advertisements and Malicious Websites, Just point your system or browser DNS queries to localhost:53 and Voila! No more ads and bad websites!

Customizable: Blacklist can include any website you want!

### Added feature
Blacklist gets reloaded into the application at runtime when it is modified
old blacklist is used if there are any problems in the new blacklist

# How to install?
run ```sudo ./install.sh``` to install required python3 libraries


# How to Check?

## For Browser Testing
Search up how to change the DNS of your respective operating system on internet and set the DNS (IPV4) address to 127.0.0.1
and start the server on command line or using daemons such as runit or monit

## Using Dig utility on linux terminal
$ dig www.example.com @127.0.0.1

The websites which are blocked will not receive a response / will be timed out

# USAGE

```sudo python3 DNSGuard.py```

usage: DNSGuard.py [-h] [-ip IP] [-p PORT] [-bl BLACKLIST]

optional arguments:
  -h, --help            show this help message and exit
  
  
  -ip IP, --ip IP       Select the ip on which the DNS server is to be active
  
  
  -p PORT, --port PORT  Select the port number on which the DNS server is to
                        be active
                        
                        
  -bl BLACKLIST, --blacklist BLACKLIST
                        Select the file from which the blacklist is to be read
