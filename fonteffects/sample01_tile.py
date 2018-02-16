#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
# convert -size 320x100 xc:lightblue -font Candice -pointsize 72 \
#         -tile pattern:checkerboard   -annotate +28+68 'Anthony' \
#         font_tile.jpg


def checkpattern(draw, w, h, color1, color2):
    fill_color_backup = draw.fill_color
    draw.fill_color = color1
    draw.rectangle(0, 0, width=w/2, height=h/2)
    draw.rectangle(w/2, h/2, width=w/2, height=h/2)
    draw.fill_color = color2
    draw.rectangle(0, h/2, width=w/2, height=h/2)
    draw.rectangle(w/2, 0, width=w/2, height=h/2)
    draw.fill_color = fill_color_backup


w = 320
h = 100
with Image(width=w, height=h, background=Color('lightblue')) as img:
    with Drawing() as draw:
        # make checkerboard pattern
        draw.push_pattern('checkerboard', 0, 0, 32, 32)
        checkpattern(draw, 32, 32, Color('gray40'), Color('gray60'))
        draw.pop_pattern()

        text = 'Anthony'
        draw.font = 'Candice'
        draw.font_size = 72
        draw.set_fill_pattern_url('#checkerboard')  # fill with defined pattern
        draw.gravity = 'center'
        draw.text(0, 0, text)
        draw(img)
        img.save(filename='sample01.png')
