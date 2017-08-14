import argparse
import os

def processDir(dirName):
    
    for file in os.listdir(dirName):
        # print('Processing: ', dirName);   
        # fullFileName = dirName + '/' + file;
        fullFileName = os.path.join(dirName, file);
        if os.path.isdir(fullFileName) == True:
            print('Dir: ', file, ':', fullFileName);   
            processDir(fullFileName);
        else:
            print('File: ', file);   

#--

print("Photo Publish Static");

parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('-pin', action="store", dest="photoInDir")
parser.add_argument('-pout', action="store", dest="photoOutDir")

#args = parser.parse_args(['-pin', '/Users/albertosantaballa/Dropbox/Devel/twPhotoPublishStaticPython/photos_in', '-pout', '../out']); 
args = parser.parse_args(['-pin', '../photos_in', '-pout', '../out']); 

print('DirIn:', args.photoInDir);
print('DirOut:', args.photoOutDir);

# for file in os.listdir(args.photoInDir):
#     print('File: ', file);   
#     if os.path.isdir(file) == True:
#         print('isdir');

processDir(args.photoInDir);

