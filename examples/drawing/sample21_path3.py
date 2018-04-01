#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/#paths
# original imagemagick command:
# An object with a reversed drawn hole!
# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "path 'M 30,10 20,55 70,50 80,5 Z
#                      M 50,20 60,40 40,30 Z' " path_with_hole.gif
#
# Separate paths are separate objects
# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "path 'M 40,10 20,20 70,50 Z'
#                path 'M 20,40 70,40 90,10 Z' " path_separate.gif

with Image(width=100, height=60, background=Color('skyblue')) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.path_start()
        draw.path_move((30, 10))
        draw.path_line((20, 55))
        draw.path_line((70, 50))
        draw.path_line((80, 5))
        draw.path_close()
        draw.path_move((50, 20))
        draw.path_line((60, 40))
        draw.path_line((40, 30))
        draw.path_close()
        draw.path_finish()
        draw(img)
    img.save(filename='sample21a.png')

with Image(width=100, height=60, background=Color('skyblue')) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.path_start()
        draw.path_move((40, 10))
        draw.path_line((20, 20))
        draw.path_line((70, 50))
        draw.path_close()
        draw.path_finish()

        draw.path_start()
        draw.path_move((20, 40))
        draw.path_line((70, 40))
        draw.path_line((90, 10))
        draw.path_close()
        draw.path_finish()
        draw(img)
    img.save(filename='sample21b.png')
