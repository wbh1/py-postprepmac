# __author__ = 'wbhegedus'
import imp
try:
        imp.find_module("requests") # Checks if requests module is installed
        found = True
except ImportError:
	found = False
if found == False:  # installs requests if not installed
	    import os
	os.system('easy_install requests')
    os.system('clear')
	print("Rerun the script.")
else:
        import os
        import requests
        import sys
        import time

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

        def download(url, filename):
                # NOTE the stream=True parameter
                dl = requests.get(url, stream=True)
                with open(filename, 'wb') as f:
                    for chunk in dl.iter_content(chunk_size=1024):
                        if chunk: # filter out keep-alive new chunks
                            f.write(chunk)
                            f.flush()
                fpath = os.path.realpath(filename)
                kbsize = int(dl.headers['content-length']) #filesize in bytes
                filesize = kbsize / 1000000  # gets the filesize in bytes -> converts to MB
                curSize = os.path.getsize(fpath)
                print("Downloading: %s (MB:~%s)" % (filename, filesize)) # %s references the variable listed in order
                if curSize != kbsize:
                    print(progressPls())
                else:
                    print("Complete")


        download('http://download.mozilla.org/?product=firefox-latest&os=osx&lang=en-US', 'Firefox.dmg')

