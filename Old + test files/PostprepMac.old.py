#!/usr/bin/env python
# ----------------------------------------------
# title: "PostprepMac - Python Edition"
version = "1.0.3"
# Author: Will Hegedus
# OG bash shout out: Lucas Messenger
# Created: 7-29-2015
# Known issues: No loading bar, no Firefox icon sometimes
# Last update: changes the cwd if someone (Zak Lantz) cd's to somewhere else like the Desktop
# Previous update: Fixed sudo permissions issue that was created by the previous update (8/20/2015)
# Old updates: Fixed permissions error when installing requests module on some computers (8/19/2015)
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
    os.system('sudo easy_install requests')
    os.system('clear')
    sys.exit("Rerun the script.")
else:
    import os
    import requests
    import time
    import urllib
    import subprocess
    from os.path import expanduser
    from subprocess import Popen

    def progressPls():

        # Attempt 3 uses ANSI escape sequences and sucks.
        # for i in range(3):
        #    print("Loading" + "." * i)
        #    sys.stdout.write("\033[F") # Cursor up one line
        #    time.sleep(0.5)

        # Attempt 2 = failure
        # JK I modified it myself and MADE IT WORK PRAISE THE LAWD
        for x in range(0, 3):
            b = "Loading." + "." * x
            #    end = '\r' * x
            #    bend = end + b + end
            sys.stdout.write('\r' + b)
            #    if x == 3:
            #        print('\r' + b)
            time.sleep(1)


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
        while curSize != kbsize:
            print(progressPls())

    # def download1(url, filename):
    #     dl = requests.get(url, timeout=15, stream=True)
    #     with open(filename, 'wb') as fd:
    #         for chunk in dl.iter_content(chunk_size=1024):
    #             fd.write(chunk)
    #             fd.flush()
    #         fpath = os.path.realpath(filename)
    #         kbsize = int(dl.headers['content-length'])  # filesize in bytes
    #         filesize = kbsize / 1000000  # gets the filesize in bytes -> converts to MB
    #         curSize = os.path.getsize(fpath)
    #         print('Downloaded: "%s" (~%s MB)' % (filename, filesize))  # %s references the variable listed in order
    #         while curSize != kbsize:
    #             print(progressPls())



def clear():
    os.system("clear")


def lines():
    print("-" * 30)


def done():
    print("Complete.")


def Firefox():
    download2('http://download.mozilla.org/?product=firefox-latest&os=osx&lang=en-US', 'Firefox.dmg')


def Shockwave():
    download2(
        'http://fpdownload.macromedia.com/get/shockwave/default/english/macosx/latest/Shockwave_Installer_Full_64bit.dmg',
        'Shockwave.dmg')


def Java():
    download2('http://javadl.sun.com/webapps/download/AutoDL?BundleId=108140', 'Java.dmg')


def Silver():  # Silverlight is weird
    download2('http://go.microsoft.com/fwlink/?LinkID=229322', 'Silverlight.dmg')


def Flash():
    download2('http://fpdownload.macromedia.com/pub/flashplayer/latest/help/install_flash_player_osx.dmg', 'Flash.dmg')


def AIR():
    download2('http://airdownload.adobe.com/air/mac/download/latest/AdobeAIR.dmg', 'Air.dmg')


def Reader():
    print("This one takes forever. Sorry. (not sorry).")
    urllib.urlretrieve('ftp://ftp.adobe.com/pub/adobe/reader/mac/11.x/11.0.10/en_US/AdbeRdr11010_en_US.dmg',
                       'Reader.dmg')
    done()

# I CALL THIS THE ZAK-LANTZ-SUCKS PART OF THE SCRIPT BECAUSE HE LIKES TO CD TO THINGS.
# It changes the current working directory to the equivalent of ~/
home = expanduser("~")
os.chdir(home)


os.system("clear")
print("Downloading installers... \n(The downloads have a timeout parameter. Don't quit the script. It's not frozen)")
print("")
lines()
print("")

print("(1/6) Downloading Mozilla Firefox...")
Firefox()

print("(2/6) Downloading Shockwave Flash...")
Shockwave()

print("(3/6) Downloading Java...")
Java()

print("(4/6) Downloading Silverlight...")
Silver()

print("(5/6) Downloading Adobe Flash...")
Flash()

print("(6/6) Downloading Adobe Air...")
AIR()

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
    os.system('hdiutil detach /Volumes/Java\ 8\ Update\ 51/ -quiet')


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

# Silverlight
SILVER = str(subprocess.check_output('find /Volumes -type d -name "Silverlight*" -maxdepth 1', shell=True))[:-1]
silverstring = '%s/Silverlight.pkg' % (SILVER)
silverinstall = 'echo %s | sudo -S installer -pkg %s -target /' % (sudoPass, silverstring)

# Java (first line not needed due to complications)
# JAVA = str(subprocess.check_output('find /Volumes -type d -name "Java*" -maxdepth 1', shell=True))[:-1]
javastring = '/Volumes/Java\ 8\ Update\ 51/Java\ 8\ Update\ 51.pkg'
javainstall = 'echo %s | sudo -S installer -pkg %s -target /' % (sudoPass, javastring)

PKGS = {javainstall, silverinstall, shkwvinstall}


# Other installations
# Firefox is so easy. Shout out to Mozilla. You da real MVP.

def Firefox():
	ffxinstall = 'echo %s | sudo -S cp -R /Volumes/Firefox/Firefox.app /Applications' % (sudoPass)
	os.system(ffxinstall)
	print("Firefox installed.")
	print("")


def Flash():
    print("Flash will open a popup installer...")
    os.system(
        '/Volumes/Flash\ Player/Install\ Adobe\ Flash\ Player.app/Contents/MacOS/Adobe\ Flash\ Player\ Install\ Manager')
    print("Flash installed.")
    print("")



def Air():
    print("Adobe Air will open a popup installer...")
    os.system("/Volumes/Adobe\ AIR/Adobe\ AIR\ Installer.app/Contents/MacOS/Adobe\ AIR\ Installer")
    print("Air installed.")
    os.system('clear')


for item in PKGS:
    os.system(item)
    os.system('clear')

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
time.sleep(5)
print("Done.")

os.system('clear')
print("Script is complete.\nPlease report any bugs to Will Hegedus.")
