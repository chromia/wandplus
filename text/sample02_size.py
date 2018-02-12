from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/text/
# original imagemagick command:
# convert -background lightblue -fill blue  -font Candice \
#           -size 165x70 -pointsize 24 label:Anthony     label_size.gif

w = 165
h = 70
with Image(width=w, height=h, background=Color('lightblue')) as img:
    with Drawing() as draw:
        text = 'Anthony'
        draw.font = 'Candice'
        draw.font_size = 24
        draw.gravity = 'north_west'
        draw.fill_color = Color('blue')
        draw.text(0, 0, text)
        draw(img)
        img.save(filename='sample02.png')
