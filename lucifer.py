#!/usr/bin/env python2
#    ______              _      _           _______
#   |  ____|            (_)    | |         |__   __|
#   | |__ ___  ___   ___ _  ___| |_ _   _     | | ___  __ _ _ __ ___
#   |  __/ __|/ _ \ / __| |/ _ \ __| | | |    | |/ _ \/ _` | '_ ` _ \
#   | |  \__ \ (_) | (__| |  __/ |_| |_| |    | |  __/ (_| | | | | | |
#   |_|  |___/\___/ \___|_|\___|\__|\__, |    |_|\___|\__,_|_| |_| |_|
#                                    __/ |
#                                   |___/
#
#
#                                Greet's To
#                              IcoDz - Canejo
#                             Tool For Hacking
#                             Author : Manisso

'''
Imports
'''
import sys
import argparse
import os
import http.client
import subprocess
import re
import urllib.request, urllib.error, urllib.parse
import socket
import urllib.request, urllib.parse, urllib.error
import sys
import json
import telnetlib
import glob
import random
import queue
import threading
import base64
import time
import configparser
from sys import argv
from subprocess import *
from getpass import getpass
from xml.dom import minidom
from urllib.parse import urlparse
from optparse import OptionParser
from time import gmtime, strftime, sleep

'''
Common Functions
'''


class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'


def clearScr():
    os.system('clear')


def yesOrNo():
    return (input("Continue Y / N: ") in yes)

def check_permissions():
    if os.getuid() == 0:
        os.system('clear')
        print("{0}[!]{1} Must be run with root: {2}sudo {1}python3 lucifer.py")
        exit(0)

'''
Config
'''
installDir = os.path.dirname(os.path.abspath(__file__)) + '/'
configFile = installDir + "/lucifer.cfg"
print(installDir)
config = configparser.RawConfigParser()
config.read(configFile)

toolDir = installDir + config.get('lucifer', 'toolDir')
logDir = installDir + config.get('lucifer', 'logDir')
yes = config.get('lucifer', 'yes').split()
color_random=[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.UNDERLINE,color.LOGGING]
random.shuffle(color_random)
luciferlogo = color_random[0] + '''
          _                       _    __               
 | |                     (_)  / _|              
 | |       _   _    ___   _  | |_    ___   _ __ 
 | |      | | | |  / __| | | |  _|  / _ \ | '__|
 | |____  | |_| | | (__  | | | |   |  __/ | |   
 |______|  \__,_|  \___| |_| |_|    \___| |_|   
                                                
        '''
luciferPrompt = "lucifer ~# "
alreadyInstalled = "Already Installed"
continuePrompt = "\nClick [Return] to continue"


'''
Starts Menu Classes
'''
class lucifer:
    def __init__(self):
        clearScr()
        self.createFolders()
        print((luciferlogo + color.RED + '''
       }--------------{+} Coded By Manisso {+}--------------{
       }--------{+}  GitHub.com/Manisso/lucifer {+}--------{
    ''' + color.END + '''
       {1}--Reconnaissance
       {2}--Delivery
       {3}--Command & Control
       {4}--Exploitation Tools
       {5}--Post Exploitation
       {6}--UPDATE
       {99}-EXIT\n
     '''))
        print()

        choice = input(luciferPrompt)
        clearScr()
        if choice == "1":
            reconnaissanceMenu()
        elif choice == "2":
            deliveryMenu()
        elif choice == "3":
            command_contorlMenu()
        elif choice == "4":
            exploitationToolsMenu()
        elif choice == "5":
            postExploitationMenu()
        elif choice == "6":
            self.update()
        elif choice == "99":
            with open(configFile, 'wb') as configfile:
                config.write(configfile)
            sys.exit()
        elif choice == "\r" or choice == "\n" or choice == "" or choice == " ":
            self.__init__()
        else:
            try:
                print((os.system(choice)))
            except:
                pass
        self.completed()

    def createFolders(self):
        if not os.path.isdir(toolDir):
            os.makedirs(toolDir)
        if not os.path.isdir(logDir):
            os.makedirs(logDir)

    def completed(self):
        input("Completed, click return to go back")
        self.__init__()

    def update(self):
        os.system("cd lucifer && bash update.sh")
        os.system("lucifer")



