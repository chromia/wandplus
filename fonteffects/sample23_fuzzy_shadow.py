#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.image import blur

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
# convert -size 320x100 xc:lightblue -font Candice -pointsize 72 \
#         -annotate +30+70 'Anthony'   -blur 0x4 \
#         -fill white  -stroke black  -annotate +25+65 'Anthony' \
#         font_shadow_fuzzy.jpg


w = 320
h = 100
with Image(width=w, height=h, background=Color('lightblue')) as img:
    with Drawing() as draw0:
        text = 'Anthony'
        draw0.font = 'Candice'
        draw0.font_size = 72
        draw0.gravity = 'forget'

        with draw0.clone() as draw:
            draw.fill_color = Color('black')
            draw.text(30, 70, text)
            draw(img)
        blur(img, 0, 4)

        with draw0.clone() as draw:
            draw.fill_color = Color('white')
            draw.stroke_color = Color('black')
            draw.text(25, 65, text)
            draw(img)

        img.save(filename='sample23.png')
