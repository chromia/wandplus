#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/#bounds
# original imagemagick command:
# convert -size 10x10 xc: -draw 'polygon 2,-1 7,10 10,10 10,-1' bound_left.gif
# convert -size 10x10 xc: -draw 'polygon 2,-1 7,10 -1,10 -1,-1' bound_right.gif
#
# convert bound_left.gif bound_right.gif -compose Plus -composite bound_add.gif

# NOTE: xc: means 'white canvas'
with Image(width=10, height=10, background=Color('white')) as left:
    with Image(width=10, height=10, background=Color('white')) as right:
        with Drawing() as draw:
            draw.polygon([(2, -1), (7, 10), (10, 10), (10, -1)])
            draw(left)
            left.save(filename='sample17a.png')
        with Drawing() as draw:
            draw.polygon([(2, -1), (7, 10), (-1, 10), (-1, -1)])
            draw(right)
            right.save(filename='sample17b.png')
        left.composite_channel('default_channels', right, 'plus')
        left.save(filename='sample17c.png')
