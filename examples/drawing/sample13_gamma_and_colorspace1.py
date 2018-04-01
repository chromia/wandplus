#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/#colorspace
# original imagemagick command:
# convert -size 81x81 xc:black -fill white -draw 'circle 40,40 40,3' \
#          circle_raw.png
#
# convert -size 81x81 xc:black -fill white -draw 'circle 40,40 40,3' \
#         -gamma 2.2 circle_gamma.png
#
# convert -size 81x81 xc:black -set colorspace RGB \
#         -fill white -draw 'circle 40,40 40,3' \
#         -colorspace sRGB circle_sRGB.png

w = 81
h = 81
bgcolor = Color('black')

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.circle((40, 40), (40, 3))
        draw(img)
    img.save(filename='sample13a.png')

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.circle((40, 40), (40, 3))
        draw(img)
    img.gamma(2.2)
    img.save(filename='sample13b.png')

with Image(width=w, height=h, background=bgcolor) as img:
    img.colorspace = 'rgb'
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.circle((40, 40), (40, 3))
        draw(img)
    img.colorspace = 'srgb'
    img.save(filename='sample13c.png')
