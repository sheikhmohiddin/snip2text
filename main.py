import pytesseract
from PIL import ImageGrab

# tesseract path setup
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = ImageGrab.grabclipboard() # store clipboard img to memory
out = pytesseract.image_to_string(img) # convert to text

print(out)