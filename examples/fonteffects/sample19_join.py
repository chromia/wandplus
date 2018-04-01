#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
# convert -size 320x100 xc:lightblue -font Candice -pointsize 72 \
#         -kerning -6  -strokewidth 4 -fill white \
#         -stroke black   -annotate +28+68 Anthony \
#         -stroke none    -annotate +28+68 Anthony \
#         font_joined.jpg


w = 320
h = 100
with Image(width=w, height=h, background=Color('lightblue')) as img:
    with Drawing() as draw:
        text = 'Anthony'
        draw.font = 'Candice'
        draw.font_size = 72
        draw.gravity = 'center'
        draw.text_kerning = -6
        draw.fill_color = Color('white')
        draw.stroke_width = 4
        draw.stroke_color = Color('black')
        draw.text(0, 0, text)
        draw.stroke_color = Color('none')
        draw.text(0, 0, text)
        draw(img)
        img.save(filename='sample19.png')
