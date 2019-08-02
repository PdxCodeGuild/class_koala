# filename: image_manipulation2.py
from PIL import Image
import colorsys

img = Image.open("lena.png") # opens image and stores as "img"
width, height = img.size # stores width and height accordingly
pixels = img.load() # stores pixel data in "pixels"

# cycles through each pixel, unpacks into rgb, converts into hsv and manipulates hsv, then converts back into rgb and repacks
for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        h, s, v = (h + 0.7), (s + 0.2), (v - 0.2)
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        r, g, b = int(r*255), int(g*255), int(b*255)
        pixels[i, j] = (r, g, b)

img.show() # displays the image
