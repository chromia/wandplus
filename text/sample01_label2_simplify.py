#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.textutil import calcSuitableImagesize

# http://www.imagemagick.org/Usage/text/
# original imagemagick command:
# convert -background lightblue -fill blue \
#           -font Candice -pointsize 72 label:Anthony \
#           label.gif

with Drawing() as draw:
    text = 'Anthony'
    draw.font = 'Candice'
    draw.font_size = 72
    (w, h) = calcSuitableImagesize(draw, text)
    with Image(width=w, height=h, background=Color('lightblue')) as img:
        draw.gravity = 'north_west'
        draw.fill_color = Color('blue')
        draw.text(0, 0, text)
        draw(img)
        img.save(filename='sample01b.png')
