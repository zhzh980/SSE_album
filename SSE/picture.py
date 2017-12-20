import os
import threading
from tkinter import *
import time
from PIL import ImageTk, Image
#ImageTk模块用于创建和修改BitmapImage和PhotoImage对象中的Tkinter
# 分辨率
resolution = (1024, 512)
# 路径
Path = 'd:\photo'
# 播放间隔.单位:s
Interval = 3
# 当前照片计数
Index = 0

scaler = Image.ANTIALIAS

# 创建窗口对象的背景色
root = Tk()

#------呈现图片-------
img_in = Image.open("Blur.jpg")
w, h = img_in.size
size_new = ((int)(w * resolution[1] / h), resolution[1])
img_out = img_in.resize(size_new)
img = ImageTk.PhotoImage(img_out)
# img = ImageTk.PhotoImage(Image.open("load.jpg"))
panel = Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")


# def callback():
#     global Index
#
#     files = os.listdir(Path)
#     i = 0
#     for x in files:
#         # 判断文件是否存在
#         if not os.path.isfile(Path + '\{}'.format(x)):
#             break
#
#         if i < Index:
#             i += 1
#             continue
#
#         print('手动处理图片', x, Index)
#         if not (x.endswith('.jpg') or x.endswith('.JPG')):
#             i += 1
#             Index += 1
#             if Index >= len(files):
#                 Index = 0
#             continue
#
#         img_in = Image.open(Path + '\%s' % x)
#         print(img_in)
#         w, h = img_in.size
#         size_new = ((int)(w * resolution[1] / h), resolution[1])
#         img_out = img_in.resize(size_new, scaler)
#         img2 = ImageTk.PhotoImage(img_out)
#         # img2 = ImageTk.PhotoImage(Image.open(Path + '\%s' % x))
#         panel.configure(image=img2)
#         panel.image = img2
#         Index += 1
#         if Index >= len(files):
#             Index = 0
#         break
#
#         # root.bind("<Return>", callback)
#
#
# root.bind("<Button-1>", callback)


def image_change():
    global Index

    time.sleep(3)
    while True:
        files = os.listdir(Path)
        i = 0
        for x in files:
            # 判断文件是否存在
            if not os.path.isfile(Path + '\%s' % x):
                break

            if i < Index:
                i += 1
                continue

            print('自动处理图片', x, Index)
            if not (x.endswith('.jpg') or x.endswith('.JPG')):
                i += 1
                Index += 1
                if Index >= len(files):
                    Index = 0
                continue

            img_in = Image.open(Path + '\%s' % x)
            w, h = img_in.size
            size_new = ((int)(w * resolution[1] / h), resolution[1])
            img_out = img_in.resize(size_new, scaler)
            img2 = ImageTk.PhotoImage(img_out)
            # img2 = ImageTk.PhotoImage(Image.open(Path + '\%s' % x))
            panel.configure(image=img2)
            panel.image = img2
            Index += 1
            if Index >= len(files):
                Index = 0
            time.sleep(Interval)

            # 图片切换线程


t = threading.Thread(target=image_change)
t.start()

root.mainloop()