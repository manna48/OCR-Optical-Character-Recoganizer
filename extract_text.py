from PIL import Image
import pytesseract
import pandas as pd

text = pytesseract.image_to_string(Image.open('text.jpg'))
text_file = open("output.txt", "w")
text_file.write(text)
text_file.close()

csv_file = pd.read_fwf('output.txt')
csv_file.to_csv('output.csv')