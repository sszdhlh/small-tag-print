from base64 import decode
import csv

sku_list=[]
barcode_list=[]
quantity_list = []
with open("goods_list full updated 1412.csv", 'r', encoding='utf-8') as f:
    file=csv.reader(f)
    next(file)
    for line in file:
        sku_list.append(line[0])
        barcode_list.append(line[1])
        quantity_list.append(int(line[2]))

header = ["sku", "barcode"]
with open("kohler.csv", 'w', newline='', encoding='utf-8') as f:
    csv_write = csv.writer(f)
    csv_write.writerow(header)
    for i in range(len(sku_list)):
        for u in range(quantity_list[i]):
            csv_write.writerow([sku_list[i], barcode_list[i]])
    
        
