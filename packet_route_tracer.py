# "socket" is the name for opening connections with other machines

import socket
import sys

#determine options from -f (first ttl) to -m (max ttl)

if len(sys.argv) == 1:
    first_ttl = 1
    max_ttl = 30

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f":
        first_ttl = sys.argv[2]
        max_ttl = 30
    elif sys.argv[1] == "-m":
        max_ttl = sys.argv[2]
        first_ttl = 1

elif len(sys.argv) == 5:
    if sys.argv[1] == "-f":
        first_ttl = sys.argv[2]
    elif sys.argv[1] == "-m":
        max_ttl = sys.argv[2]
    if sys.argv[3] == "-f":
        first_ttl = sys.argv[4]
    elif sys.argv[3] == "-m":
        max_ttl = sys.argv[4]


first_ttl = int(first_ttl)
max_ttl = int(max_ttl)


for i in range(first_ttl, max_ttl):
    print("TTL " + str(i))
    # set the TTL value
    ttl = i
    dest_name = "www.google.com"
    # convert the name to its IP (look up in DNS)
    dest_addr = socket.gethostbyname(dest_name)
    # use port 33434 since that's known as a "traceroute port"
    port = 33434

    # set up variables for protocols
    icmp = socket.getprotobyname("icmp")
    udp = socket.getprotobyname("udp")

    # establish the receiving (response) socket
    recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
    send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)


    send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

    # set up receiving socket on the port
    recv_socket.bind(("", port))

    # send blank data to destination
    send_socket.sendto(str.encode(""), (dest_addr, port))
    
    try:
        # wait to receive response from router that gave up (TTL dropped to 0)
        _, curr_addr = recv_socket.recvfrom(512)
        #print(_)
        #print(curr_addr)
        # try to get DNS name from IP
        curr_name = socket.gethostbyaddr(curr_addr[0])
        print(curr_name)

    except:
        print("***")
   
    send_socket.close()
    recv_socket.close()

