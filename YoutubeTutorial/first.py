import random
import urllib.request

def download_image(url):
    name = random.randrange(1)
    fullname = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fullname)

download_image("https://www.google.com/landing/2step/images/why-need-img-2.png")




