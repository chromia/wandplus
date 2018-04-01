#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/#stroke
# original imagemagick command:
# convert -size 380x70 xc:lightblue -pointsize 50 -font Chisel \
#         -fill green  -stroke black  -draw 'text 10,55 "Black Border"' \
#         stroke_font.jpg
#
# convert -size 320x420 xc:lightblue -pointsize 70 -font Vademecum \
#   -fill red -stroke none                 -draw 'text 30,80  "Stroke -"' \
#   -fill red -stroke black -strokewidth 0 -draw 'text 30,160 "Stroke 0"' \
#   -fill red -stroke black -strokewidth 1 -draw 'text 30,240 "Stroke 1"' \
#   -fill red -stroke black -strokewidth 2 -draw 'text 30,320 "Stroke 2"' \
#   -fill red -stroke black -strokewidth 3 -draw 'text 30,400 "Stroke 3"' \
#   stroke_table.jpg
#
# convert -size 320x100 xc:lightblue -font Candice -pointsize 72 -fill white \
#         -stroke black -strokewidth 15 -draw "text 25,65 'Anthony'" \
#         stroke_thick.jpg
#
# convert -size 320x100 xc:lightblue -font Candice -pointsize 72 -fill white \
#         -stroke black -strokewidth 15 -draw "text 25,65 'Anthony'" \
#         -stroke none                  -draw "text 25,65 'Anthony'" \
#         stroke_outline.jpg

with Image(width=380, height=70, background=Color('lightblue')) as img:
    with Drawing() as draw:
        draw.font = 'Chisel'
        draw.font_size = 50
        draw.fill_color = Color('green')
        draw.stroke_color = Color('black')
        draw.text(10, 55, 'Black Border')
        draw(img)
    img.save(filename='sample15a.png')

with Image(width=320, height=420, background=Color('lightblue')) as img:
    with Drawing() as draw:
        draw.font = 'Vademecum'
        draw.font_size = 70
        draw.fill_color = Color('red')
        draw.stroke_color = Color('none')
        draw.text(30, 80, 'Stroke -')
        draw.stroke_color = Color('black')
        draw.stroke_width = 0
        draw.text(30, 160, 'Stroke 0')
        draw.stroke_width = 1
        draw.text(30, 240, 'Stroke 1')
        draw.stroke_width = 2
        draw.text(30, 320, 'Stroke 2')
        draw.stroke_width = 3
        draw.text(30, 400, 'Stroke 3')
        draw(img)
    img.save(filename='sample15b.png')

# convert -size 320x100 xc:lightblue -font Candice -pointsize 72 -fill white \
#         -stroke black -strokewidth 15 -draw "text 25,65 'Anthony'" \
#         stroke_thick.jpg

with Image(width=320, height=100, background=Color('lightblue')) as img:
    with Drawing() as draw:
        draw.font = 'Candice'
        draw.font_size = 72
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.stroke_width = 15
        draw.text(25, 65, 'Anthony')
        draw(img)
    img.save(filename='sample15c.png')

with Image(width=320, height=100, background=Color('lightblue')) as img:
    with Drawing() as draw:
        draw.font = 'Candice'
        draw.font_size = 72
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.stroke_width = 15
        draw.text(25, 65, 'Anthony')
        draw.stroke_color = Color('none')
        draw.text(25, 65, 'Anthony')
        draw(img)
    img.save(filename='sample15d.png')
