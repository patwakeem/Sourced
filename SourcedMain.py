#!/usr/bin/python
'''
Created on Apr 28, 2014
@author:patrickW

To do:

Use daemonize code from snippets to turn this into a proper daemon.


'''

from Sourced import SourceDaemon
import os
import sys
import signal

def usage():
    print("USAGE: ./SourcedMain.py $COMMAND")
	print("USAGE: $COMMAND can be start, stop, restart or status.")

def start():
    
    print("\nStarting source ID daemon.")
    try:
        lockFile = "/var/run/sourced.lock"
        
        if (os.path.exists(lockFile)):
            sys.exit(5)
        
        else:
            f = file(lockFile, "w")
            f.write(str(os.getpid()))
            f.close()

		#Directory name + file scheme stripped out.
        sd = SourceDaemon("/home/directory/","File*.csv")
        print("Source ID Daemon has been started.")
        sd.start()
        
    
    except SystemExit, be:
        print(be)
        print("Lockfile exists, Exiting. If you believe that this is in error you may remove the lockfile with 'rm " + lockFile + "'")
    
    except Exception, e: 
        print("exception caught " + e)

def stop():
    
    print("\nStopping source ID daemon.")
    try:
        lockFile = "/var/run/sourced.lock"
        
        if (not os.path.exists(lockFile)):
            sys.exit(6)
        
        else:
            pidFile = open(lockFile, "r")
            pID = str(pidFile.readline())
            pID = pID.strip()
            process = int(pID)
            os.kill(process, signal.SIGKILL)
            pidFile.close()
            os.remove(lockFile)
            print("Source ID Daemon has been stopped.")
    
    except SystemExit, be:
        print("Lockfile does not exist. Exit 6.")
        sys.exit(6)
    
    except Exception, e: 
        print("exception caught " + e)

def restart():
    stop()
    start()
    
#This could be implemented better; it should actually see if that pid is running and if so what is running under that pid.
def status():

    lockFile = "/var/run/sourced.lock"
	
    if (os.path.exists(lockFile)):
        pidFile = open(lockFile, "r")
        pID = str(pidFile.readline())
        pID = pID.strip()      
        print("\nSource ID Daemon is running. PID: " + pID)
        pidFile.close()
    else:
        print("\nSource ID Daemon is stopped.")
    

if __name__ == '__main__':
    
    try:
		#this script should be called by the Sourced.init.sh script but if not we don't want to deal with case sensitivity here.
        switch = str(sys.argv[1]).lower()
        if (switch == "start"):
            start()
        elif (switch == "stop"):
            stop()
        elif (switch == "restart"):
            restart()
        elif (switch == "status"):
            status()
        else:
            usage()

    except SystemExit, be:
        sys.exit(6)
        
    except:
        usage()