'''
Reconnaissance Tools Classes
'''


class reconnaissanceMenu:
    menuLogo = '''
  _____                      
 |  __ \                     
 | |__) |___  ___ ___  _ __  
 |  _  // _ \/ __/ _ \| '_ \ 
 | | \ \  __/ (_| (_) | | | |
 |_|  \_\___|\___\___/|_| |_|
  
    '''

    def __init__(self):
        clearScr()
        print((self.menuLogo))

        print("  {1}--Active Intelligence Gathering")
        print("  {2}--Passive Intelligence Gathering")
        print("  {0}-Back To Main Menu \n")
        choice2 = input("recon ~# ")
        clearScr()
        if choice2 == "1":
            activeScan()
        elif choice2 == "2":
            passiveScan()
        elif choice2 == "0":
            lucifer()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        input("Completed, click return to go back")
        self.__init__()


def activeScan():

    print(activeMenu)
    choose = input("choose a number: ")
    while True:

        if choose == "1":
            sudomy()
        elif choose == "2":
            o365spray()
        elif choose == "3":
            spoofchecker()
        elif choose == "0":
            lucifer()
        else:
            activeScan()


def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]


############################
activeMenu = '''
\t 1: Sudomy
\t 2: O365spray
\t 3: Spoofchecker
\t 0: Back To Main Menu
'''

class sudomy:
    sudomyLogo = '''
   _____           _                       
  / ____|         | |                      
 | (___  _   _  __| | ___  _ __ ___  _   _ 
  \___ \| | | |/ _` |/ _ \| '_ ` _ \| | | |
  ____) | |_| | (_| | (_) | | | | | | |_| |
 |_____/ \__,_|\__,_|\___/|_| |_| |_|\__, |
                                      __/ |
                                     |___/ 
    '''

    def __init__(self):
        self.installDir = toolDir + "Sudomy"
        self.gitRepo = "https://github.com/screetsec/Sudomy.git"

        if not self.installed():
            self.install()
        clearScr()
        self.run()
        response = input(continuePrompt)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        os.system("git clone --recursive %s %s" %
                  (self.gitRepo, self.installDir))
        os.system("pip install -r %s/requirements.txt" % self.installDir)

        print("Add needed api's to sudomy.api")

    def run(self):
        os.system("bash %s/sudomy" % self.installDir)
        target = input("Enter Target Domain: ")
        os.system("bash %s/sudomy" % self.installDir % target)


class o365spray:
    o365sprayLogo = '''
   ____ ____    __ _____                           
  / __ \___ \  / /| ____|                          
 | |  | |__) |/ /_| |__  ___ _ __  _ __ __ _ _   _ 
 | |  | |__ <| '_ \___ \/ __| '_ \| '__/ _` | | | |
 | |__| |__) | (_) |__) \__ \ |_) | | | (_| | |_| |
  \____/____/ \___/____/|___/ .__/|_|  \__,_|\__, |
                            | |               __/ |
                            |_|              |___/ 
    '''

    def __init__(self):
        self.installDir = toolDir + "o365spray"
        self.gitRepo = "https://github.com/0xZDH/o365spray.git"

        if not self.installed():
            self.install()
        clearScr()
        self.run()
        response = input(continuePrompt)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        os.system("git clone %s %s" %
                  (self.gitRepo, self.installDir))
        os.system("pip install -r %s/requirements.txt" % self.installDir)
        os.system("cd %s && python setup.py build" % self.installDir)

    def run(self):
        target = input("Enter Target Domain: ")
        os.system("python %s/o365spray.py --validate --domain" % self.installDir % target)

