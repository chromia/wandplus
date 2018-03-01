#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/#colorspace
# original imagemagick command:
# convert rose:  -fill none -stroke white -draw 'line 5,40 65,5'  rose_raw.png
#
# convert rose: -gamma .454545 \
#         -fill none -stroke white -draw 'line 5,40 65,5' \
#         -gamma 2.2 rose_gamma.png
#
# convert rose: -colorspace RGB \
#         -fill none -stroke white -draw 'line 5,40 65,5' \
#         -colorspace sRGB rose_sRGB.png

with Image(filename='rose:') as img:
    with Drawing() as draw:
        draw.stroke_color = Color('white')
        draw.line((5, 40), (65, 5))
        draw(img)
    img.save(filename='sample14a.png')

with Image(filename='rose:') as img:
    img.gamma(0.454545)
    with Drawing() as draw:
        draw.stroke_color = Color('white')
        draw.line((5, 40), (65, 5))
        draw(img)
    img.gamma(2.2)
    img.save(filename='sample14b.png')

with Image(filename='rose:') as img:
    img.colorspace = 'rgb'
    with Drawing() as draw:
        draw.stroke_color = Color('white')
        draw.line((5, 40), (65, 5))
        draw(img)
    img.colorspace = 'srgb'
    img.save(filename='sample14c.png')
