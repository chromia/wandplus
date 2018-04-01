#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/
# original imagemagick command:
# Rectangle  /  Rounded Rectangle  /  Rectangular Arc
# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "rectangle 20,10 80,50"       draw_rect.gif
#
# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "roundrectangle 20,10 80,50 20,15"  draw_rrect.gif
#
# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "arc  20,10 80,50  0,360"     draw_arc.gif
#
# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "arc  20,10 80,50 45,270"     draw_arc_partial.gif


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
        draw.rectangle(left=20, top=10, right=80, bottom=50)
        draw(img)
        img.save(filename='sample02a.png')

with Image(width=w, height=h, background=bgcolor) as img:
    with makedrawing() as draw:
        draw.rectangle(left=20, top=10, right=80, bottom=50,
                       xradius=20, yradius=15)
        draw(img)
        img.save(filename='sample02b.png')

with Image(width=w, height=h, background=bgcolor) as img:
    with makedrawing() as draw:
        draw.arc((20, 10), (80, 50), (0, 360))
        draw(img)
        img.save(filename='sample02c.png')

with Image(width=w, height=h, background=bgcolor) as img:
    with makedrawing() as draw:
        draw.arc((20, 10), (80, 50), (45, 270))
        draw(img)
        img.save(filename='sample02d.png')