class spoofchecker:
    spoofcheckerLogo = '''
   _____                    __     _               _             
  / ____|                  / _|   | |             | |            
 | (___  _ __   ___   ___ | |_ ___| |__   ___  ___| | _____ _ __ 
  \___ \| '_ \ / _ \ / _ \|  _/ __| '_ \ / _ \/ __| |/ / _ \ '__|
  ____) | |_) | (_) | (_) | || (__| | | |  __/ (__|   <  __/ |   
 |_____/| .__/ \___/ \___/|_| \___|_| |_|\___|\___|_|\_\___|_|   
        | |                                                      
        |_|                                                      
    '''

    def __init__(self):
        self.installDir = toolDir + "spoofchecker"
        self.gitRepo = "https://github.com/masquerad3r/spoofchecker.git"

        if not self.installed():
            self.install()
        clearScr()
        self.run()
        response = input(continuePrompt)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        os.system("git clone %s %s" %
                  (self.gitRepo, self.installDir))

    def run(self):
        target = input("Enter Target Domain: ")
        os.system("python %s/spoofdetect.py" % self.installDir % target)


def passiveScan():

    print(passiveMenu)
    choose = input("choose a number: ")
    while True:

        if choose == "1":
            sherlok()
        elif choose == "2":
            theHarvester()
        elif choose == "3":
            zoominfo_scraper()
        elif choose == "4":
            o365creeper()
        elif choose == "0":
            lucifer()
        else:
            passiveScan()


def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]


############################
passiveMenu = '''
\t 1: Sherlok
\t 2: theHarvester
\t 3: Zoominfo Scraper
\t 4: O365creeper
\t 0: Back To Main Menu
'''


class sherlok:
    sherlokLogo = '''
   _____ _               _       _    
  / ____| |             | |     | |   
 | (___ | |__   ___ _ __| | ___ | | __
  \___ \| '_ \ / _ \ '__| |/ _ \| |/ /
  ____) | | | |  __/ |  | | (_) |   < 
 |_____/|_| |_|\___|_|  |_|\___/|_|\_\

    '''

    def __init__(self):
        self.installDir = toolDir + "sherlok"
        self.gitRepo = "https://github.com/sherlock-project/sherlock.git"

        if not self.installed():
            self.install()
        clearScr()
        self.run()
        response = input(continuePrompt)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        os.system("git clone --recursive %s %s" %
                  (self.gitRepo, self.installDir))
        os.system("pip install -r %s/requirements.txt" % self.installDir)

    def run(self):
        os.system("bash %s/sudomy" % self.installDir)


class theHarvester:
    theHarvesterLogo = '''
   _   _          _    _                           _            
 | | | |        | |  | |                         | |           
 | |_| |__   ___| |__| | __ _ _ ____   _____  ___| |_ ___ _ __ 
 | __| '_ \ / _ \  __  |/ _` | '__\ \ / / _ \/ __| __/ _ \ '__|
 | |_| | | |  __/ |  | | (_| | |   \ V /  __/\__ \ ||  __/ |   
  \__|_| |_|\___|_|  |_|\__,_|_|    \_/ \___||___/\__\___|_|   

    '''

    def __init__(self):
        self.installDir = toolDir + "o365spray"
        self.gitRepo = "https://github.com/0xZDH/o365spray.git"

        if not self.installed():
            self.install()
        clearScr()
        self.run()
        response = input(continuePrompt)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        os.system("git clone %s %s" %
                  (self.gitRepo, self.installDir))
        os.system("pip install -r %s/requirements.txt" % self.installDir)
        os.system("cd %s && python setup.py build" % self.installDir)

    def run(self):
        os.system("python %s/o365spray.py" % self.installDir)

