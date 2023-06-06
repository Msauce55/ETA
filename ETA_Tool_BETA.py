# Everyday Task Automation (ETA)
import socket
import sys
from datetime import datetime


print(r'''
╦ ╦╔═╗╦  ╔═╗╔═╗╔╦╗╔═╗  ╔╦╗╔═╗  ╔═╗╔╦╗╔═╗
║║║║╣ ║  ║  ║ ║║║║║╣    ║ ║ ║  ║╣  ║ ╠═╣
╚╩╝╚═╝╩═╝╚═╝╚═╝╩ ╩╚═╝   ╩ ╚═╝  ╚═╝ ╩ ╩ ╩''')
print("~" * 60)
print(r'''
   ___           _        ___                                  
  / _ )___ ___ _(_)__    / __/______ ____  ___
 / _  / -_) _ `/ / _ \   _\ \/ __/ _ `/ _ \(_-<
/____/\__/\_, /_/_//_/  /___/\__/\_,_/_//_/___/
         /___/                                  ''')
print("~" * 60)
print(r''' 
╔═╗╔═╗╦═╗╔╦╗╔═╗╔═╗╔═╗╔╗╔
╠═╝║ ║╠╦╝ ║ ╚═╗║  ╠═╣║║║
╩  ╚═╝╩╚═ ╩ ╚═╝╚═╝╩ ╩╝╚╝''')
print("~" * 60)


