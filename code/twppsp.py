import os
import datetime
import generator
import configClass
import sys

#--

def processDir(dirName):
    
    for file in os.listdir(dirName):
        fullFileName = os.path.join(dirName, file)
        if os.path.isdir(fullFileName) == True:
            print('Dir: ', file, ':', fullFileName)  
            processDir(fullFileName)
        else:
            print('File: ', file) 

#--

def assureDir(fullDirName):
    
    if not os.path.exists(fullDirName):
        os.makedirs(fullDirName)

#--

def getArgs():
    global config
    config = configClass.configClass()    #-- Instatiate config and make it like a module

#--

print("PhotoStatic")

getArgs()

outputFullDirName = os.path.join(config.photoOutDir,
                                 'webout' + datetime.datetime.now().strftime("_%Y%m%d_%H%M%S"))
assureDir(outputFullDirName)
processDir(config.photoInDir)

genx = generator.generator()
genx.generate()

