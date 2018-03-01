#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/#paths
# original imagemagick command:
# Open, Completed and Closed Paths (same points)
#
# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "path 'M 40,10 L 20,50 90,10 70,40'" path_open.gif
#
# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "path 'M 40,10 L 20,50 90,10 70,40 40,10'" path_complete.gif
#
# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "path 'M 40,10 20,50 90,10 70,40 Z'" path_closed.gif

w = 100
h = 60
bgcolor = Color('skyblue')

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.path_start()
        draw.path_move((40, 10))
        draw.path_line((20, 50))
        draw.path_line((90, 10))
        draw.path_line((70, 40))
        # draw.path_close()
        draw.path_finish()
        draw(img)
    img.save(filename='sample18a.png')

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.path_start()
        draw.path_move((40, 10))
        draw.path_line((20, 50))
        draw.path_line((90, 10))
        draw.path_line((70, 40))
        draw.path_line((40, 10))  # back to the starting point
        draw.path_finish()
        draw(img)
    img.save(filename='sample18b.png')

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.path_start()
        draw.path_move((40, 10))
        draw.path_line((20, 50))
        draw.path_line((90, 10))
        draw.path_line((70, 40))
        draw.path_close()  # just close
        draw.path_finish()
        draw(img)
    img.save(filename='sample18c.png')
