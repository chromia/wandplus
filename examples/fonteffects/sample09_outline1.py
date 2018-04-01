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


def outline1(draw, text, x, y, outcolor, incolor):
    draw.fill_color = outcolor
    draw.text(x-1, y-1, text)
    draw.text(x+1, y-1, text)
    draw.text(x+1, y+1, text)
    draw.text(x-1, y+1, text)
    draw.fill_color = incolor
    draw.text(x, y, text)


w = 320
h = 100
with Image(width=w, height=h, background=Color('lightblue')) as img:
    with Drawing() as draw:
        text = 'Anthony'
        draw.font = 'Candice'
        draw.font_size = 72
        draw.gravity = 'forget'
        outline1(draw, text, 25, 65, Color('black'), Color('white'))
        draw(img)
        img.save(filename='sample09.png')
