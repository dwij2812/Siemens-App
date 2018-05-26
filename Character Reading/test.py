from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
print (pytesseract.image_to_string(Image.open('pic.jpg')))
