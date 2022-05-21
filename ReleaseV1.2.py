from PIL import Image
from itertools import product
import  os
def getImageName():
    fileStringArray = os.listdir(os.getcwd())
    for img in fileStringArray:
        if img.endswith(".jpg") or img.endswith(".png") or img.endswith(".bmp") or img.endswith(
                ".jpeg") or img.endswith(".gif") or img.endswith(".tif"):
            return img
def ImageProcess(img) :
    imgPath = os.getcwd() + '/' + img
    origin=Image.open(imgPath)
    (rwidth,dhight)=origin.size;
    box=(rwidth-600,dhight-100,rwidth,dhight-20)
    region=origin.crop(box)
    (regionWidth,regionHigth)=region.size
    for pos in  product(range(regionWidth),range(regionHigth)):
        if sum(region.getpixel(pos)[:3]) > 500:
                region.putpixel(pos,(255,255,255))
    region.save("cut.png")
    cutPath=os.getcwd()+'/'+"cut.png"
    boxpaste=Image.open(cutPath)
    origin.paste(boxpaste,box)
    origin.show()
def Main():
    fileStringArray = os.listdir(os.getcwd())
    os.makedirs('ImageProcessed', exist_ok=True)
    path_save=os.getcwd()+'/'+"ImageProcessed"
    for img in fileStringArray:
        if img.endswith(".jpg") or img.endswith(".png") or img.endswith(".bmp") or img.endswith(
                ".jpeg") or img.endswith(".gif") or img.endswith(".tif"):
            imgPath = os.getcwd() + '/' + img
            origin = Image.open(imgPath)
            (rwidth, dhight) = origin.size;
            box = (rwidth - 600, dhight - 200, rwidth, dhight )
            region = origin.crop(box)
            (regionWidth, regionHigth) = region.size
            for pos in product(range(regionWidth), range(regionHigth)):
                if sum(region.getpixel(pos)[:3]) > 500:
                    region.putpixel(pos, (255, 255, 255))
            origin.paste(region, box)
            origin.save(os.path.join(path_save,os.path.basename(img)))
            # origin.show()
Main()