#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/
# original imagemagick command:
# Circle  /  Ellipse    (centered on a point)
# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "circle 50,30 40,10"          draw_circle.gif
#
# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "ellipse 50,30 40,20 0,360"   draw_ellipse.gif
#
# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "ellipse 50,30 40,20 45,270"   draw_ellipse_partial.gif


def makedrawing():
    draw = Drawing()
    draw.fill_color = Color('white')
    draw.stroke_color = Color('black')
    draw.stroke_width = 1
    return draw


w = 100
h = 60
bgcolor = Color('skyblue')

with Image(width=w, height=h, background=bgcolor) as img:
    with makedrawing() as draw:
        draw.circle((50, 30), (40, 10))
        draw(img)
        img.save(filename='sample03a.png')

with Image(width=w, height=h, background=bgcolor) as img:
    with makedrawing() as draw:
        draw.ellipse((50, 30), (40, 20))
        draw(img)
        img.save(filename='sample03b.png')

with Image(width=w, height=h, background=bgcolor) as img:
    with makedrawing() as draw:
        draw.ellipse((50, 30), (40, 20), (45, 270))
        draw(img)
        img.save(filename='sample03c.png')
