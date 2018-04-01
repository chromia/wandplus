#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.textutil import calcSuitableImagesize

# http://www.imagemagick.org/Usage/text/
# original imagemagick command:
# echo -n "Vertical" | sed 's/./&@/g; s/@$//' | tr '@' '\012' |\
#     convert -background lightblue -fill blue -font Ravie -pointsize 24 \
#             -gravity center    label:@-   label_vertical.gif

with Drawing() as draw:
    text = 'Vertical'
    text = '\n'.join(list(text))  # insert \n between each char
    draw.font = 'Ravie'
    draw.font_size = 24
    draw.gravity = 'center'
    (w, h) = calcSuitableImagesize(draw, text, multiline=True)
    with Image(width=w, height=h, background=Color('lightblue')) as img:
        draw.fill_color = Color('blue')
        draw.text(0, 0, text)
        draw(img)
        img.save(filename='sample10.png')
