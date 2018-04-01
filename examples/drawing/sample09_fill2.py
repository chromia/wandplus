#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/
# original imagemagick command:
# convert -size 3x1 xc:red -matte -fill '#00F8' \
#         -draw 'point 1,0' \
#         -draw 'color 2,0 point'   -scale 33x33  draw_points.png


with Image(width=3, height=1, background=Color('red')) as img:
    img.alpha_channel = True  # -matte means 'to enable alpha channels'
    with Drawing() as draw:
        draw.fill_color = Color('#00F8')  # RGBA
        draw.point(1, 0)
        draw.color(2, 0, 'point')
        draw(img)
    img.resize(33, 11, 'point')
    img.save(filename='sample09.png')
