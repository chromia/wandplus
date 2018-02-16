#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
# convert -size 320x100 xc:lightblue -font Candice -pointsize 72 \
#         -stroke black -strokewidth 4 -fill white \
#         -stroke black -annotate  +26+80 A  -stroke none -annotate  +26+80 A \
#         -stroke black -annotate  +95+63 n  -stroke none -annotate  +95+63 n \
#         -stroke black -annotate +133+54 t  -stroke none -annotate +133+54 t \
#         -stroke black -annotate +156+67 h  -stroke none -annotate +156+67 h \
#         -stroke black -annotate +193+59 o  -stroke none -annotate +193+59 o \
#         -stroke black -annotate +225+59 n  -stroke none -annotate +225+59 n \
#         -stroke black -annotate +266+54 y  -stroke none -annotate +266+54 y \
#         font_jittered.jpg


def drawcharacter(draw, char, x, y, color):
    draw.stroke_color = color
    draw.text(x, y, char)
    draw.stroke_color = Color('none')
    draw.text(x, y, char)


w = 320
h = 100
with Image(width=w, height=h, background=Color('lightblue')) as img:
    with Drawing() as draw:
        draw.font = 'Candice'
        draw.font_size = 72
        draw.gravity = 'forget'
        draw.fill_color = Color('white')
        draw.stroke_width = 4
        drawcharacter(draw, 'A',  26, 80, Color('black'))
        drawcharacter(draw, 'n',  95, 63, Color('black'))
        drawcharacter(draw, 't', 133, 54, Color('black'))
        drawcharacter(draw, 'h', 156, 67, Color('black'))
        drawcharacter(draw, 'o', 193, 59, Color('black'))
        drawcharacter(draw, 'n', 225, 59, Color('black'))
        drawcharacter(draw, 'y', 266, 54, Color('black'))
        draw(img)
        img.save(filename='sample21.png')
