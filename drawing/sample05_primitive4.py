#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/
# original imagemagick command:
# text drawing  / image
# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -font Candice -pointsize 40 -gravity center \
#         -draw "text 0,0 'Hello'"   draw_text.gif
#
# convert -size 100x60 xc:skyblue -gravity center \
#         -draw "image over 0,0 0,0 'terminal.gif'"   draw_image.gif


def makedrawing():
    draw = Drawing()
    draw.fill_color = Color('white')
    draw.stroke_color = Color('black')
    draw.stroke_width = 1
    draw.gravity = 'center'
    return draw


w = 100
h = 60
bgcolor = Color('skyblue')

with Image(width=w, height=h, background=bgcolor) as img:
    with makedrawing() as draw:
        draw.font = 'Candice'
        draw.font_size = 40
        draw.text(0, 0, 'Hello')
        draw(img)
        img.save(filename='sample05a.png')

with Image(width=w, height=h, background=bgcolor) as img:
    with Image(filename='rose:') as rose:  # substitute for 'terminal.gif'
        with makedrawing() as draw:
            draw.composite('over', 0, 0, 0, 0, rose)
            draw(img)
            img.save(filename='sample05b.png')