class zoominfo_scraper:
    zoominfoLogo = '''
  ______                     _        __      
 |___  /                    (_)      / _|     
    / / ___   ___  _ __ ___  _ _ __ | |_ ___  
   / / / _ \ / _ \| '_ ` _ \| | '_ \|  _/ _ \ 
  / /_| (_) | (_) | | | | | | | | | | || (_) |
 /_____\___/ \___/|_| |_| |_|_|_| |_|_| \___/ 
                                              
    '''

    def __init__(self):
        self.installDir = toolDir + "Sudomy"
        self.gitRepo = "https://github.com/0xZDH/o365spray.git"

        if not self.installed():
            self.install()
        clearScr()
        self.run()
        response = input(continuePrompt)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        os.system("git clone --recursive %s %s" %
                  (self.gitRepo, self.installDir))
        os.system("pip install -r %s/requirements.txt" % self.installDir)

    def run(self):
        os.system("python %s/spoofdetect.py" % self.installDir)


class XSStrike:
    XSStrikeLogo = '''
    Yb  dP .dP"Y8 .dP"Y8 888888 88""Yb 88 88  dP 888888
     YbdP  `Ybo." `Ybo."   88   88__dP 88 88odP  88__
     dPYb  o.`Y8b o.`Y8b   88   88"Yb  88 88"Yb  88""
    dP  Yb 8bodP' 8bodP'   88   88  Yb 88 88  Yb 888888
    '''

    def __init__(self):
        self.installDir = toolDir + "XSStrike"
        self.gitRepo = "https://github.com/UltimateHackers/XSStrike.git"

        if not self.installed():
            self.install()
        clearScr()
        print((self.XSStrikeLogo))
        self.run()
        response = input(continuePrompt)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        os.system("git clone  %s %s" %
                  (self.gitRepo, self.installDir))
        os.system("pip install -r %s/requirements.txt" % self.installDir)

    def run(self):
        os.system("python %s/xsstrike" % self.installDir)



class setoolkit:
    def __init__(self):
        self.installDir = toolDir + "setoolkit"
        self.gitRepo = "https://github.com/trustedsec/social-engineer-toolkit.git"

        if not self.installed():
            self.install()
            self.run()
        else:
            print(alreadyInstalled)
            self.run()
        response = input(continuePrompt)

    def installed(self):
        return (os.path.isfile("/usr/bin/setoolkit"))

    def install(self):
        os.system("apt-get --force-yes -y install git apache2 python-requests libapache2-mod-php \
            python-pymssql build-essential python-pexpect python-pefile python-crypto python-openssl")
        os.system("git clone  %s %s" %
                  (self.gitRepo, self.installDir))
        os.system("cd %s && python setup.py install" % self.installDir)

    def run(self):
        os.system("setoolkit")


class host2ip:
    host2ipLogo = '''
    88  88  dP"Yb  .dP"Y8 888888 oP"Yb. 88 88""Yb
    88  88 dP   Yb `Ybo."   88   "' dP' 88 88__dP
    888888 Yb   dP o.`Y8b   88     dP'  88 88"""
    88  88  YbodP  8bodP'   88   .d8888 88 88
    '''

    def __init__(self):
        clearScr()
        print((self.host2ipLogo))
        host = input("   Enter a Host: ")
        ip = socket.gethostbyname(host)
        print(("   %s has the IP of %s" % (host, ip)))
        response = input(continuePrompt)


