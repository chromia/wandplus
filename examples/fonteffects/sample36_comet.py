#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.image import motionblur

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
#  convert -size 340x120 xc:lightblue  -font Candice  -pointsize 72 \
#          -fill navy   -annotate +45+95 'Anthony' -motion-blur 0x25+65 \
#          -fill black  -annotate +45+95 'Anthony' -motion-blur 0x1+65 \
#          font_comet.jpg


w = 340
h = 120
bgcolor = Color('lightblue')
with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        text = 'Anthony'
        draw.font = 'Candice'
        draw.font_size = 72
        draw.gravity = 'forget'
        x = 45
        y = 95
        draw.fill_color = Color('navy')
        draw.text(x, y, text)
        draw(img)
        motionblur(img, 0, 25, 65)
        draw.fill_color = Color('black')
        draw.text(x, y, text)
        draw(img)
        motionblur(img, 0, 1, 65)
        img.save(filename='sample36.png')
