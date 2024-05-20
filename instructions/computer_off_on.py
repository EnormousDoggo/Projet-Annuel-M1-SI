import os
import platform

def shutdown():
    if platform.system() == "Windows":
        os.system('shutdown -s')
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("shutdown -h now")
    else:
        print("Os not supported!")

def restart():
    if platform.system() == "Windows":
        os.system("shutdown -t 0 -r -f")
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system('reboot now')
    else:
        print("Os not supported!")

def hibernate():
    if platform.system() == "Windows":
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system('systemctl suspend')
    else:
        print("Os not supported!")


def logoff():
    if platform.system() == "Windows":
        os.system("shutdown -l")
    #elif platform.system() == "Linux" or platform.system() == "Darwin":
    #    os.system('reboot now')
    else:
        print("Os not supported!")

command = input("Use \'r\' => restart , \'s\' => shutdown , \'h\'  => hibernate,  \'l\'  => logoff: ").lower()

if command == "r":
    restart()
elif command == "s":
    shutdown()
elif command == "h":
    hibernate()
elif command == "l":
    logoff()
else:
    print("Wrong letter")