remoteServer = input("Enter IP to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

print("~" * 60)
print("Please wait, scanning...", remoteServerIP)
print("~" * 60)

t1 = datetime.now()

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: Open".format(port))
        sock.close()
except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

t2 = datetime.now()

total = t2 - t1
print("~" * 60)
print('There are 65,535 possible port numbers! Here are common open ports:')
print('-P 20/21: FTP')
print('-P 22: SSH')
print('-P 25: SMTP')
print('-P 53: DNS ')
print('-P 80: HTTP')
print('-P 123: NTP')
print('-P 179: BGP')
print('-P 443: HTTPS')
print('-P 500: ISAKMP')
print('-P 587: SMTP')
print('-P 3389: RDP')
print("~" * 60)
print(r'''
╔═╗╔╗╔╔╦╗  ╔═╗╔═╗╦═╗╔╦╗╔═╗╔═╗╔═╗╔╗╔
║╣ ║║║ ║║  ╠═╝║ ║╠╦╝ ║ ╚═╗║  ╠═╣║║║
╚═╝╝╚╝═╩╝  ╩  ╚═╝╩╚═ ╩ ╚═╝╚═╝╩ ╩╝╚╝ ''')
print("~" * 60)
print(r'''
╔╗╔╔═╗╔╦╗╦ ╦╔═╗╦═╗╦╔═  ╔═╗╔═╗╔╗╔╔╗╔╔═╗╔═╗╔╦╗╦╔═╗╔╗╔  ╔═╗╔═╗╔═╗╔╗╔   
║║║║╣  ║ ║║║║ ║╠╦╝╠╩╗  ║  ║ ║║║║║║║║╣ ║   ║ ║║ ║║║║  ╚═╗║  ╠═╣║║║   
╝╚╝╚═╝ ╩ ╚╩╝╚═╝╩╚═╩ ╩  ╚═╝╚═╝╝╚╝╝╚╝╚═╝╚═╝ ╩ ╩╚═╝╝╚╝  ╚═╝╚═╝╩ ╩╝╚╝ooo''')
import os
import socket
import datetime
import time

FILE = os.path.join(os.getcwd(), "networking.log")

def ping():
    try:
        socket.setdefaulttimeout(3)


        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        host = input('Enter Host IP to Start: ')
        port = 53

        server_address = (host, port)
        s.connect(server_address)

    except OSError as error:
        return False


    else:
        s.close()

        return True


def calculate_time(start, stop):

    difference = stop - start
    seconds = float(str(difference.total_seconds()))
    return str(datetime.timedelta(seconds=seconds)).split(".")[0]


def first_check():


    if ping():

        live = "\nConnection Established\n"
        print(live)

        connection_acquired_time = datetime.datetime.now()
        acquiring_message = "Connection Established: " + \
                            str(connection_acquired_time).split(".")[0]
        print("~" * 60)
        print(acquiring_message)

        with open(FILE, "a") as file:


            file.write(live)
            file.write(acquiring_message)

        return True

    else:

        not_live = "\nNo Connection Found\n"
        print(not_live)
        print("~" * 60)
        with open(FILE, "a") as file:

            file.write(not_live)
        return False


def main():
    print("~" * 60)
    monitor_start_time = datetime.datetime.now()
    monitoring_date_time = "Started Monitoring: " + \
                           str(monitor_start_time).split(".")[0]
    print("~" * 60)

    if first_check():

        print(monitoring_date_time)


    else:

        while True:

            if not ping():

                time.sleep(1)
            else:


                first_check()
                print(monitoring_date_time)
                break

    with open(FILE, "a") as file:

        file.write("\n")
        file.write(monitoring_date_time + "\n")

main()
print("~" * 60)
print('''
╔═╗╔╗╔╔╦╗  ╔╗╔╔═╗╔╦╗╦ ╦╔═╗╦═╗╦╔═  ╔═╗╔═╗╔╗╔╔╗╔╔═╗╔═╗╔╦╗╦╔═╗╔╗╔  ╔═╗╔═╗╔═╗╔╗╔┬
║╣ ║║║ ║║  ║║║║╣  ║ ║║║║ ║╠╦╝╠╩╗  ║  ║ ║║║║║║║║╣ ║   ║ ║║ ║║║║  ╚═╗║  ╠═╣║║║│
╚═╝╝╚╝═╩╝  ╝╚╝╚═╝ ╩ ╚╩╝╚═╝╩╚═╩ ╩  ╚═╝╚═╝╝╚╝╝╚╝╚═╝╚═╝ ╩ ╩╚═╝╝╚╝  ╚═╝╚═╝╩ ╩╝╚╝o''')
print("~" * 60)
print(r'''
╦  ╦╦╔═╗╦ ╦  ╔═╗╦═╗╔═╗╦ ╦╔═╗╔═╗ ┬ ╦ ╦╔═╗╔═╗╦═╗╔═╗  ╔═╗╔═╗╔═╗╔╗╔   
╚╗╔╝║║╣ ║║║  ║ ╦╠╦╝║ ║║ ║╠═╝╚═╗┌┼─║ ║╚═╗║╣ ╠╦╝╚═╗  ╚═╗║  ╠═╣║║║   
 ╚╝ ╩╚═╝╚╩╝  ╚═╝╩╚═╚═╝╚═╝╩  ╚═╝└┘ ╚═╝╚═╝╚═╝╩╚═╚═╝  ╚═╝╚═╝╩ ╩╝╚╝ooo''')
print("~" * 60)
import grp
groups = grp.getgrall()
for group in groups:
    for user in group[3]:
        print(user, group[0])
print("~" * 60)
print(r'''
╔═╗╔╗╔╔╦╗  ╔═╗╦═╗╔═╗╦ ╦╔═╗╔═╗ ┬ ╦ ╦╔═╗╔═╗╦═╗╔═╗  ╔═╗╔═╗╔═╗╔╗╔   
║╣ ║║║ ║║  ║ ╦╠╦╝║ ║║ ║╠═╝╚═╗┌┼─║ ║╚═╗║╣ ╠╦╝╚═╗  ╚═╗║  ╠═╣║║║   
╚═╝╝╚╝═╩╝  ╚═╝╩╚═╚═╝╚═╝╩  ╚═╝└┘ ╚═╝╚═╝╚═╝╩╚═╚═╝  ╚═╝╚═╝╩ ╩╝╚╝ooo''')
print("~" * 60)

print(r'''
╔╦╗╦ ╦╔═╗╔╗╔╦╔═╔═╗  ╔═╗╔═╗╦═╗  ╦ ╦╔═╗╦╔╗╔╔═╗  ╔═╗╔╦╗╔═╗┬
 ║ ╠═╣╠═╣║║║╠╩╗╚═╗  ╠╣ ║ ║╠╦╝  ║ ║╚═╗║║║║║ ╦  ║╣  ║ ╠═╣│
 ╩ ╩ ╩╩ ╩╝╚╝╩ ╩╚═╝  ╚  ╚═╝╩╚═  ╚═╝╚═╝╩╝╚╝╚═╝  ╚═╝ ╩ ╩ ╩o''')

