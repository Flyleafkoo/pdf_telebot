from pdf2image import convert_from_path
from PIL import Image
from PIL import ImageDraw
import os
images = convert_from_path('протирочная машина.pdf', poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
for i in range(len(images)):
    images[i].save('page' + str(i) + '.jpg', 'JPEG')

input_img = r'C:\Users\CBMO-U06Adm\pdf_telebot\page0.jpg'
(filepath, filename) = os.path.split(input_img)
img = Image.open(input_img)
img_d = ImageDraw.Draw(img)
x_len, y_len = img.size
x_step = x_len / 15
y_step = y_len / 14
print: x_len
print: y_len
for x in range(0, x_len, int(x_step)):
    img_d.line(((x, 0), (x, y_len)), (250, 175, 300))
for y in range(0, y_len, int(y_step)):
    j = y_len - y - 1
    img_d.line(((0, j), (x_len, j)), (250, 175, 300))
img.save(os.path.join(filepath, "разметка_" + filename))
