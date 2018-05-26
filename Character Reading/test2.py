from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
path = 'pic.JPG'
img = Image.open(path)
img = img.convert('RGBA')
pix = img.load()
for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pix[x, y][0] < 102 or pix[x, y][1] < 102 or pix[x, y][2] < 102:
            pix[x, y] = (0, 0, 0, 255)
        else:
            pix[x, y] = (255, 255, 255, 255)
img.save('temp.PNG')
text = pytesseract.image_to_string(Image.open('temp.PNG'))
# os.remove('temp.jpg')
print(text)
