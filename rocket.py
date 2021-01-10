#Authonr: Cavasin Elia aka hackername
#Scope: Privilege escalation scan

#How it works:
# ////////////////////////////////////////////////////////////////////////////////////////////////////////


#SEARCH EXPLOITS
# $sudo -l  or   find / -perm /4000 -type f -exec ls -ld {} \; 2>/dev/null    sudoers file
# $uname -a     kernel + os information
# $lsb_release -a       ubuntu version if installed
# $ps aux       view prg installed
# $ps aux | grep root       prgs as root
# $cat /etc/passwd      view file /etc/passwd for view usrs
# $cat /etc/passwd | cut -d : -f 1      view file /etc/passwd for view super users
# $ls -lah /home
# $ls -lha /var/www/


#VIEW SOME LOG FILES
# $ls -alh /var/log
# $ls -alh /var/lib/mysql


#SEARCH USR.TXT FLAG
# $find | grep usr.txt


#for more info visit: https://hacktips.it/guida-privilege-escalation-sistemi-linux/

# ////////////////////////////////////////////////////////////////////////////////////////////////////////


#importing some libraries...

import sys
import os 
import subprocess
from os import system                       #for execute bash command from python 
import platform                 #for search system info in os_scan()
#import time
#from datetime import datetime
 


#define some classes...

class color():
   
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    underline = '\033[4m'
    reset = '\033[0m'




#define some functions...

#searching the installed programms
def file(file):

    print("\n" * 2)

    try:

    	with open(file, 'r') as f:     #open file in input

        	content = f.read()
        	print(content)

    except IOError as error:
    	print(color.red + str(error) + color.reset)


    print(color.blue + "\n [*] " + file + " scan completed!" + color.reset)




#take a look inside a dir... 
def dir(dirs):

    print("\n" * 2)

    try:
        #inputs
        path = dirs
        directory = os.listdir(path)
    

        #searching the dirs...
        for file in directory:
            print("\n" + file)          #print file
        

        print(color.blue + "\n[*]" + path + " directory scan completed!" + color.reset)

    except:
        print(color.red + "there was an error..." + color.reset)
        print(color.red + "\n[*]" + path + " directory scan not completed" + color.reset)




def controll(file):

    print("\n" * 2)   

    try:
        with open(file, 'w') as f:     #open file in input
            content = "The file is writable (delete me)"        #change this 

            #writing on the file
            f.write(content)
            f.close()

        print(color.green + "[+]the file is writable!" + color.reset)


    except (IOError, OSError) as e:
        print(color.red + "[-]" + str(e) + color.reset)

    except:
        print(color.red + "[-] ERROR: error don't know" + color.reset)


    finally:    
        print(color.blue + "[*]Controll of the permissions of the" + file + "completed" + color.reset)




def banner():
    print('''
     

      |
     | |
    |   |
   |     |
  |this is|
 |=========|
 |    a    |
 |         |
 |    r    |
 |    o    |
 |    c    |
 |    k    |
 |    e    |
 |    t    |
  |       |
   |     |
    |   |
     ===
    |777|
   |77777|
  |7777777|
  |7777777|
  |7777777|
   |77777|
    |777|
     |7|
      7
''')  










#run programm

#print("scan started" + datetime.now())
print("\n" * 2)


#import terminal...
os.environ['TERM'] = 'screen'
#Type = os.name()

#clear screen

system('clear')

#run programm
print("scan started")
print("\n" * 2)

banner()
print("\n")

#suid files + sudoers files
try:

    try:

        os.system("find / -perm /4000 -type f -exec ls -ld {} \; 2>/dev/null")      #search with find


        os.system("sudo -l")                    #use sudo -l

        print("\n" + color.blue + "[*] Sudoers file scan completed!" + color.reset)
        print("\n" * 2)


    except KeyboardInterrupt:               #if CTRL+C exit
            print(color.red + "You pressed ctrl + c" + color.reset)

    except:                                 #if there are other errors
            print(color.red + "There was a problem..." + color.reset)

finally:
        print(color.blue + "\n[*] Sudoers file scan completed!" + color.reset)



#/etc/lsb-release
file('/etc/lsb-release')




#os scan
print("\n" * 2)


kernel = platform.release()                 

print(platform.system())    #linux, windows ecc...
print(kernel)       #kernel


if kernel >= "5.4.0":
    print(color.green + "\n[*] The kernel has a good version" + color.reset)

else:
    print(color.red + "\n[-] The kernel has a old version, search for vulnerabilities" + color.reset)

print(color.blue + "\n[*] information scan completed!" + color.reset)

#id info
try:
    os.system("id")         #id info

except:
    print(color.red + "\n[-] There was an error..." + color.reset)

finally:
    print(color.blue + "\n[*] id scan completed!" + color.reset)




#info running programm    
v = sys.version

if v == "2.7":

    proc1 = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
    proc2 = subprocess.Popen(['grep', 'root'], stdin=proc1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    proc1.stdout.close()         # Allow proc1 to receive a SIGPIPE if proc2 exits.
    out, err = proc2.communicate()

    print('out: {0}'.format(out))
    print('err: {0}'.format(err))

    print(color.blue + "\n[*] programm running as root scan completed!" + color.reset)

else:
    os.system("ps aux | grep root")
        
    print(color.blue + "\n[*] programm running as root scan completed!" + color.reset)




#/etc/passwd
file('/etc/passwd')         #change parametrer, this p

#/etc/crontab
file('/etc/crontab')       

#/var/www/wp-config
file('/var/www/wp-config')

#controll if some fiel is writable
controll('/etc/hosts')         #change parametrer, this parametrer is default

#/home
dir('/home')        #change parametrer, this parametrer is default

#/var/log
dir('/var/log')         #change parametrer, this parametrer is default

#/var/lib/mysql
dir('/var/lib/mysql')       #change parametrer, this parametrer is default

#/var/www
dir('/var/www')         #change parametrer, this parametrer is default

#print("\nscan finished" + datetime.now())