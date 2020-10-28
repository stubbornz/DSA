import os
from PIL import Image
from PIL.ExifTags import TAGS

exif = {}
# print(TAGS)
img = 'one.png'
image = Image.open(img)
for tag, value in image._getexif().items():
    if tag in TAGS:
        exif[TAGS[tag]] = value

print(exif)
