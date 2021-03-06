#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.textutil import calcSuitableFontsize, calcSuitableImagesize

# http://www.imagemagick.org/Usage/text/
# original imagemagick command:
# convert -background lightblue -fill blue -font Candice \
#           -size 160x  label:Anthony     label_size_width.gif

w = 160
# h =
with Drawing() as draw:
    text = 'Anthony'
    draw.font = 'Candice'
    draw.font_size = calcSuitableFontsize(draw, text, width=w, height=None)
    (w2, h) = calcSuitableImagesize(draw, text)
    with Image(width=w, height=h, background=Color('lightblue')) as img:
        draw.gravity = 'north_west'
        draw.fill_color = Color('blue')
        draw.text(0, 0, text)
        draw(img)
        img.save(filename='sample06.png')
