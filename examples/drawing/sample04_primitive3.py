#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/
# original imagemagick command:
# Line / Polyline / Polygon / Bezier
# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "line   20,50 90,10"                 draw_line.gif
#
# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "polyline 40,10 20,50 90,10 70,40"   draw_polyline.gif
#
# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "polygon  40,10 20,50 90,10 70,40"   draw_polygon.gif
#
# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "bezier   40,10 20,50 90,10 70,40"   draw_bezier.gif


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
        draw.line((20, 50), (90, 10))
        draw(img)
        img.save(filename='sample04a.png')

with Image(width=w, height=h, background=bgcolor) as img:
    with makedrawing() as draw:
        draw.polyline([(40, 10), (20, 50), (90, 10), (70, 40)])
        draw(img)
        img.save(filename='sample04b.png')

with Image(width=w, height=h, background=bgcolor) as img:
    with makedrawing() as draw:
        draw.polygon([(40, 10), (20, 50), (90, 10), (70, 40)])
        draw(img)
        img.save(filename='sample04c.png')

with Image(width=w, height=h, background=bgcolor) as img:
    with makedrawing() as draw:
        draw.bezier([(40, 10), (20, 50), (90, 10), (70, 40)])
        draw(img)
        img.save(filename='sample04d.png')
