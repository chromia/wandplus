#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/#paths
# original imagemagick command:
# Overlapping Paths and Fill Rule
# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "fill-rule evenodd \
#                path 'M 40,10 20,20 70,50 Z
#                      M 20,40 70,40 90,10 Z' " path_evenodd.gif
#
# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "fill-rule nonzero \
#                path 'M 40,10 20,20 70,50 Z
#                      M 20,40 70,40 90,10 Z' " path_nonzero.gif


def drawpath(rule, filename):
    with Image(width=100, height=60, background=Color('skyblue')) as img:
        with Drawing() as draw:
            draw.fill_color = Color('white')
            draw.stroke_color = Color('black')
            draw.fill_rule = rule
            draw.path_start()
            draw.path_move((40, 10))
            draw.path_line((20, 20))
            draw.path_line((70, 50))
            draw.path_close()
            draw.path_move((20, 40))
            draw.path_line((70, 40))  # please try to swap
            draw.path_line((90, 10))  # these lines
            draw.path_close()
            draw.path_finish()
            draw(img)
        img.save(filename=filename)


drawpath('evenodd', 'sample19a.png')
drawpath('nonzero', 'sample19b.png')
