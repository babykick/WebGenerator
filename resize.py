import os
import Image
import sys

EXCLUDE = ("header.jpg",)
FORMAT = (".JPG",".jpg",".gif", ".GIF", "_thn.jpg","_thn.JPG")


if len(sys.argv) < 2:
    print "Usage:"
    print "python resize.py imagedir newwidth [prefix]"
    exit()

imageDIR = sys.argv[1]
newWidth = int(sys.argv[2])
if len(sys.argv) == 3:
    prefix = sys.argv[3]
else:
    prefix = ""

for f in os.listdir(imageDIR):
    if f.endswith(FORMAT) and f not in EXCLUDE and prefix in f:
        print "process %s..." % f
        im = Image.open(os.path.join(imageDIR, f))
        imgName = f.split(".")[0]
        originWidth = im.size[0]
        originHeight = im.size[1]
        if not newWidth == originWidth:
            scale = 1.0 * newWidth / originWidth
            newSize = (newWidth, int(originHeight * scale))
            newImg = im.resize(newSize, Image.ANTIALIAS)
            newImg.save(os.path.join(imageDIR, imgName + '_thn.jpg'), "JPEG")

raw_input("Images has converted to new size(suffix with _thn)")
