from __future__ import print_function  # In Python 2.7, print is treated like a string. 3.0+ like a function.
# ^^ This imports print function from python 3.0 so that we are able to have progress indicators!!!!!
#!/usr/bin/env python
# ----------------------------------------------
# title: "PostprepMac - Python Edition"
version = "2.0"
# Author: Will Hegedus
# OG bash shout out: Lucas Messenger
# Updated: 6-26-2016
# Created: 7-29-2015
# Known bugs: Firefox Icon sometimes doesn't show up in the launchpad grid
# Last update: All new download function! Progress bar! Silent Flash install! Silent Air install! New Java!
# Requests module password prompt bug fixed!
# Previous updates:
# Fixed sudo permissions issue that was created by the previous update (8/20/2015)
# Fixed permissions error when installing requests module on some computers (8/19/2015)
# Modified Java link/updated timeout (8/17/2015)
# ----------------------------------------------
import imp
import getpass
import os

sudoPass = getpass.getpass("Enter password for sudo usage:")

try:
    imp.find_module("requests")  # Checks if requests module is installed
    found = True
except ImportError:
    found = False
if found == False:  # installs requests if not installed
    import os
    import sys
    os.system('clear')
    raw_input("A Python module needs to be installed. Rerun the script after it installs. \nPress enter to continue...")
    os.system('echo %s | sudo -S easy_install requests' % sudoPass)
    os.system('clear')
    sys.exit("Rerun the script.")
else:
    import os
    import requests
    import time
    import urllib
    import subprocess
    import sys
    from os.path import expanduser
#    from subprocess import Popen      this is no longer used but kept for future reference?


    def download1(url, filename):
        dl = requests.get(url, timeout=20, stream=True) # Note the stream=True part. 20 second timeout.
        kbsize = int(dl.headers['Content-Length'].strip())  # filesize in KB from url header
        filesize = int(kbsize/1000000)  # filesize in MB
        fpath = os.path.realpath(filename)  # gets the filepath being downloaded
        with open(filename, 'wb') as f:
            for chunk in dl.iter_content(1024):
                if chunk:
                    f.write(chunk)  # writes chunks to file
                    currentsize = int(os.path.getsize(fpath))
                    currentsize = currentsize / 1000000  # current size in MB
                    print("%i MB out of %i MB downloaded so far..." % (currentsize, filesize), end="\r")
                    f.flush()  # flush writes the stuff in the buffer to the disk
        print("")


def clear():
    os.system("clear")


def lines():
    print("-" * 30)


def done():
    print("Complete.")


def Firefox():
    download1('http://download.mozilla.org/?product=firefox-latest&os=osx&lang=en-US', 'Firefox.dmg')


def Shockwave():
    download1(
        'http://fpdownload.macromedia.com/get/shockwave/default/english/macosx/latest/Shockwave_Installer_Full_64bit.dmg',
        'Shockwave.dmg')


def Java():
    download1('http://javadl.oracle.com/webapps/download/AutoDL?BundleId=207766', 'Java.dmg')


def Silver():  # Silverlight is weird
    download1('http://go.microsoft.com/fwlink/?LinkID=229322', 'Silverlight.dmg')


def Flash():
    download1('http://fpdownload.macromedia.com/pub/flashplayer/latest/help/install_flash_player_osx.dmg', 'Flash.dmg')


def AIR():
    download1('http://airdownload.adobe.com/air/mac/download/latest/AdobeAIR.dmg', 'Air.dmg')


def Reader():
    print("This one takes forever. Sorry. (not sorry).")
    print("It also uses an ftp link so no status updates...be patient.")
    urllib.urlretrieve('ftp://ftp.adobe.com/pub/adobe/reader/mac/11.x/11.0.16/misc/AdbeRdrUpd11016.dmg',
                       'Reader.dmg')
    done()

# I CALL THIS THE ZAK-LANTZ-SUCKS PART OF THE SCRIPT BECAUSE HE LIKES TO CD TO THINGS.
# It changes the current working directory to the equivalent of ~/
home = expanduser("~")
desk = expanduser("~/Desktop")
os.chdir(home)


