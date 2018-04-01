#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
# convert -size 320x100 xc:lightblue -font Candice -pointsize 72 \
#         -fill gray -annotate +29+69 'Anthony' \
#                    -annotate +28+68 'Anthony' \
#                    -annotate +27+67 'Anthony' \
#                    -annotate +26+66 'Anthony' \
#                    -annotate +25+65 'Anthony' \
#                    -annotate +24+64 'Anthony' \
#         -fill navy -annotate +23+63 'Anthony' \
#         font_extrude.jpg


def extrude(draw, text, x, y, forecolor, shadowcolor):
    draw.fill_color = shadowcolor
    draw.text(x+6, y+6, text)
    draw.text(x+5, y+5, text)
    draw.text(x+4, y+4, text)
    draw.text(x+3, y+3, text)
    draw.text(x+2, y+2, text)
    draw.text(x+1, y+1, text)
    draw.fill_color = forecolor
    draw.text(x, y, text)


w = 320
h = 100
with Image(width=w, height=h, background=Color('lightblue')) as img:
    with Drawing() as draw:
        text = 'Anthony'
        draw.font = 'Candice'
        draw.font_size = 72
        draw.gravity = 'forget'
        extrude(draw, text, 23, 63, Color('navy'), Color('gray'))
        draw(img)
        img.save(filename='sample08.png')
