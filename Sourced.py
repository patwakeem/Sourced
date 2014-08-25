#!/usr/bin/python
'''
Created on Apr 28, 2014
@author: patrickW

Source daemon code: Watches a certain directory (specified by SourcedMain) for a file match (also specified by SourcedMain). When a file is found processFiles method is triggered.

'''

import time
import glob
import os

class SourceDaemon(object):

    def __init__(self, direc, fil):
        
        self.foundFiles = False
        self.filter = fil
    
        if (direc.endswith("/")):
            pass
        else:
            direc = direc + "/"

        self.directory = direc
   
    def processFiles(self, fileList):
        
        for f in fileList:
		
		#File names and directory names have been simplified.
		
            lFile = f + ".log"
            os.popen("/home/processingScript.sh " + f + " > " + lFile)
            os.popen("mv " + f + " /home/processed/")
            os.chmod(lFile, 0666)
            os.popen("cat " + lFile + " >> /tmp/logFile.log")
            os.popen("cat "+  lFile + " | mail -s \"SourceID Processed\" email@example.com")
    
    def start(self):

        while (True):
            
            fileList = glob.glob(self.directory + self.filter)
        
            if (len(fileList) == 0):
                foundFiles = False
            else:
                foundFiles = True            
                  
            if (foundFiles):
				#The files we expect are very small so we give them 15s to fully copy. If the files were extremely large this would have to be a bit more involved.
                time.sleep(15)
                self.processFiles(fileList)
            else:    
                time.sleep(60)
                
