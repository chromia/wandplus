#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/
# original imagemagick command:
# points="10,10 30,90   25,10    75,90   70,10 90,40"
# symbols=`for point in $points; do
#            echo "M $point   l -2,-2 +4,+4 -2,-2   l -2,+2 +4,-4 -2,+2"
#          done`
# convert -size 100x100  xc:skyblue  -fill none \
#         -draw "stroke gray  polyline $points " \
#         -draw "stroke red   bezier $points " \
#         -draw "stroke blue  path '$symbols' " \
#         draw_bezier_multi.gif


def drawcross(draw, center, length):
    x1 = center[0] - length / 2
    x2 = center[0] + length / 2
    y1 = center[1] - length / 2
    y2 = center[1] + length / 2
    draw.line((x1, y1), (x2, y2))
    draw.line((x2, y1), (x1, y2))


points = [(10, 10), (30, 90), (25, 10), (75, 90), (70, 10), (90, 40)]


def beziersample2(points, filename):
    w = 100
    h = 100
    bgcolor = Color('skyblue')

    with Image(width=w, height=h, background=bgcolor) as img:
        with Drawing() as draw:
            draw.stroke_width = 1
            draw.fill_color = Color('transparent')

            # draw control lines
            draw.stroke_color = Color('gray')
            draw.polyline(points)

            # draw points
            draw.stroke_color = Color('blue')
            for point in points:
                drawcross(draw, point, 4)

            # draw bezier
            draw.stroke_color = Color('red')
            draw.bezier(points)

            draw(img)
            img.save(filename=filename)


beziersample2(points, 'sample07.png')
