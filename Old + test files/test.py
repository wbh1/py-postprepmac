import imp
import getpass
import sys
import os
import requests
import time
import urllib
import subprocess

sudoPass = getpass.getpass("Enter password for sudo usage:")

def download2(url, filename):
   # NOTE the stream=True parameter
   dl = requests.get(url, timeout=15, stream=True)
   with open(filename, 'wb') as f:
      for chunk in dl.iter_content(chunk_size=1024):
         if chunk:  # filter out keep-alive new chunks
            f.write(chunk)
            f.flush()
   fpath = os.path.realpath(filename)
   kbsize = int(dl.headers['content-length'])  # filesize in bytes
   filesize = kbsize / 1000000  # gets the filesize in bytes -> converts to MB
   curSize = os.path.getsize(fpath)
   print('Downloaded: "%s" (~%s MB)' % (filename, filesize))  # %s references the variable listed in order
   if curSize != kbsize:
      print(progressPls())
   else:
      print("")

def Java_unmnt():
    os.system('hdiutil detach /Volumes/Java\ 8\ Update\ 51/ -quiet')

def Java_mnt():
    os.system('hdiutil attach ~/Java.dmg -nobrowse -quiet')
    print("Java.dmg mounted.\n")

def Java():
    download2('http://javadl.sun.com/webapps/download/AutoDL?BundleId=108140', 'Java.dmg')


Java()
Java_mnt()

javastring = '/Volumes/Java\ 8\ Update\ 51/Java\ 8\ Update\ 51.pkg'
javainstall = 'echo %s | sudo -S installer -pkg %s -target /' % (sudoPass, javastring)

os.system(javainstall)




os.system('cp /Volumes/Flash\ Player/Install\ Adobe\ Flash\ Player.app/ /Volumes/')
    os.system('cd /Volumes')
    os.system('echo %s | sudo ./Install\ Adobe\ Flash\ Player.app/Contents/MacOS/Adobe\ Flash\ Player\ Install\
     Manager -install') % (sudoPass)