os.system("clear")
print("Downloading installers... \n(The downloads have a timeout parameter. Don't quit the script. It's not frozen)")
print("")
lines()
print("")

print("(1/6) Downloading Mozilla Firefox...")
Firefox()
print("")

print("(2/6) Downloading Shockwave Flash...")
Shockwave()
print("")

print("(3/6) Downloading Java...")
Java()
print("")

print("(4/6) Downloading Silverlight...")
Silver()
print("")

print("(5/6) Downloading Adobe Flash...")
Flash()
print("")

print("(6/6) Downloading Adobe Air...")
AIR()
print("")

print("All installers downloaded.")
time.sleep(2)
lines()
print("")
print("Mounting installers...")
time.sleep(1)
print("")
lines()


def Flash_mnt():
    os.system('hdiutil attach ~/Flash.dmg -nobrowse -quiet')
    print("Flash.dmg mounted.\n")


def Air_mnt():
    os.system('hdiutil attach ~/Air.dmg -nobrowse -quiet')
    print("Air.dmg mounted.\n")


def Shkwv_mnt():
    os.system('hdiutil attach ~/Shockwave.dmg -nobrowse -quiet')
    print("Shockwave.dmg mounted.\n")


def Silver_mnt():
    os.system('hdiutil attach ~/Silverlight.dmg -nobrowse -quiet')
    print("Silverlight.dmg mounted.\n")


def FFX_mnt():
    os.system('hdiutil attach ~/Firefox.dmg -nobrowse -quiet')
    print("Firefox.dmg mounted.\n")


def Java_mnt():
    os.system('hdiutil attach ~/Java.dmg -nobrowse -quiet')
    print("Java.dmg mounted.\n")


def Rdr_mnt():
    os.system('hdiutil attach ~/Reader.dmg -nobrowse -quiet')
    print("Reader.dmg mounted.\n")



# Unmounting things

def Flash_unmnt():
    os.system('hdiutil detach /Volumes/Flash\ Player/ -quiet')


def Air_unmnt():
    os.system('hdiutil detach /Volumes/Adobe\ Air/ -quiet')


def Shkwv_unmnt():
    os.system('hdiutil detach /Volumes/Adobe\ Shockwave\ 12/ -quiet')


def Silver_unmnt():
    os.system('hdiutil detach /Volumes/Silverlight/ -quiet')


def FFX_unmnt():
    os.system('hdiutil detach /Volumes/Firefox/ -quiet')


def Java_unmnt():
    os.system('hdiutil detach /Volumes/Java\ 8\ Update\ 65/ -quiet')


def Rdr_unmnt():
    os.system('hdiutil detach /Volumes/AdbeRdr11010_en_US/ -quiet')


Flash_mnt()
Air_mnt()
Shkwv_mnt()
Silver_mnt()
FFX_mnt()
Java_mnt()
lines()
print("")
print("All installers mounted.")
print("")
lines()
time.sleep(2)

clear()

# Installation of DMGs that have .pkg's


# Shockwave Flash
# SHKWV = str(subprocess.check_output('find /Volumes -type d -name "Adobe Shockwave 12" -maxdepth 1', shell=True))[:-1]
# shkwvstring = '%s/Shockwave_Installer_Full.pkg' % (SHKWV)
shkwvinstall = 'echo %s | sudo -S installer -pkg /Volumes/Adobe\ Shockwave\ 12/Shockwave_Installer_Full.pkg -target /' % (
sudoPass)

# screw you, Oracle, for recently making Java more difficult to install
# copies the pkg to Desktop :(
os.system('cp -r /Volumes/Java\ 8\ Update\ 65/Java\ 8\ Update\ 65.app/Contents/Resources/JavaAppletPlugin.pkg ~/Desktop')
javastring = '~/Desktop/JavaAppletPlugin.pkg'
javainstall = 'echo %s | sudo -S installer -pkg %s -target /' % (sudoPass, javastring)

