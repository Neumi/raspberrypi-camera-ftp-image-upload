import ftplib
from picamera import PiCamera
import time
import os

ftpUser = 'fpt-user'
ftpServer = 'example.com'
ftpPassword = 'MY-FTP-PASSWORD-123456'

ts = int(time.time())
imageName = 'image_ts_' + str(ts) + '.jpg'
imagePathOnRaspberry = os.path.dirname(os.path.realpath(__file__)) + '/images/' + imageName
imagePathOnServer = 'images/' + imageName # on the remote server sould be a 'images' dir in the ftp root (eg. webroot)

camera = PiCamera()
camera.resolution = (1920,1440)
camera.capture(imagePathOnRaspberry)

session = ftplib.FTP(ftpUser, ftpServer, ftpPassword)
file = open(imagePathOnRaspberry,'rb') # take image from here
session.storbinary('STOR ' + imagePathOnServer, file) # put image to here
file.close()
session.quit()
