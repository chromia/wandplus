#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
import math

# This is an original exsample.

bgcolor = Color('skyblue')

"""
affine example
Drawing.affine accepts the sequence: [sx, rx, ry, sy, tx, ty]
 sx, sy are scale factors.
 rx, ry are rotation coefficients.
 tx, ty are movement quantity.

the affine matrix and the formula is defined below:
| x' |   | sx rx tx |   | x |
| y' | = | ry sy ty | * | y |
| 1  |   |  0  0  1 |   | 1 |
"""


def draw_ellipse(draw):
    draw.ellipse((50, 30), (30, 15))


with Image(width=200, height=200, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')

        # draw original figure
        draw.push()
        draw_ellipse(draw)
        draw.pop()

        # move
        # |  1  0  tx |
        # |  0  1  ty |
        # |  0  0   1 |
        draw.push()
        draw.fill_color = Color('red')
        # draw.translate(70, 0)
        draw.affine([1, 0, 0, 1, 70, 0])
        draw_ellipse(draw)
        draw.pop()

        # rotate
        # | cos(x) -sin(x) 0 |
        # | sin(x)  cos(x) 0 |
        # |   0       0    1 |
        draw.push()
        draw.fill_color = Color('green')
        # draw.rotate(45)
        rad = math.radians(45)
        c = math.cos(rad)
        s = math.sin(rad)
        draw.affine([c, s, -s, c, 0, 0])
        draw_ellipse(draw)
        draw.pop()

        # rotate & move
        draw.push()
        draw.fill_color = Color('blue')
        # draw.translate(50, 80)  # 3. move down
        # draw.rotate(90)  # 2. rotate 90 degree
        # draw.translate(-50, -30)  # 1. move the center of the ellipse to (0,0)
        draw.affine([1, 0, 0, 1, 50, 80])
        draw.affine([0, -1, 1, 0, 0, 0])
        draw.affine([1, 0, 0, 1, -50, -30])
        draw_ellipse(draw)
        draw.pop()

        # rotate & move & scale
        draw.push()
        draw.fill_color = Color('cyan')
        # draw.translate(120, 120)  # 4. move
        # draw.rotate(90)  # 3. rotate 90 degree
        # draw.scale(2, 2)  # 2. double
        # draw.translate(-50, -30)  # 1. move the center of the ellipse to (0,0)
        draw.affine([0, -2, 2, 0, 120, 120])  # 2&3&4
        draw.affine([1, 0, 0, 1, -50, -30])  # 1
        draw_ellipse(draw)
        draw.pop()

        draw(img)
    img.save(filename='sample30.png')
