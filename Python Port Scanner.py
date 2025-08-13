import socket
import sys
import pyfiglet
from datetime import datetime

banner = pyfiglet.figlet_format("Port Scanner") #just for added fun hehe
print(banner)

target = input("Enter your host so I can scan it bro: ")
host = socket.gethostbyname(target)

#print(datetime.now())
date = datetime.date(datetime.now())
t1 = datetime.now()
print("Start time: {}".format(t1.strftime("%H:%M:%S"))) #kalau mau tdk ada mili second

print("Target: " + target)
print("Host: " + host)

for port in range (1, 1025):
    #AF_INET are for IP4v / AF_INET6 means IP6v add-resses and SOCK_STREAM means using TCP connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.001)
    result = sock.connect_ex((host, port))
    if result == 0 :
        try:
            print("Port No: {}\nOpen Protocol Service Name: {}\n". format(port, socket.getservbyport(port, "tcp")))
        except socket.error:
            print("Port No: {}\nOpen Protocol Service Name: {}\n". format(port, "Unknown"))
    sock.close()

t2 = datetime.now()
print("End time: {}".format(t2.strftime("%H:%M:%S"))) #kalau mau tdk ada mili second

total_time = t2 - t1
print("Total time: {}".format(total_time))