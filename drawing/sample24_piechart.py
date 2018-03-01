#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/#arcs
# original imagemagick command:
# convert -size 140x130 xc:white -stroke black \
#   -fill red   -draw "path 'M 60,70 L   60,20   A 50,50 0 0,1 68.7,20.8 Z'" \
#   -fill green -draw "path 'M 60,70 L 68.7,20.8 A 50,50 0 0,1 77.1,23.0 Z'" \
#   -fill blue  -draw "path 'M 68,65 L 85.1,18.0 A 50,50 0 0,1  118,65   Z'" \
#   -fill gold  -draw "path 'M 60,70 L  110,70   A 50,50 0 1,1   60,20   Z'" \
#   -fill black -stroke none  -pointsize 10 \
#   -draw "text 57,19 '10' text 70,20 '10' text 90,19 '70' text 113,78 '270'" \
#   piechart.jpg


def draw_figure(draw, start, top, **kwargs):
    draw.path_start()
    draw.path_move(start)
    draw.path_line(top)
    draw.path_elliptic_arc(**kwargs)
    draw.path_close()
    draw.path_finish()


with Image(width=140, height=130, background=Color('white')) as img:
    with Drawing() as draw:
        draw.stroke_color = Color('black')
        draw.fill_color = Color('red')
        draw_figure(draw, (60, 70), (60, 20), radius=(50, 50),
                    to=(68.7, 20.8), clockwise=True)
        draw.fill_color = Color('green')
        draw_figure(draw, (60, 70), (68.7, 20.8), radius=(50, 50),
                    to=(77.1, 23.0), clockwise=True)
        draw.fill_color = Color('blue')
        draw_figure(draw, (68, 65), (85.1, 18.0), radius=(50, 50),
                    to=(118, 65), clockwise=True)
        draw.fill_color = Color('gold')
        draw_figure(draw, (60, 70), (110, 70), radius=(50, 50),
                    to=(60, 20), large_arc=True, clockwise=True)

        draw.fill_color = Color('black')
        draw.stroke_color = Color('none')
        draw.font_size = 10
        draw.text(57, 19, '10')
        draw.text(70, 20, '10')
        draw.text(90, 19, '70')
        draw.text(113, 78, '270')
        draw(img)
    img.save(filename='sample24.png')
