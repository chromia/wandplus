#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
# convert -size 320x100 xc:lightblue -font Candice -pointsize 72 -fill white \
#         -stroke black -strokewidth 25 -annotate +25+65 'Anthony' \
#         -stroke white -strokewidth 20 -annotate +25+65 'Anthony' \
#         -stroke black -strokewidth 15 -annotate +25+65 'Anthony' \
#         -stroke white -strokewidth 10 -annotate +25+65 'Anthony' \
#         -stroke black -strokewidth  5 -annotate +25+65 'Anthony' \
#         -stroke none                  -annotate +25+65 'Anthony' \
#         font_psychedelic.jpg


def drawstroke(draw, text, width, color):
    draw.stroke_width = width
    draw.stroke_color = color
    draw.text(0, 0, text)


w = 320
h = 100
with Image(width=w, height=h, background=Color('lightblue')) as img:
    with Drawing() as draw:
        text = 'Anthony'
        draw.font = 'Candice'
        draw.font_size = 72
        draw.gravity = 'center'
        draw.fill_color = Color('white')
        drawstroke(draw, text, 25, Color('black'))
        drawstroke(draw, text, 20, Color('white'))
        drawstroke(draw, text, 15, Color('black'))
        drawstroke(draw, text, 10, Color('white'))
        drawstroke(draw, text,  5, Color('black'))
        drawstroke(draw, text,  0, Color('none'))
        draw(img)
        img.save(filename='sample17.png')
