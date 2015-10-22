__author__ = 'wbhegedus'
import urllib2
import time
import sys
import requests

# url = "http://download.mozilla.org/?product=firefox-latest&os=osx&lang=en-US"




def progressPls():

#Attempt 3 uses ANSI escape sequences and sucks.
   # for i in range(3):
    #    print("Loading" + "." * i)
    #    sys.stdout.write("\033[F") # Cursor up one line
    #    time.sleep(0.5)

# Attempt 2 = failure
# JK I modified it myself and MADE IT WORK PRAISE THE LAWD
    for x in range (0,3):
        b = "Loading." + "." * x
    #    end = '\r' * x
    #    bend = end + b + end
        sys.stdout.write('\r' + b)
    #    if x == 3:
    #        print('\r' + b)
        time.sleep(1)

#Attempt 1 = failure
   #  print 'Loading....  ',
   # sys.stdout.flush()

   # i = 0

   # while i <= 10:
   #     if (i%4) == 0:
   #
   #      elif (i%4) == 1:
   #         sys.stdout.write('\b-')
   #     elif (i%4) == 2:
   #         sys.stdout.write('\b\\')
   #     elif (i%4) == 3:
   #         sys.stdout.write('\b|')

   #     sys.stdout.flush()
   #     time.sleep(0.2)
   #     i+=1

   # print '\b\b Complete'

# resp = urllib2.urlopen(url)
# respHtml = resp.read()
# binfile = open(filename, "wb")
# binfile.write(respHtml)
# binfile.close()


def Download(url, filename):
    dl = requests.get(url, stream=True)
    # dl = urllib2.urlopen(url)  # dl is download. This initiates it
#    dlHtml = dl.read()
    with open(filename, 'wb') as fd:
        for chunk in dl.iter_content(chunk_size):
            fd.write(chunk)
#    op = open(filename, 'wb')  # opens file by filename and 'wb' specifies 'write' and 'binary'. Don't know why binary is needed.
#    binfile.write(dlHtml)
#    meta = dl.headers()  # gets info about the url (see the dl item above)
    filesize = int(dl.headers['content-length']) / 1000000  # gets the filesize in bytes -> converts to MB
    print("Downloading: %s (MB:~%s)" % (filename, filesize)) # %s references the variable listed in order

    filesize_dl = 0
    block_sz = 8192  # "The default logical block size is 8192 bytes (8 KB) for UFS file systems"
    while True:
        buffer = str(filesize / block_sz)
#        buffer = dl.read(block_sz) # Read the block size of the download
        progressPls()
#        if not buffer:  # The buffer object will be a slice from the beginning of object (or from the specified offset). The slice will extend to the end of object (or will have a length given by the size argument)."
#            break  # Terminates current loop

#        filesize_dl += len(buffer)  # adds another value with the variable's value and assigns the new value to the variable
#        op.write(buffer)  # writes buffer to open command above
    #    status = r'%10d [ %3.4f%%]' % (filesize_dl, filesize_dl * 100. / filesize) #The r means that the string is to be treated as a raw string, which means all escape codes will be ignored.
    # status = status + chr(61)*(len(status)+1)
    # print status

Download('http://download.mozilla.org/?product=firefox-latest&os=osx&lang=en-US', 'Firefox.dmg')