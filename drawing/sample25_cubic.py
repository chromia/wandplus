#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/#arcs
# original imagemagick command:
# Cubic Bezier:    C  control_1_x,y control_2_x,y  x,y
# Smooth " :       S  control_2_x,y  x,y
#
# convert path_cubic_canvas.gif  -fill white -stroke black \
#         -draw "path 'M 10,30  C 10,4 50,4 50,30  S 90,55 90,30' " \
#         path_cubic.gif


def draw_control(draw, base, to, r, fill=True):
    draw.push()
    if not fill:
        draw.fill_color = Color('none')
    draw.line(base, to)
    draw.circle(to, (to[0], to[1]-r))
    draw.pop()


with Image(width=100, height=60, background=Color('skyblue')) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.path_start()
        draw.path_move((10, 30))
        draw.path_curve(controls=[(10, 4), (50, 4)], to=(50, 30))
        draw.path_curve(smooth=True, controls=(90, 55), to=(90, 30))
        draw.path_finish()

        draw.fill_color = Color('dodgerblue')
        draw.stroke_color = Color('dodgerblue')
        draw_control(draw, (10, 30), (10, 4), 3)
        draw_control(draw, (50, 30), (50, 4), 3)
        draw_control(draw, (50, 30), (50, 56), 3, False)
        draw_control(draw, (90, 30), (90, 56), 3)
        draw(img)
    img.save(filename='sample25.png')
