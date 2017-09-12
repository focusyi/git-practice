#!/usr/bin/env python
#coding:utf-8

from PIL import Image,ImageDraw,ImageFont

# im = Image.open('image.jpg')
# im.rotate(45).show()

def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('backslash.ttf',size=30)
    color = '#ff0000'
    width,height = img.size
    draw.text((width-20,0),'6',font=myfont,fill=color)
    # img.show()
    img.save('result.jpg','jpeg')
    return 0

if __name__=='__main__':
    img=Image.open('image.jpg')
    add_num(img)