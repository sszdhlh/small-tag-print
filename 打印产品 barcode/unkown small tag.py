import csv
from pystrich.code128 import Code128Encoder
from pystrich.ean13 import EAN13Encoder
from PIL import Image,ImageDraw, ImageFont
import cv2

        
if __name__ == '__main__':
    
    printlist=[]
    numberlist=[]
    with open('打印产品 barcode/JD_small_printlist.csv','r',encoding='utf-8') as f:
        file = csv.reader(f)
        next(file)
        for line in file:
            if len(line) > 0 and line[0] != None and line[0] != '':
                printlist.append(line[0])
                numberlist.append(line[1])

   
    for i in range(10):
        
        encoder = Code128Encoder(numberlist[i], options={'ttf_font':'LGSmHaB_0521_HS98','ttf_fontsize':100,'bottom_border':10,'height':300})
        encoder.save('barcodes/'+str(i)+printlist[i]+".png",bar_width=8)
        
        image= Image.open('barcodes/'+str(i)+printlist[i]+".png")
        height = image.height
        width = image.width
        
        sku_image = Image.new('L', (width, 100), 255)
        draw = ImageDraw.Draw(sku_image)
        font = ImageFont.truetype("LGSmHaB_0521_HS98", 100)

        w,h = font.getsize(printlist[i])
        draw.text(((width-w)/2,(70-h)/2), printlist[i], font=font, fill="black")

        # draw.text((0,0), skulist[i], fill="#000", font=font)

        image.paste(sku_image, (0, height-100))
        image.save('barcodes/'+str(i)+printlist[i].strip()+".png", "PNG")
        # image.show()
        # break

        bk_img = cv2.imread('barcodes/'+str(i)+printlist[i].strip()+".png")
        
        if i % 16 == 0:
            newimage=Image.new('RGB', (2479,3508),(255,255,255))
            draw =ImageDraw.Draw(newimage)
        width=45+1239.5*(i%2)
        height=50+int(i%16/2)*430
        imager=Image.open('barcodes/'+str(i)+printlist[i].strip()+".png")
        newimage.paste(imager, box=(int(width), int(height)))
        
        if i % 16 == 15 or i == len(printlist)-1:                       
            newimage.save('printlist/'+printlist[i]+".pdf", "PDF", resolution=100.0, save_all=True)
