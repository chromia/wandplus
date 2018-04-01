#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/#strokewidth
# original imagemagick command:
# convert -size 100x40 xc:lightblue \
#         -draw "line 5,35 95,5" \
#         line_default.jpg

with Image(width=100, height=40, background=Color('lightblue')) as img:
    with Drawing() as draw:
        draw.line((5, 35), (95, 5))
        draw(img)
    img.save(filename='sample16a.png')

# convert -size 100x40 xc:lightblue \
#         -fill white -draw "line 5,35 95,5" \
#         line.jpg

with Image(width=100, height=40, background=Color('lightblue')) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.line((5, 35), (95, 5))
        draw(img)
    img.save(filename='sample16b.png')

# convert -size 100x40 xc:lightblue \
#         -fill white -stroke black -draw "line 5,35 95,5" \
#         line_stroke.jpg

with Image(width=100, height=40, background=Color('lightblue')) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.line((5, 35), (95, 5))
        draw(img)
    img.save(filename='sample16c.png')

# convert -size 100x40 xc:lightblue \
#         -fill white -strokewidth 3 -draw "line 5,35 95,5" \
#         line_fill_3.jpg

with Image(width=100, height=40, background=Color('lightblue')) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        # draw.stroke_color = Color('black')
        draw.stroke_width = 3
        draw.line((5, 35), (95, 5))
        draw(img)
    img.save(filename='sample16d.png')

# convert -size 100x40 xc:lightblue \
#         -stroke black -strokewidth 3 -draw "line 5,35 95,5" \
#         line_stroke_3.jpg

with Image(width=100, height=40, background=Color('lightblue')) as img:
    with Drawing() as draw:
        # draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.stroke_width = 3
        draw.line((5, 35), (95, 5))
        draw(img)
    img.save(filename='sample16e.png')

# convert -size 100x40 xc:lightblue \
#         -stroke black -strokewidth 1 -draw "line 5,35 95,5" \
#         line_stroke_1.jpg

with Image(width=100, height=40, background=Color('lightblue')) as img:
    with Drawing() as draw:
        draw.stroke_color = Color('black')
        draw.stroke_width = 1
        draw.line((5, 35), (95, 5))
        draw(img)
    img.save(filename='sample16f.png')

# convert -size 100x40 xc:lightblue \
#         -stroke black -strokewidth 5 -draw "line 5,35 95,5" \
#         -stroke white -strokewidth 2 -draw "line 5,35 95,5" \
#         line_multi.jpg

with Image(width=100, height=40, background=Color('lightblue')) as img:
    with Drawing() as draw:
        draw.stroke_color = Color('black')
        draw.stroke_width = 5
        draw.line((5, 35), (95, 5))
        draw.stroke_color = Color('white')
        draw.stroke_width = 2
        draw.line((5, 35), (95, 5))
        draw(img)
    img.save(filename='sample16g.png')

#  convert -size 100x40 xc:lightblue \
#          -fill white -stroke black -strokewidth 0 -draw "line 5,35 95,5" \
#          line_stroke_0.jpg
#

with Image(width=100, height=40, background=Color('lightblue')) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.stroke_width = 0
        draw.line((5, 35), (95, 5))
        draw(img)
    img.save(filename='sample16h.png')

# convert -size 25x10 xc:lightblue \
#         -fill white -stroke black -strokewidth 0 -draw "line 2,8 22,1" \
#         -scale 400%    line_stroke_0_white.jpg

with Image(width=25, height=10, background=Color('lightblue')) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.stroke_width = 0
        draw.line((2, 8), (22, 1))
        draw(img)
    img.resize(100, 40, 'point')
    img.save(filename='sample16i.png')

# convert -size 100x40 xc:lightblue \
#         -fill white -stroke black -strokewidth 0 -draw "line 5,20 95,20" \
#         line_stroke_horz.jpg

with Image(width=100, height=40, background=Color('lightblue')) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.stroke_width = 0
        draw.line((5, 20), (95, 20))
        draw(img)
    img.save(filename='sample16j.png')

# convert -size 25x10 xc:lightblue \
#         -fill none -stroke black -strokewidth 0 -draw "line 2,8 22,1" \
#         -scale 400%     line_stroke_0_none.jpg

with Image(width=25, height=10, background=Color('lightblue')) as img:
    with Drawing() as draw:
        draw.fill_color = Color('none')
        draw.stroke_color = Color('black')
        draw.stroke_width = 0
        draw.line((2, 8), (22, 1))
        draw(img)
    img.resize(100, 40, 'point')
    img.save(filename='sample16k.png')

# convert -size 25x10 xc:lightblue \
#         -fill red -stroke black -strokewidth 0 -draw "line 2,8 22,1" \
#         -scale 400%     line_stroke_0_none.jpg

with Image(width=25, height=10, background=Color('lightblue')) as img:
    with Drawing() as draw:
        draw.fill_color = Color('red')
        draw.stroke_color = Color('black')
        draw.stroke_width = 0
        draw.line((2, 8), (22, 1))
        draw(img)
    img.resize(100, 40, 'point')
    img.save(filename='sample16l.png')

# convert -size 25x10 xc:lightblue \
#         -fill black -stroke black -strokewidth 0 -draw "line 2,8 22,1" \
#         -scale 400%     line_stroke_0_none.jpg

with Image(width=25, height=10, background=Color('lightblue')) as img:
    with Drawing() as draw:
        draw.fill_color = Color('black')
        draw.stroke_color = Color('black')
        draw.stroke_width = 0
        draw.line((2, 8), (22, 1))
        draw(img)
    img.resize(100, 40, 'point')
    img.save(filename='sample16m.png')

# convert -size 25x10 xc:lightblue \
#         -fill black -stroke none -draw "line 2,8 22,1" \
#         -scale 400%    line_stroke_-_black.jpg

with Image(width=25, height=10, background=Color('lightblue')) as img:
    with Drawing() as draw:
        draw.fill_color = Color('black')
        draw.stroke_color = Color('none')
        draw.stroke_width = 0
        draw.line((2, 8), (22, 1))
        draw(img)
    img.resize(100, 40, 'point')
    img.save(filename='sample16n.png')
