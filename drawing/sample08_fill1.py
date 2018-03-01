#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/
# original imagemagick command:
# convert color_test.png   -fill white \
#         -draw 'color 30,20 point'      color_point.png


def color_test():
    w = 100
    h = 60
    img = Image(width=w, height=h, background=Color('skyblue'))
    with Drawing() as draw:
        draw.stroke_color = Color('none')
        draw.fill_color = Color('dodgerblue')
        draw.ellipse((50, 30), (40, 20))
        draw.fill_color = Color('blue')
        draw.circle((50, 30), (40, 20))
        draw.stroke_width = 5
        draw.stroke_color = Color('black')
        draw.fill_color = Color('none')
        draw.line((0, 30), (100, 30))
        draw.stroke_color = Color('royalblue')
        draw.line((50, 0), (50, 60))
        draw(img)
    return img


with color_test() as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.color(30, 20, 'point')
        draw(img)
        img.save(filename='sample08.png')
