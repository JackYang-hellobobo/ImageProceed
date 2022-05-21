from itertools import product

from PIL import Image
from itertools import product
# box=Image.open(r'D:\Git_Prj\JackYangPythonPrj\QR\Test.png')
origin=Image.open(r'D:\Git_Prj\JackYangPythonPrj\QR\origin_xc.jpg')
(rwidth,dhight)=origin.size;
# print(rwidth)
# print(dhight)
# origin.show()
# print(origin)
box=(rwidth-600,dhight-100,rwidth,dhight-20)
region=origin.crop(box)
(regionWidth,regionHigth)=region.size
for pos in  product(range(regionWidth),range(regionHigth)):
    if sum(region.getpixel(pos)[:3]) > 500:
            region.putpixel(pos,(255,255,255))
region.save("cutAndRemoved.png")
boxpaste=Image.open(r'D:\Git_Prj\JackYangPythonPrj\QR\cutAndRemoved.png')
(bpwidth,bphigth)=boxpaste.size
# print(boxpaste.size)
origin.paste(boxpaste,box)
origin.show()


# region.show()
# print(region)



# zuobiao=(0,0,384,90)#裁剪过后的坐标 图片全坐标
# zuob2=(1220,781,1604,871)
# region=box.crop(zuobiao)
# # region.show()
# origin.paste(region,zuob2)
# origin.save("Result.png")
# origin.show()
#
# # origin.show()
