#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/
# original imagemagick command:
# Point 'paints' the color pixel
# convert -size 10x6 xc:skyblue  -fill black \
#         -draw 'point 3,2'         -scale 100x60   draw_point.gif
#
# Color Point 'replaces' the color pixel
# convert -size 10x6 xc:skyblue  -fill black \
#         -draw 'color 6,3 point'   -scale 100x60   draw_color_point.gif

with Image(width=10, height=6, background=Color('skyblue')) as img:
    with Drawing() as draw:
        draw.point(3, 2)
        draw(img)
    img.resize(100, 60, 'point')
    img.save(filename='sample01a.png')

with Image(width=10, height=6, background=Color('skyblue')) as img:
    with Drawing() as draw:
        draw.point(6, 3)
        draw(img)
    img.resize(100, 60, 'point')
    img.save(filename='sample01b.png')
