from PIL import Image , ImageOps , ImageFilter , ImageEnhance
from resize import Resize
import pytesseract
from resize import Resize
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
import csv
############################################################
#Image Resizing Section
print('Reszing Image Please Wait........')
Resize().rsize(Image.open('pic.jpg')).save('pic1.jpg')
image = Image.open('pic1.jpg').convert("L")
for i in range(5):
    image=image.filter(ImageFilter.SMOOTH_MORE)
############################################################
"""print (pytesseract.image_to_string(Image.open('pic.jpg')))
inverted_image = ImageOps.invert(image)
inverted_image.save('pic_bw.png')
print (pytesseract.image_to_string(Image.open('pic_bw.PNG')))
############################################################
im=Image.open('pic1.jpg')
im=im.filter(ImageFilter.SHARPEN)
im.save('pic_sharpen.jpg')
print('Picture with Sharpening Filter')
print (pytesseract.image_to_string(Image.open('pic_sharpen.jpg')))
############################################################
im=Image.open('pic_bw.png')
im=im.filter(ImageFilter.SHARPEN)
im.save('pic_sharpen_bw.jpg')
print('Picture with Sharpening and Black and white filter')
print (pytesseract.image_to_string(Image.open('pic_sharpen_bw.jpg')))"""
##############################################################
print("\n====================OUTPUT====================\n")
contrast=ImageEnhance.Contrast(image)
for i in range(10):
    contrast.enhance(4).save('pic_contrast.png')
print('Stage 1:')
try:
    s1=pytesseract.image_to_string(Image.open('pic_contrast.PNG'))
except UnicodeError:
    print('The Input text consists a character which is not supported by the current CODEC installed please upload a better Image')
print ('<',s1,'>')
##############################################################
color=ImageEnhance.Color(Image.open('pic_contrast.png'))
color.enhance(0).save('pic_color_bw.png')
print('Stage 2:')
try:
    s2=pytesseract.image_to_string(Image.open('pic_color_bw.PNG'))
except UnicodeError:
    print('The Input text consists a character which is not supported by the current CODEC installed please upload a better Image')
print ('<',s2,'>')
##############################################################
sharpen=ImageEnhance.Sharpness(Image.open('pic_color_bw.png'))
sharpen.enhance(2).save('pic_sharpen_enhance.png')
print('Stage 3:')
try:
    s3=pytesseract.image_to_string(Image.open('pic_sharpen_enhance.PNG'))
except UnicodeError:
    print('The Input text consists a character which is not supported by the current CODEC installed please upload a better Image')
print ('<',s3,'>')
##############################################################
inverted_image = ImageOps.invert(Image.open('pic_sharpen_enhance.png'))
for i in range(10):
    ImageEnhance.Sharpness(inverted_image).enhance(2).save('pic_sharpen_enhance_sharpen.png')
    k=Image.open('pic.jpg')
    k=ImageOps.grayscale(k)
    k=ImageOps.invert(k)
    k=ImageEnhance.Contrast(k).enhance(3)
    k.save('pic_sharpen_enhance_sharpen.png')
    ImageEnhance.Sharpness(inverted_image).enhance(2).save('pic_sharpen_enhance_sharpen.png')
print('Stage 4:')
try:
    s4=pytesseract.image_to_string(Image.open('pic_sharpen_enhance_sharpen.png'))
except UnicodeError:
    print('The Input text consists a character which is not supported by the current CODEC installed please upload a better Image')
print('<',s4,'>')
##############################################################
def output(k):
    print('Saving the Result as .csv....................')
    res = []
    res.append(k)
    csvfile = "output.csv"
    print('Writing to the File Output.csv the following Result:')
    print(res)

    #Assuming res is a flat list
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for val in res:
            writer.writerow([val])
    print("EXIT, YOUR FILE IS READY please check the output.csv in the current directory")
##############################################################
print('\n====================Final Result====================\n')
if(s1==s2):
    if s1:
        print(s1)
        output(s1)
        exit()
if(s2==s3):
    if s2:
        print(s2)
        output(s2)
        exit()
if(s3==s4):
    if s3:
        print(s3)
        output(s3)
        exit()
if s4:
    print(s4)
    output(s4)
    exit()
if not s4:
    print('Please Upload a better Image')
