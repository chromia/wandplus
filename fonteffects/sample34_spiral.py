#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.textutil import calcSuitableImagesize

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
#  convert -font Candice -pointsize 32 -background lightblue \
#          -fill navy  label:"Anthony's IM Examples" \
#          -rotate 12 -virtual-pixel background -distort Arc 360 \
#          -trim -bordercolor lightblue -border 5x5  font_spiral.jpg


with Drawing() as draw:
    text = 'Anthony\'s IM Examples'
    draw.font = 'Candice'
    draw.font_size = 32
    draw.gravity = 'center'
    (w, h) = calcSuitableImagesize(draw, text)
    bgcolor = Color('lightblue')
    with Image(width=w, height=h, background=bgcolor) as img:
        draw.fill_color = Color('navy')
        draw.text(0, 0, text)
        draw(img)
        img.rotate(12, bgcolor)
        img.distort('arc', [360], False)
        img.trim(color=bgcolor)
        img.frame(matte=bgcolor, width=5, height=5)
        img.save(filename='sample34.png')
