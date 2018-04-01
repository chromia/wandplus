#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# This is an original exsample.

"""
translate/rotate/scale example
the usage of these function is similar to OpenGL(also push/pop)
"""


def draw_ellipse(draw):
    draw.ellipse((50, 30), (30, 15))  # fixed coordinate


with Image(width=200, height=200, background=Color('skyblue')) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')

        # draw original figure
        draw.push()
        draw_ellipse(draw)
        draw.pop()

        # move
        draw.push()
        draw.fill_color = Color('red')
        draw.translate(70, 0)
        draw_ellipse(draw)
        draw.pop()

        # rotate
        draw.push()
        draw.fill_color = Color('green')
        draw.rotate(45)
        draw_ellipse(draw)
        draw.pop()  # Note: rotation is done around the origin.

        # rotate & move
        draw.push()
        draw.fill_color = Color('blue')
        draw.translate(50, 80)  # 3. move down
        draw.rotate(90)  # 2. rotate 90 degree
        draw.translate(-50, -30)  # 1. move the center of the ellipse to (0,0)
        draw_ellipse(draw)
        draw.pop()

        # rotate & move & scale
        draw.push()
        draw.fill_color = Color('cyan')
        draw.translate(120, 120)  # 4. move
        draw.rotate(90)  # 3. rotate 90 degree
        draw.scale(2, 2)  # 2. double
        draw.translate(-50, -30)  # 1. move the center of the ellipse to (0,0)
        draw_ellipse(draw)
        draw.pop()

        draw(img)
    img.save(filename='sample29.png')
