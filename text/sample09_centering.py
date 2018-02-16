#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.textutil import calcSuitableImagesize

# http://www.imagemagick.org/Usage/text/
# original imagemagick command:
# convert -background lightblue -fill blue -font Corsiva -pointsize 24 \
#           -gravity center    label:'ImageMagick\nExamples\nby Anthony' \
#           label_centered.gif

with Drawing() as draw:
    text = 'ImageMagick\nExamples\nAnthony'
    draw.font = 'Corsiva'
    draw.font_size = 24
    draw.gravity = 'center'
    (w, h) = calcSuitableImagesize(draw, text, multiline=True)
    with Image(width=w, height=h, background=Color('lightblue')) as img:
        draw.fill_color = Color('blue')
        draw.text(0, 0, text)
        draw(img)
        img.save(filename='sample09.png')
