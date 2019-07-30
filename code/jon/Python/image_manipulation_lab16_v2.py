from PIL import Image
import colorsys

img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        

        # colorsys uses colors in the range [0, 1]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        h, s, v = (h + 0.9), (s + 0.2), (v + 0.5)

        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        r, g, b = int(r*255), int(g*255), int(b*255)

        pixels[i, j] = (r, g, b)

img.show()




# # colorsys uses colors in the range [0, 1]
# h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

# # do some math on h, s, v



# # convert back to [0, 255]

# r = int(r*255)
# g = int(g*255)
# b = int(b*255)