import os
import time
from tkinter import *
import threading
from PIL import Image,ImageTk

#分辨率
resolution = (1024,550)
#时间间隔
interval = 1
#照片索引
index = 0
path = "D:/photo"

#创建窗口对象背景色
root = Tk()
root.title("SSE4相册（淡入淡出）")

#首页开始图片的处理
im_begin = Image.open("1.jpg")
# w,h = im_begin.size
# size_new = ((int)(w*resolution[1]/h),resolution[1])
im_after1 = im_begin.resize(resolution)
img = ImageTk.PhotoImage(im_after1)
panel = Label(root,image=img)
panel.pack(side="top",fill="both",expand = "yes")
img_last = im_after1

#淡入淡出效果
def merge(img1,img2,fade):
    # width = min(img1.size[0],img2.size[0])
    # height = min(img1.size[1],img2.size[1])
    # img_new = Image.new('RGB',(width,height))
    # for x in range(width):
    #     for y in range(height):
    #         r1,g1,b1 = img1.getpixel((x,y))
    #         r2,g2,b2 = img2.getpixel((x,y))
    #         r = (int)((r1-r2)*fade)+r2
    #         g = (int)((g1-g2)*fade)+g2
    #         b = (int)((b1-b2)*fade)+b2
    #         img_new.putpixel((x,y),(r,g,b))
    img_new = Image.blend(img1,img2,fade)
    return img_new




#正式加载图片
def changeImage():
    global index
    global img_last
    files = os.listdir(path)
    while True:
        for x in files:
            #判断文件是否存在
            print(x,index)
            if not os.path.isfile(path+"\{}".format(x)):
                break;
            if not ((x.endswith(".jpg")) or x.endswith(".JPG")):
                continue
            print("自动处理图片")
            img_begin = Image.open(path+"\{}".format(x))
            # w,h = img_begin.size
            # size_new = ((int)(w * resolution[1] / h), resolution[1])
            im_after = img_begin.resize(resolution)

            #淡入淡出
            fade = 0
            while fade<=1:
                fade = fade+0.01
                img_temp=merge(img_last,im_after,fade)
                img = ImageTk.PhotoImage(img_temp)
                panel.configure(image=img)
                panel.image = img

            #定格展示新图片
            # img = ImageTk.PhotoImage(im_after)
            # panel.configure(image = img)
            # panel.image = img
            index = index+1
            if index>=len(files):
                index=0
            img_last = im_after

def auto_begin():
    t= threading.Thread(target=changeImage)
    t.start()


button1 = Button(text = "自动播放",command = auto_begin)
button2 = Button(text = "退出",command = quit)
button1.pack(fill = 'x')
button2.pack(fill = 'x')
root.mainloop()
