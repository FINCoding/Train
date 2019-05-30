from urllib.request import urlopen
import sys
import os
#picture = urlopen("https://download.microsoft.com/download/2/4/3/24375141-E08D-4803-AB0E-10F2E3A07AAA/AccessDatabaseEngine.exe")
picture = urlopen("https://ftp.nluug.nl/pub/vim/pc/gvim81.exe")
lsize = int(picture.info()['Content-Length'])
lsize2 = 0
#f = open("access.zip", "wb")
f = open("VIM.zip", "wb")
n = 4096
while lsize > lsize2:
    if lsize - lsize2 < 4096:
        n = lsize - lsize2
    f.write(picture.read(n))
    lsize2 += n
    print(lsize2, " from ", lsize)
    # sys.stdout.write("#")
f.close()
