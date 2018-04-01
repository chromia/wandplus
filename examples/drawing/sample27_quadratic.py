#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/#quad
# original imagemagick command:
#
# Quadratic Bezier:  Q  control_x,y  x,y
# Smooth " :         T  x,y
#
# convert path_quad_canvas.gif  -fill white -stroke black \
#         -draw "path 'M 10,30   Q 20,4 50,30   T 90,30' " \
#         path_quad.gif


def draw_control(draw, base, to, r, fill=True):
    draw.push()
    if not fill:
        draw.fill_color = Color('none')
    draw.line(base, to)
    draw.circle(to, (to[0], to[1]-r))
    draw.pop()


w = 100
h = 60
bgcolor = Color('skyblue')

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.path_start()
        draw.path_move((10, 30))
        draw.path_curve_to_quadratic_bezier(control=(20, 4), to=(50, 30))
        draw.path_curve_to_quadratic_bezier(smooth=True, to=(90, 30))
        draw.path_finish()

        draw.fill_color = Color('dodgerblue')
        draw.stroke_color = Color('dodgerblue')
        draw_control(draw, (10, 30), (20, 4), 3)
        draw_control(draw, (50, 30), (20, 4), 3)
        draw_control(draw, (50, 30), (80, 56), 3, False)
        draw_control(draw, (90, 30), (80, 56), 3, False)
        draw(img)
    img.save(filename='sample27a.png')

# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "path 'M 20,55  Q 30,32 25,10
#                               Q 50,1 70,5
#                               Q 50,45 20,55 Z' " triangle_bulge_2.gif

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.path_start()
        draw.path_move((20, 55))
        draw.path_curve_to_quadratic_bezier(control=(30, 32), to=(25, 10))
        draw.path_curve_to_quadratic_bezier(control=(50, 1), to=(70, 5))
        draw.path_curve_to_quadratic_bezier(control=(50, 45), to=(20, 55))
        draw.path_close()
        draw.path_finish()
        draw(img)
    img.save(filename='sample27b.png')
