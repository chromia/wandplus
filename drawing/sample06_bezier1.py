#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/
# original imagemagick command:
# points="10,10 30,90   25,10 50,50   50,50 75,90   70,10 90,40"
# clines=`echo "$points" | sed 's/   /\n/g' |\
#            while read line; do echo "line $line"; done`
# symbols=`echo path "'"; for point in $points; do
#            echo "M $point   l -2,-2 +4,+4 -2,-2   l -2,+2 +4,-4 -2,+2"
#          done;  echo "'"`
# convert -size 100x100 xc:skyblue -fill none \
#         -draw "stroke gray $clines    stroke blue $symbols " \
#         -draw "stroke red  bezier 10,10 30,90   25,10 50,50 " \
#         -draw "stroke red  bezier 50,50 75,90   70,10 90,40 " \
#         draw_bezier_joined.gif


def drawcross(draw, center, length):
    x1 = center[0] - length / 2
    x2 = center[0] + length / 2
    y1 = center[1] - length / 2
    y2 = center[1] + length / 2
    draw.line((x1, y1), (x2, y2))
    draw.line((x2, y1), (x1, y2))


joined = [
    [(10, 10), (30, 90), (25, 10), (50, 50)],
    [(50, 50), (75, 90), (70, 10), (90, 40)]
]
disjoined = [
    [(10, 10), (30, 90), (25, 10), (50, 50)],
    [(50, 50), (80, 50), (70, 10), (90, 40)]
]
no_curve = [
    [(10, 10), (30, 90), (25, 10), (50, 50)],
    [(50, 50), (50, 50), (70, 10), (90, 40)]
]
lines = [
    [(10, 10), (10, 10), (50, 50), (50, 50)],
    [(50, 50), (50, 50), (90, 40), (90, 40)]
]


def beziersample(pointlists, filename):
    w = 100
    h = 100
    bgcolor = Color('skyblue')

    with Image(width=w, height=h, background=bgcolor) as img:
        with Drawing() as draw:
            draw.stroke_width = 1
            draw.fill_color = Color('none')

            # draw control lines
            draw.stroke_color = Color('gray')
            for points in pointlists:
                for i in range(0, len(points), 2):
                    draw.line(points[i], points[i+1])

            # draw points
            draw.stroke_color = Color('blue')
            for points in pointlists:
                for point in points:
                    drawcross(draw, point, 4)

            # draw bezier
            draw.stroke_color = Color('red')
            for points in pointlists:
                draw.bezier(points)

            draw(img)
            img.save(filename=filename)


beziersample(joined, 'sample06a.png')
beziersample(disjoined, 'sample06b.png')
beziersample(no_curve, 'sample06c.png')
beziersample(lines, 'sample06d.png')
