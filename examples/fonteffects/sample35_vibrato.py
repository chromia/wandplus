#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.image import wave

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
#  convert -size 320x100 xc:lightblue -font Candice -pointsize 72 \
#          -fill navy  -annotate +25+65 'Anthony' \
#          -background lightblue -rotate 85  -wave 2x5   -rotate -85 \
#          -gravity center  -crop 320x100+0+0 +repage font_vibrato.jpg


w = 320
h = 100
bgcolor = Color('lightblue')
with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        text = 'Anthony'
        draw.font = 'Candice'
        draw.font_size = 72
        draw.gravity = 'center'
        draw.fill_color = Color('navy')
        draw.text(0, 0, text)
        draw(img)
    img.rotate(85, background=bgcolor)
    wave(img, 2, 5)  # vertical only
    img.rotate(-85, background=bgcolor)
    img.crop(width=w, height=h, gravity='center')
    img.save(filename='sample35.png')
