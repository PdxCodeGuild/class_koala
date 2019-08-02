# filename: image_manipulation3.py
from PIL import Image, ImageDraw

# sets image size
width = 500
height = 500

# creates a new image in RGB mode with inputted width and height
img = Image.new('RGB', (width, height))

# creates an object that can be used to draw in the given image
draw = ImageDraw.Draw(img)

# draws a rectangle around the full boundary and fills the background as "white"
draw.rectangle(((0, 0), (width, height)), fill="white")

# draws the body - for reference: x0, y0, x1, y1
body_color = (0, 0, 0)  # black
draw.line(((width * .5), (height * .43), (width * .5), height * .70), fill=body_color) # body / torso
draw.line(((width * .5), (height * .57), (width * .35), height * .45), fill=body_color) # left arm
draw.line(((width * .5), (height * .57), (width * .65), height * .45), fill=body_color) # right arm
draw.line(((width * .5), (height * .70), (width * .35), height * .85), fill=body_color) # left leg
draw.line(((width * .5), (height * .70), (width * .65), height * .85), fill=body_color) # right leg

# draws the head
circle_x = width * .5
circle_y = height * .33
circle_radius = 50
draw.ellipse((circle_x - circle_radius, circle_y - circle_radius, circle_x + circle_radius, circle_y + circle_radius), outline='black')

# draws the hat
draw.line(((width * .405), (height * .3), (width * .69), height * .3), fill=body_color) # right leg

img.show() # displays the completed image
