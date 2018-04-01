#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
# convert -size 320x100 xc:lightblue -font Candice -pointsize 72 \
#         -fill black -draw "text 28,68 'Anthony'" \
#         -fill white -draw "text 25,65 'Anthony'" \
#         font_shadow.jpg


w = 320
h = 100
with Image(width=w, height=h, background=Color('lightblue')) as img:
    with Drawing() as draw:
        text = 'Anthony'
        draw.font = 'Candice'
        draw.font_size = 72
        draw.gravity = 'center'
        draw.fill_color = Color('black')
        draw.text(+3, +3, text)
        draw.fill_color = Color('white')
        draw.text(0, 0, text)
        draw(img)
        img.save(filename='sample04.png')

        # NOTE: text() function does not accept minus value
        # To control delicately, switch off draw.gravity
        # and use absolute coordinate
        # draw.gravity = 'forget'
        # draw.fill_color = Color('black')
        # draw.text(28, 68, text)
        # draw.fill_color = Color('white')
        # draw.text(25, 65, text)
