import pyqrcode
import png
from pyqrcode import QRCode
s = "https://youtu.be/_3wkyerSBpw"
url = pyqrcode.create(s)
url.svg("Rickroll.svg",scale = 8)
url.png("Rickroll.png", scale = 6)
