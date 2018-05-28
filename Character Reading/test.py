from PIL import Image , ImageOps , ImageFilter , ImageEnhance
from resize import Resize
import pytesseract
from resize import Resize
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
############################################################
#Image Resizing Section
Resize().rsize(Image.open('pic.jpg')).save('pic1.jpg')
image = Image.open('pic1.jpg')
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
contrast=ImageEnhance.Contrast(image)
contrast.enhance(2).save('pic_contrast.png')
print('Image with contrast enhancement')
print (pytesseract.image_to_string(Image.open('pic_contrast.PNG')))
##############################################################
color=ImageEnhance.Color(Image.open('pic_contrast.png'))
color.enhance(0).save('pic_color_bw.png')
print (pytesseract.image_to_string(Image.open('pic_color_bw.PNG')))
##############################################################
sharpen=ImageEnhance.Sharpness(Image.open('pic_color_bw.png'))
sharpen.enhance(2).save('pic_sharpen_enhance.png')
print (pytesseract.image_to_string(Image.open('pic_sharpen_enhance.PNG')))
##############################################################
inverted_image = ImageOps.invert(Image.open('pic_sharpen_enhance.png'))
ImageEnhance.Sharpness(inverted_image).enhance(2).save('pic_sharpen_enhance_sharpen.png')
print(pytesseract.image_to_string(Image.open('pic_sharpen_enhance_sharpen.png')))
