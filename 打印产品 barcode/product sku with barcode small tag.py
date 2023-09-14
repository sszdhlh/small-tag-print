import csv
from pystrich.code128 import Code128Encoder
from pystrich.ean13 import EAN13Encoder
from PIL import Image,ImageDraw, ImageFont
import cv2
import sys
import os
        
if __name__ == '__main__':
    
    for root, dirs, files in os.walk("barcodes"):
        for name in files:
            os.remove(os.path.join(root, name))
    
    for root, dirs, files in os.walk("printlist"):
        for name in files:
            os.remove(os.path.join(root, name))

    printlist=[]
    numberlist=[]
    with open('unknown.csv','r',encoding='utf-8') as f:
        file = csv.reader(f)
        next(file)
        for line in file:
            if len(line) > 0 and line[0] != None and line[0] != '':
                printlist.append(line[0])
                numberlist.append(line[1])

   
    for i in range(len(printlist)):
        
        encoder = Code128Encoder(numberlist[i], options={'ttf_font':'REFSAN','ttf_fontsize':60,'bottom_border':10,'height':280})
        encoder.save('barcodes/'+str(i)+printlist[i].replace("/", "")+".png",bar_width=8)
        
        image= Image.open('barcodes/'+str(i)+printlist[i].replace("/", "")+".png")
        height = image.height
        width = image.width
        # image = image.crop((0, 0, 0, height-50))
        sku_image = Image.new('L', (width, 100), 255)
        draw = ImageDraw.Draw(sku_image)
        if len(printlist[i]) > 17:
            font = ImageFont.truetype("REFSAN", 50)
        else: 
            font = ImageFont.truetype("REFSAN", 80)

        w,h = font.getsize(printlist[i])
        draw.text(((width-w)/2,(70-h)/2), printlist[i], font=font, fill="black")
        
        back_img = Image.new('L', (width, 400), 255)
        back_img.paste(image, (0, 0))
        back_img.paste(sku_image, (0, height))
        back_img = back_img.resize((1144,340))
        back_img.save('barcodes/'+str(i)+printlist[i].replace("/", "").strip()+".png", "PNG")
        # back_img.show()
        # break
        
        if i % 16 == 0:
            newimage=Image.new('RGB', (2479,3508),(255,255,255))
            draw =ImageDraw.Draw(newimage)
        width=40+1239.5*(i%2)
        height=90+int(i%16/2)*430
        imager=Image.open('barcodes/'+str(i)+printlist[i].replace("/", "").strip()+".png")
        newimage.paste(imager, box=(int(width), int(height)))
        
        if i % 16 == 15 or i == len(printlist)-1:                       
            newimage.save('printlist/'+str(i)+printlist[i].replace("/", "")+".pdf", "PDF", resolution=100.0, save_all=True)
            # newimage.show()