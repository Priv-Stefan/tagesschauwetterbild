# pip install requests

import requests
import re
import ctypes
from ctypes import wintypes
import os
import tempfile

image_url = "https://www.tagesschau.de/multimedia/bilder/wetterbilder-101.html"

r = requests.get(image_url) # create HTTP response object
x = re.findall( r'wetterbild-\d+.jpg',r.text)  
x.sort(reverse=True)

image_url = "https://www.tagesschau.de/multimedia/bilder/" + x[0]
r = requests.get(image_url)

image = os.path.join(tempfile.gettempdir(),"wetterbild.jpg")

with open(image,'wb') as f:
    f.write(r.content)

# source https://stackoverflow.com/questions/40574622/how-do-i-set-the-desktop-background-in-python-windows
SPI_SETDESKWALLPAPER  = 0x0014
SPIF_UPDATEINIFILE    = 0x0001
SPIF_SENDWININICHANGE = 0x0002
user32 = ctypes.WinDLL('user32')
SystemParametersInfo = user32.SystemParametersInfoW
SystemParametersInfo.argtypes = ctypes.c_uint,ctypes.c_uint,ctypes.c_void_p,ctypes.c_uint
SystemParametersInfo.restype = wintypes.BOOL
SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, image, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
