#思路是半自动化截取所需要处理的区域 然后裁剪处理后覆盖回源文件后输出 以达到简单的图像水印处理
# from PIL import Image
# from itertools import product
# import  os
# def getImageName():#识别文件夹内的图片文件函数
#     fileStringArray = os.listdir(os.getcwd())
#     for img in fileStringArray:
#         if img.endswith(".jpg") or img.endswith(".png") or img.endswith(".bmp") or img.endswith(
#                 ".jpeg") or img.endswith(".gif") or img.endswith(".tif"):
#             return img #返回

# def ImageProcess(img) :#图片处理函数
#     imgPath = os.getcwd() + '/' + img
#     origin=Image.open(imgPath)
#     (rwidth,dhight)=origin.size;
#     box=(rwidth-600,dhight-100,rwidth,dhight-20)#裁剪区域设置 自定义裁剪区域进行图像处理
#     region=origin.crop(box)
#     (regionWidth,regionHigth)=region.size
#     for pos in  product(range(regionWidth),range(regionHigth)):
#         if sum(region.getpixel(pos)[:3]) > 500:
#                 region.putpixel(pos,(255,255,255))
#     region.save("cut.png")
#     cutPath=os.getcwd()+'/'+"cut.png"
#     boxpaste=Image.open(cutPath)
#     origin.paste(boxpaste,box)
#     origin.show()

def Main():#进程主函数
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
Main()#运行主函数