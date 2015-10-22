To run the new PostprepMac:

-You do NOT have to sudo chmod +x the file.
-Do NOT cd to the Desktop (this messes up the downloads)
-Follow these steps:
	1) Copy PostprepMac.py to desktop
	2) Open terminal
	3) Type "python" + space + *drag file from desktop into terminal window*

-If you have any questions or discover bugs, feel free to contact Will Hegedus (wbhegedus)

As opposed to previous versions of PostprepMac, this script is made in Python instead of Bash. It runs faster and is easier to maintain.

Known bugs:
- Java download occassionally times out because Oracle's CDN is weird. Not the script's fault.
- Firefox icon occassionally doesn't show in the Launchpad grid.
- If Unibak was used to restore data from the server, the script fails because of how Unibak mounts luna04 and luna05 to the computer
(as /Volumes/hdbackups and /Volumes/hdstorage). RESTART the computer to fix this.

Not quite sure why Unibak breaks the script? Screenshots of issues would be appreciated to fix this in the future.