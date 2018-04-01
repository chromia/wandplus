#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/#mvg_settings
# original imagemagick command:
# Stroke Opacity
# convert -size 100x60 xc:skyblue -fill none -stroke black \
#         -draw "                           path 'M 10,10 L 90,10'" \
#         -draw "stroke-opacity 0.8         path 'M 10,20 L 90,20'" \
#         -draw "stroke-opacity 0.6         path 'M 10,30 L 90,30'" \
#         -draw "stroke-opacity 0.4         path 'M 10,40 L 90,40'" \
#         -draw "stroke-opacity 0.2         path 'M 10,50 L 90,50'" \
#         set_stroke_opacity.gif

w = 100
h = 60
bgcolor = Color('skyblue')

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('none')
        draw.stroke_color = Color('black')
        draw.line((10, 10), (90, 10))
        draw.stroke_opacity = 0.8
        draw.line((10, 20), (90, 20))
        draw.stroke_opacity = 0.6
        draw.line((10, 30), (90, 30))
        draw.stroke_opacity = 0.4
        draw.line((10, 40), (90, 40))
        draw.stroke_opacity = 0.2
        draw.line((10, 50), (90, 50))
        draw(img)
    img.save(filename='sample18a.png')

# # Fill Opacity
# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "                    rectangle  5,10 15,50 " \
#         -draw "fill-opacity 0.8    rectangle 20,10 30,50 " \
#         -draw "fill-opacity 0.6    rectangle 35,10 45,50 " \
#         -draw "fill-opacity 0.4    rectangle 50,10 60,50 " \
#         -draw "fill-opacity 0.2    rectangle 65,10 75,50 " \
#         -draw "fill-opacity  0     rectangle 80,10 90,50 " \
#         set_fill_opacity.gif

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.rectangle(5, 10, right=15, bottom=50)
        draw.fill_opacity = 0.8
        draw.rectangle(20, 10, right=30, bottom=50)
        draw.fill_opacity = 0.6
        draw.rectangle(35, 10, right=45, bottom=50)
        draw.fill_opacity = 0.4
        draw.rectangle(50, 10, right=60, bottom=50)
        draw.fill_opacity = 0.2
        draw.rectangle(65, 10, right=75, bottom=50)
        draw.fill_opacity = 0.0
        draw.rectangle(80, 10, right=90, bottom=50)
        draw(img)
    img.save(filename='sample18b.png')

# Plain and Dashed Lines
# convert -size 100x60 xc:skyblue -fill none -stroke black \
#         -draw "                           path 'M 10,10 L 90,10'" \
#         -draw "stroke-dasharray 5 3       path 'M 10,20 L 90,20'" \
#         -draw "stroke-dasharray 5 5       path 'M 10,30 L 90,30'" \
#         -draw "stroke-dasharray 10 3 3 3  path 'M 10,40 L 90,40'" \
#         -draw "stroke-dasharray 1 6       path 'M 10,50 L 90,50'" \
#         set_lines.gif

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('none')
        draw.stroke_color = Color('black')
        draw.line((10, 10), (90, 10))
        draw.stroke_dash_array = [5, 3]
        draw.line((10, 20), (90, 20))
        draw.stroke_dash_array = [5, 5]
        draw.line((10, 30), (90, 30))
        draw.stroke_dash_array = [10, 3, 3, 3]
        draw.line((10, 40), (90, 40))
        draw.stroke_dash_array = [1, 6]
        draw.line((10, 50), (90, 50))
        draw(img)
    img.save(filename='sample18c.png')

# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "                           path 'M 10,10 L 90,10'" \
#         -draw "stroke-dasharray 5 3       path 'M 10,20 L 90,20'" \
#         -draw "stroke-dasharray 5 5       path 'M 10,30 L 90,30'" \
#         -draw "stroke-dasharray 10 3 3 3  path 'M 10,40 L 90,40'" \
#         -draw "stroke-dasharray 1 6       path 'M 10,50 L 90,50'" \
#         set_lines_fill.gif

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')  # none->white
        draw.stroke_color = Color('black')
        draw.line((10, 10), (90, 10))
        draw.stroke_dash_array = [5, 3]
        draw.line((10, 20), (90, 20))
        draw.stroke_dash_array = [5, 5]
        draw.line((10, 30), (90, 30))
        draw.stroke_dash_array = [10, 3, 3, 3]
        draw.line((10, 40), (90, 40))
        draw.stroke_dash_array = [1, 6]
        draw.line((10, 50), (90, 50))
        draw(img)
    img.save(filename='sample18d.png')

# Stroke Ends and Joins
# convert -size 100x60 xc:skyblue -fill white -stroke black -strokewidth 8 \
#         -draw "                           path 'M 20,20 L 20,70'" \
#         -draw "stroke-linecap butt        path 'M 40,20 L 40,70'" \
#         -draw "stroke-linecap round       path 'M 60,20 L 60,70'" \
#         -draw "stroke-linecap square      path 'M 80,20 L 80,70'" \
#         set_endcaps.gif

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')  # none->white
        draw.stroke_color = Color('black')
        draw.stroke_width = 8
        draw.line((20, 20), (20, 70))
        draw.stroke_line_cap = 'butt'
        draw.line((40, 20), (40, 70))
        draw.stroke_line_cap = 'round'
        draw.line((60, 20), (60, 70))
        draw.stroke_line_cap = 'square'
        draw.line((80, 20), (80, 70))
        draw(img)
    img.save(filename='sample18e.png')

# convert -size 100x60 xc:skyblue -fill white -stroke black -strokewidth 5 \
#         -draw "                        path 'M  5,70 L 20,20  35,70'" \
#         -draw "stroke-linejoin miter   path 'M 35,70 L 50,20  65,70'" \
#         -draw "stroke-linejoin bevel   path 'M 55,70 L 70,20  85,70'" \
#         -draw "stroke-linejoin round   path 'M 75,70 L 90,20 105,70'" \
#         set_linejoin.gif


def draw_triangle(draw, points):
    draw.path_start()
    draw.path_move(points[0])
    draw.path_line(points[1])
    draw.path_line(points[2])
    draw.path_finish()


with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')  # none->white
        draw.stroke_color = Color('black')
        draw.stroke_width = 5
        draw_triangle(draw, [(5, 70), (20, 20), (35, 70)])
        draw.stroke_line_join = 'miter'
        draw_triangle(draw, [(35, 70), (50, 20), (65, 70)])
        draw.stroke_line_join = 'bevel'
        draw_triangle(draw, [(55, 70), (70, 20), (85, 70)])
        draw.stroke_line_join = 'round'
        draw_triangle(draw, [(75, 70), (90, 20), (105, 70)])
        draw(img)
    img.save(filename='sample18f.png')

# convert -size 100x60 xc:skyblue -fill white -stroke black -strokewidth 5 \
#         -draw "                        path 'M  5,70 L 20,20  35,70'" \
#         -draw "stroke-miterlimit 7     path 'M 35,70 L 50,20  65,70'" \
#         -draw "stroke-miterlimit 6     path 'M 65,70 L 80,20  95,70'" \
#         set_miterlimit.gif

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')  # none->white
        draw.stroke_color = Color('black')
        draw.stroke_width = 5
        draw_triangle(draw, [(5, 70), (20, 20), (35, 70)])
        draw.stroke_miter_limit = 7
        draw_triangle(draw, [(35, 70), (50, 20), (65, 70)])
        draw.stroke_miter_limit = 6
        draw_triangle(draw, [(65, 70), (80, 20), (95, 70)])
        draw(img)
    img.save(filename='sample18g.png')
