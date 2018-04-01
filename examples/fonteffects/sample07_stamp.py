#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
# convert -size 320x100 xc:lightblue -font Candice -pointsize 72 \
#         -fill black     -annotate +24+64 'Anthony' \
#         -fill white     -annotate +26+66 'Anthony' \
#         -fill lightblue -annotate +25+65 'Anthony' \
#         font_stamp.jpg


def stamp(draw, text, x, y, color):
    draw.fill_color = Color('black')
    draw.text(x-1, y-1, text)
    draw.fill_color = Color('white')
    draw.text(x+1, y+1, text)
    draw.fill_color = color
    draw.text(x, y, text)


w = 320
h = 100
with Image(width=w, height=h, background=Color('lightblue')) as img:
    with Drawing() as draw:
        text = 'Anthony'
        draw.font = 'Candice'
        draw.font_size = 72
        draw.gravity = 'forget'
        stamp(draw, text, 25, 65, Color('lightblue'))
        draw(img)
        img.save(filename='sample07.png')
