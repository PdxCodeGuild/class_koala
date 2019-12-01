from PIL import Image, ImageDraw
import colorsys
from random import randint




width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)




draw.rectangle(((0, 0), (width, height)), fill="white")


draw.polygon(((200, 200), (300, 400)), fill="lightblue")
draw.polygon(((100, 200), (400, 250)), fill="lightblue")
draw.polygon(((200, 400), (225, 500)), fill="lightblue")
draw.polygon(((275, 400), (300, 500)), fill="lightblue")


color = (256, 128, 128)  
draw.line((0, 0, width, height), fill=color)
draw.line((0, height, width, 0), fill=color)


circle_x = width/2 
circle_y = height/2 - 100
circle_radius = 50
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')

img.show()