class wpscan:
    wpscanLogo = '''
    Yb        dP 88""Yb .dP"Y8  dP""b8    db    88b 88
     Yb  db  dP  88__dP `Ybo." dP   `"   dPYb   88Yb88
      YbdPYbdP   88"""  o.`Y8b Yb       dP__Yb  88 Y88
       YP  YP    88     8bodP'  YboodP dP""""Yb 88  Y8
    '''

    def __init__(self):
        self.installDir = toolDir + "wpscan"
        self.gitRepo = "https://github.com/wpscanteam/wpscan.git"

        if not self.installed():
            self.install()
        clearScr()
        print((self.wpscanLogo))
        target = input("   Enter a Target: ")
        self.menu(target)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        os.system("git clone  %s %s" %
                  (self.gitRepo, self.installDir))

    def menu(self, target):
        clearScr()
        print((self.wpscanLogo))
        print(("   WPScan for: %s\n" % target))
        print("   {1}--Username Enumeration [--enumerate u]")
        print("   {2}--Plugin Enumeration [--enumerate p]")
        print("   {3}--All Enumeration Tools [--enumerate]\n")
        print("   {0}-Return to information gathering menu \n")
        response = input("wpscan ~# ")
        clearScr()
        logPath = "../../logs/wpscan-" + \
            strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".txt"
        wpscanOptions = "--no-banner --random-agent --url %s" % target
        try:
            if response == "1":
                os.system(
                    "ruby tools/wpscan/wpscan.rb %s --enumerate u --log %s" % (wpscanOptions, logPath))
                response = input(continuePrompt)
            elif response == "2":
                os.system(
                    "ruby tools/wpscan/wpscan.rb %s --enumerate p --log %s" % (wpscanOptions, logPath))
                response = input(continuePrompt)
            elif response == "3":
                os.system(
                    "ruby tools/wpscan/wpscan.rb %s --enumerate --log %s" % (wpscanOptions, logPath))
                response = input(continuePrompt)
            elif response == "0":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)


class CMSmap:
    CMSmapLogo = '''
     dP""b8 8b    d8 .dP"Y8 8b    d8    db    88""Yb
    dP   `" 88b  d88 `Ybo." 88b  d88   dPYb   88__dP
    Yb      88YbdP88 o.`Y8b 88YbdP88  dP__Yb  88"""
     YboodP 88 YY 88 8bodP' 88 YY 88 dP""""Yb 88
    '''

    def __init__(self):
        self.installDir = toolDir + "CMSmap"
        self.gitRepo = "https://github.com/Dionach/CMSmap.git"

        if not self.installed():
            self.install()
        clearScr()
        print((self.CMSmapLogo))
        target = input("   Enter a Target: ")
        self.run(target)
        response = input(continuePrompt)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        os.system("git clone  %s %s" %
                  (self.gitRepo, self.installDir))

    def run(self, target):
        logPath = "logs/cmsmap-" + \
            strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".txt"
        try:
            os.system("python %s/cmsmap.py -t %s -o %s" %
                      (self.installDir, target, logPath))
        except:
            pass


class doork:
    doorkLogo = '''
    8888b.   dP"Yb   dP"Yb  88""Yb 88  dP
     8I  Yb dP   Yb dP   Yb 88__dP 88odP
     8I  dY Yb   dP Yb   dP 88"Yb  88"Yb
    8888Y"   YbodP   YbodP  88  Yb 88  Yb
    '''

    def __init__(self):
        self.installDir = toolDir + "doork"
        self.gitRepo = "https://github.com/AeonDave/doork.git"

        if not self.installed():
            self.install()
        clearScr()
        print((self.doorkLogo))
        target = input("   Enter a Target: ")
        self.run(target)
        response = input(continuePrompt)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        os.system("git clone  %s %s" %
                  (self.gitRepo, self.installDir))
        os.system("pip install beautifulsoup4 requests Django==1.11")

    def run(self, target):
        if not "http://" in target:
            target = "http://" + target
        logPath = "logs/doork-" + \
            strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".txt"
        try:
            os.system("python %s/doork.py -t %s -o %s" %
                      (self.installDir, target, logPath))
        except KeyboardInterrupt:
            pass


    print('\n')

############################


if __name__ == "__main__":
    try:
        check_permissions()
        lucifer()
    except KeyboardInterrupt:
        choice = input('\n\n{0}[1] {1}Return lucifer {0}[2] {1}Exit \n{2}lucifer >> {1}')
        choice = choice.zfill(2)
        if choice == '01':
            if os.path.isfile('/usr/local/bin/lucifer'):
                os.system('clear && lucifer')
            else:
                os.system('clear && sudo python3 lucifer.py')   

        elif choice == '02':
            time.sleep(2)
            os.system('clear')
            print(" Finishing up...\n")
            time.sleep(0.25)
            exit(0)
        else:
            print("\n{}[x] Invalid Option.")
            time.sleep(2)   
            exit(0)
