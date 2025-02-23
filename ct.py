from colorthief import ColorThief
from urllib.request import urlopen
import io
import ssl

def get_color_palette(url):
    file = urlopen(url, context=ssl._create_unverified_context())
    img = io.BytesIO(file.read())
    ct = ColorThief(img)
    return ct.get_palette(color_count=5, quality=1)