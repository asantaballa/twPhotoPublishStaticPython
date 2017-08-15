import argparse
import os
import datetime

#-- globals

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
    
    parser = argparse.ArgumentParser(description='Short sample app')

    parser.add_argument('-pin', action="store", dest="photoInDir")
    parser.add_argument('-pout', action="store", dest="photoOutDir")
    parser.add_argument('-piurl', action="store", dest="photoImageDir")

    global args
    args = parser.parse_args([
          '-pin', '../photos_in'
        , '-pout', '/Users/albertosantaballa/temp'
        , '-piurl', 'http://someimagestorage.com/al/images'
        ]); 

    print('DirIn:', args.photoInDir)
    print('DirOut:', args.photoOutDir)
    print('Images URL:', args.photoImageDir)

#--

print("PhotoStatic")

getArgs()

outputFullDirName = os.path.join(args.photoOutDir,
                                 'webout' + datetime.datetime.now().strftime("_%Y%m%d_%H%M%S"))
assureDir(outputFullDirName)
processDir(args.photoInDir)

