"""
I should probably turn this into a proper function etc. I won't.
"""
from PIL import Image


image = Image.open("sprechen\sprechen_teil_2.jpeg")



pdf_path = "sprechen\sprechen_teil_2.pdf"
image.save(pdf_path, "PDF", resolution=100.0)
print("Saved PDF!")
