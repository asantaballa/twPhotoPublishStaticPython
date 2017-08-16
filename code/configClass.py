import argparse

class configClass:

    def __init__(self):
        self.photoInDir = '?'
        self.photoOutDir = '?'
        self.photoImageDir = '?'

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

        self.photoInDir = args.photoInDir
        self.photoOutDir = args.photoOutDir
        self.photoImageDir = args.photoImageDir

        print('DirIn:', self.photoInDir)
        print('DirOut:', self.photoOutDir)
        print('Images URL:', self.photoImageDir)        