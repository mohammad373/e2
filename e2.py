# e2

import os
import sys
import time
import socket
import requests
from colorama import Fore
import webbrowesr as web

def __target__():
    time.sleep(1)
    clear = input(Fore.RED + "\n[!] ~ Are Clear Text In Terminal (y , n) ==>  ")
    if clear.lower() == "y":
        time.sleep(1)
        os.system("clear")
    if clear.lower() == "n":
        print("")
    if clear == "" or None:
        try:
            print(Fore.RED + "\n[!] Error : Your Input Is None Or Not Found ;(")
            time.sleep(1)
            sys.exit()
        except:
            pass

    time.sleep(1)
    print( Fore.BLUE + "[*]"+ Fore.YELLOW +" ~ " + Fore.GREEN + "So . Pleass 3 Sec Wail ;)")
    time.sleep(3)
    wp = input(Fore.BLUE + "\n[" + Fore.RED + "!" + Fore.BLUE + "]" + Fore.RED + " ~ " +Fore.GREEN + "Are You Target Is WordPress ? ( 1 : yes | 2: no )" + Fore.YELLOW + " ==>  ")
    if wp == "" or None:
        try:
            time.sleep(1)
            print(Fore.RED + "Error : Your Input Is None Or Not Found ;(")
            time.sleep(1)
            sys.exit()
        except:
            pass
    if wp == "1":
        time.sleep(1)
    if wp == "2":

            time.sleep(1)
            print(Fore.RED + "\n[" + Fore.BLUE + "!" + Fore.RED + "]" + Fore.BLUE + " ~ " + Fore.YELLOW + "Error : Your Target Is Not WordPress ;(")
            time.sleep(1)
            sys.exit()


    #----
    clear2 = input(Fore.RED + "\n[!] ~ Are Clear Text In Terminal (y , n) ==>  ")
    if clear2 == "" or None:
        try:
            time.sleep(1)
            print(Fore.RED + "\n[!] ~ Error : Your Input Is None Or Not Found ;(")
            time.sleep(1)
            sys.exit()
        except:
            pass
    if clear2.lower() == "y":
        time.sleep(1)
        os.system("clear")
        
    if clear2.lower() == "N":
        time.sleep(1)
        print("")
  

    # ----
    #       /wp-content/plugins/
    time.sleep(1)
    target = input(Fore.RED + "\n[" + Fore.BLUE + "*" + Fore.RED + "]" + Fore.BLUE + " ~ " + Fore.GREEN + "Pleass Enter Your Address Target" + Fore.YELLOW + " ==>  ")
    if target == "" or None:
        try:
            time.sleep(1)
            print(Fore.RED + "\n[!] ~ Error : Your Input Is None Or Not Found ;(")
            time.sleep(1)
            sys.exit()
        except:
            pass
    m = requests.get("http://" + target + "/wp-content/plugins/")
    if m.status_code == 404 or m.status_code == 500:
        try:
            time.sleep(1)
            print(Fore.RED + "\n[!]" + Fore.BLUE + " ~ " + Fore.RED + "Error : Sory , Your Target Is Not WordPreass ;(")
            time.sleep(1)
            sys.exit()
        except:
            pass
    else:
        time.sleep(1)
        print(Fore.GREEN + "\n[+]" + Fore.BLUE + " ~ " + Fore.GREEN + "Ok , Your Target Is WordPreass :)\n")
        time.sleep(0.2)
    # ------
    my_list = ["xmlrpc"]
    for i in my_list:
        time.sleep(0.1)
        test = requests.get("http://" + target + "/wp-content/plugins/" + i)
        if test.status_code == 404 or test.status_code == 500:
            try:
                time.sleep(1)
                print(Fore.RED + "[!]" + Fore.BLUE + " ~ " + Fore.RED + "Error : Your Xmlrpc Target Is Close ;(")
                time.sleep(1)
                sys.exit()
            except:
                pass
        if test.status_code != 404 or test.status_code != 500:
            time.sleep(1)
            print(Fore.GREEN + "[+]" + Fore.BLUE + " ~ " + Fore.GREEN + "Ok , Your Xmlrpc Target Is Open ;)")
    #  ------


    e1 = input(Fore.RED + "\n[!]" + Fore.BLUE + " ~ " + Fore.RED + "Do You Want To Continue ( 1 : yes  |  2 : no )" + Fore.YELLOW + " ==>  ")
    if e1 == "" or None:
        try:
            print(Fore.RED + "\n[!]" + Fore.BLUE + " ~ " + Fore.RED + "Error : Your Input Is None Or Not Found ;(")
            time.sleep(1)
            sys.exit()
        except:
            pass
    if e1 == "1":
        pass
    if e1 == "2":
        time.sleep(1)
        sys.exit()


    # who.is
    time.sleep(1)
    i1 = input(Fore.BLUE + "\n[" + Fore.RED + "!" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Enter Your Number ( 1 : Whois  |  2 : Next  |  3 : Exit )" + Fore.GREEN + " ==>  ")
    if i1 == "" or None:
        try:
            time.sleep(1)
            print(Fore.RED + "\n[!]" + Fore.BLUE + " ~ " + Fore . RED + "Error : Your Input Is None Or Not Found ;(")
            time.sleep(1)
            sys.exit()
        except:
            pass
    if i1 == "1":
        time.sleep(1)
        clear3 = input(Fore.RED + "\n[!] ~ Are Clear Text In Terminal (y , n) ==>  ")
        if clear.lower() == "y":
            time.sleep(1)
            os.system("clear")
        if clear.lower() == "n":
            print("")
        if clear == "" or None:
            try:
                print(Fore.RED + "\n[!] Error : Your Input Is None Or Not Found ;(")
                time.sleep(1)
                sys.exit()
            except:
                pass
        w1 = input(Fore.BLUE + "\n[" + Fore.RED + "!" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Pleass Enter your Number ( 1 : Open Whois  |  2 : Paste Link )" + Fore.GREEN + " ==>  ")
        ip = socket.gethostbyname(target)
        if w1 == "" or None:
            try:
                time.sleep(1)
                print(Fore.RED + "\n[!]" + Fore.BLUE + " ~ " + Fore.RED + "Error : Your Input Is None Or Not Found ;(")
                time.sleep(1)
                sys.exit()
            except:
                pass
        if w1 == "1":
            time.sleep(1)
            print(Fore.YELLOW + "\n[" + Fore.RED + "!" + Fore.YELLOW + "]" + Fore.RED  + " ~ " + Fore.BLUE + "Pleass 5 Sec Later ...")
            time.sleep(1)
            print(Fore.YELLOW + "[" + Fore.RED + "!" + Fore.YELLOW + "]" + Fore.RED  + " ~ " + Fore.BLUE + "Pleass 4 Sec Later ...")
            time.sleep(1)
            print(Fore.YELLOW + "[" + Fore.RED + "!" + Fore.YELLOW + "]" + Fore.RED  + " ~ " + Fore.BLUE + "Pleass 3 Sec Later ...")
            time.sleep(1)
            print(Fore.YELLOW + "[" + Fore.RED + "!" + Fore.YELLOW + "]" + Fore.RED  + " ~ " + Fore.BLUE + "Pleass 2 Sec Later ...")
            time.sleep(1)
            print(Fore.YELLOW + "[" + Fore.RED + "!" + Fore.YELLOW + "]" + Fore.RED  + " ~ " + Fore.BLUE + "Pleass 1 Sec Later ...")
            time.sleep(1)
            wb = "https://who.is/whois-ip/ip-address/" + ip
            web.open(wb)
            time.sleep(1)
        if w1 == "2":
            time.sleep(1)
            print(Fore.YELLOW + "\n[" + Fore.RED + "!" + Fore.YELLOW + "]" + Fore.RED  + " ~ " + Fore.BLUE + "Pleass 5 Sec Later ...")
            time.sleep(1)
            print(Fore.YELLOW + "[" + Fore.RED + "!" + Fore.YELLOW + "]" + Fore.RED  + " ~ " + Fore.BLUE + "Pleass 4 Sec Later ...")
            time.sleep(1)
            print(Fore.YELLOW + "[" + Fore.RED + "!" + Fore.YELLOW + "]" + Fore.RED  + " ~ " + Fore.BLUE + "Pleass 3 Sec Later ...")
            time.sleep(1)
            print(Fore.YELLOW + "[" + Fore.RED + "!" + Fore.YELLOW + "]" + Fore.RED  + " ~ " + Fore.BLUE + "Pleass 2 Sec Later ...")
            time.sleep(1)
            print(Fore.YELLOW + "[" + Fore.RED + "!" + Fore.YELLOW + "]" + Fore.RED  + " ~ " + Fore.BLUE + "Pleass 1 Sec Later ...")
            time.sleep(1)
            link1 = "https://who.is/whois-ip/ip-address/" + ip
            print(Fore.RED + "\n[" + Fore.BLUE + "+" + Fore.RED + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Your Link Whois : " + link1)
            time.sleep(1)
    if i1 == "2":
        time.sleep(1)
        print("")
    if i1 == "3":
        time.sleep(1)
        sys.exit()
    # --------------

    e2 = input(Fore.RED + "\n[!]" + Fore.BLUE + " ~ " + Fore.RED + "Do You Want To Continue ( 1 : yes  |  2 : no )" + Fore.YELLOW + " ==>  ")
    if e2 == "" or None:
        try:
            print(Fore.RED + "\n[!]" + Fore.BLUE + " ~ " + Fore.RED + "Error : Your Input Is None Or Not Found ;(")
            time.sleep(1)
            sys.exit()
        except:
            pass
    if e2 == "1":
        pass
    if e2 == "2":
        time.sleep(1)
        sys.exit()

    # ip target

    time.sleep(1)
    i2 = input(Fore.BLUE + "\n[" + Fore.RED + "!" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Enter Your Number ( 1 : Ip Target  |  2 : Next  |  3 : Exit )" + Fore.GREEN + " ==>  ")
    if i2 == "" or None:
        try:
            time.sleep(1)
            print(Fore.RED + "\n[!]" + Fore.BLUE + " ~ " + Fore.RED + "Error : Your Input Is None Or Not Found ;(")
            time.sleep(1)
            sys.exit()
        except:
            pass
    if i2 == "1":
        time.sleep(0.1)
        ip2 = socket.gethostbyname(target)
        print(Fore.YELLOW + "\n[" + Fore.RED + "!" + Fore.YELLOW + "]" + Fore.RED  + " ~ " + Fore.BLUE + "Pleass 5 Sec Later ...")
        time.sleep(1)
        print(Fore.YELLOW + "[" + Fore.RED + "!" + Fore.YELLOW + "]" + Fore.RED  + " ~ " + Fore.BLUE + "Pleass 4 Sec Later ...")
        time.sleep(1)
        print(Fore.YELLOW + "[" + Fore.RED + "!" + Fore.YELLOW + "]" + Fore.RED  + " ~ " + Fore.BLUE + "Pleass 3 Sec Later ...")
        time.sleep(1)
        print(Fore.YELLOW + "[" + Fore.RED + "!" + Fore.YELLOW + "]" + Fore.RED  + " ~ " + Fore.BLUE + "Pleass 2 Sec Later ...")
        time.sleep(1)
        print(Fore.YELLOW + "[" + Fore.RED + "!" + Fore.YELLOW + "]" + Fore.RED  + " ~ " + Fore.BLUE + "Pleass 1 Sec Later ...")
        time.sleep(1)
        print(Fore.GREEN + "\n[+]" + Fore.BLUE + " ~ " + Fore.GREEN + "Your p Target : " + ip2)
    if i2 == "2":
        time.sleep(1)
        print("")
    if i2 == "3":
        time.sleep(1)
        sys.exit()
    # --------
__target__()
