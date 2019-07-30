# filename: image_manipulation.py
from PIL import Image

img = Image.open("lena.png") # opens image and stores as "img"
width, height = img.size # stores width and height accordingly
pixels = img.load() # stores pixel data in "pixels"

# cycles through each pixel, unpacking into rgb, converting into greyscale accordingly and then repacking
for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        y = 0.299*r + 0.587*g + 0.114*b # greyscale formula
        r, g, b = int(y), int(y), int(y)
        pixels[i, j] = (r, g, b)

img.show() # displays the image
