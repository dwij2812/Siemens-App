from PIL import Image , ImageOps , ImageFilter
from resize import Resize
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
print (pytesseract.image_to_string(Image.open('pic.jpg')))
image = Image.open('pic.jpg')
inverted_image = ImageOps.invert(image)
inverted_image.save('pic_bw.png')
print (pytesseract.image_to_string(Image.open('pic_bw.PNG')))
im=Image.open('pic.jpg')
im=im.filter(ImageFilter.SHARPEN)
im.save('pic_sharpen.jpg')
print('Picture with Sharpening Filter')
print (pytesseract.image_to_string(Image.open('pic_sharpen.jpg')))
im=Image.open('pic_bw.png')
im=im.filter(ImageFilter.SHARPEN)
im.save('pic_sharpen_bw.jpg')
print('Picture with Sharpening and Black and white filter')
print (pytesseract.image_to_string(Image.open('pic_sharpen_bw.jpg')))