# Silverlight
SILVER = str(subprocess.check_output('find /Volumes -type d -name "Silverlight*" -maxdepth 1', shell=True))[:-1]
silverstring = '%s/Silverlight.pkg' % (SILVER)
silverinstall = 'echo %s | sudo -S installer -pkg %s -target /' % (sudoPass, silverstring)

PKGS = {javainstall, silverinstall, shkwvinstall}


# Other installations
# Firefox is so easy. Shout out to Mozilla. You da real MVP.

def Firefox():
	ffxinstall = 'echo %s | sudo -S cp -R /Volumes/Firefox/Firefox.app /Applications' % (sudoPass)
	os.system(ffxinstall)
	print("Firefox installed.")
	print("")


# The Flash installer is different. I copy the .app to the Desktop to install it silently. Otherwise it has a popup.
# During the course of this, I change the directory to the Desktop, then back to ~/
def Flash():
    print("Installing Flash...")
    os.system('cp -r /Volumes/Flash\ Player/Install\ Adobe\ Flash\ Player.app/* ~/Desktop/')
    os.chdir(desk)
    print("Don't you touch that bouncing folder!")  # Nothing happens if they touch the bouncing folder
    os.system("echo %s | sudo -S ./Contents/MacOS/Adobe\ Flash\ Player\ Install\ Manager -install" % sudoPass)
    os.chdir(home)
    clear()
    print("Flash installed.")
    os.system('rm -rf ~/Desktop/Contents')


def Air():
    print("Installing Adobe Air...")
    os.system('cp -r /Volumes/Adobe\ AIR/Adobe\ AIR\ Installer.app/* ~/Desktop/')
    os.chdir(desk)
    os.system("echo %s | sudo -S ./Contents/MacOS/Adobe\ Air\ Installer -silent -eulaAccepted" % sudoPass)
    os.chdir(home)
    clear()
    print("Air installed.")
    os.system('rm -rf ~/Desktop/Contents')

for item in PKGS:
    os.system(item)
    clear()

print("Installing Firefox...")
Firefox()
Flash()
Air()
clear()

# additional Reader prompt
def dontsayyes():
    print("Everything was installed except for Adobe Reader.\nApple includes 'Preview' as the default PDF viewer.")
    print("")
    rdrsucks = raw_input("Would you like to install Reader anyway? (Defaults to no) [y/N] ")
    if rdrsucks.lower() == 'y':
        print("Downloading Adobe Reader...\n")
        Reader()
        print("Download complete. Installing...\n")
        Rdr_mnt()
        RDR = str(subprocess.check_output('find /Volumes -type d -name "AdbeRdr*" -maxdepth 1', shell=True))[:-1]
        rdrstring = '%s/Adobe\ Reader\ XI\ Installer.pkg' % (RDR)
        rdrinstall = 'echo %s | sudo -S installer -pkg %s -target /' % (sudoPass, rdrstring)
        os.system(rdrinstall)
        print("Reader installed.\n")
        Rdr_unmnt()
        os.system('rm ~/Reader.dmg')
        print("Reader unmounted & deleted.")
        clear()

dontsayyes()
clear()

print("Unmounting things...")
time.sleep(2)

Flash_unmnt()
Air_unmnt()
Shkwv_unmnt()
Silver_unmnt()
FFX_unmnt()
Java_unmnt()
os.system('clear')
print("All installers unmounted.")
time.sleep(1)

print("Deleting the DMG's that were downloaded...")
os.system('rm ~/Flash.dmg')
os.system('rm ~/Air.dmg')
os.system('rm ~/Shockwave.dmg')
os.system('rm ~/Silverlight.dmg')
os.system('rm ~/Firefox.dmg')
os.system('rm ~/Java.dmg')
os.system('rm ~/Desktop/JavaAppletPlugin.pkg')
time.sleep(5)
print("Done.")

os.system('clear')
print("Script is complete.\nPlease report any bugs to Will Hegedus.")
