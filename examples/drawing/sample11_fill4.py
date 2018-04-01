#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.image import setfuzz

# http://www.imagemagick.org/Usage/draw/
# original imagemagick command:
# convert color_test.png   -fill white  -bordercolor royalblue \
#         -draw 'color 30,20 filltoborder'   color_filltoborder.png
#
# convert color_test.png   -fill white  -bordercolor blue \
#         -draw 'color 30,20 filltoborder'   color_filltoborder2.png
#
# convert color_test.png   -fill white  -bordercolor blue  -fuzz 30% \
#         -draw 'color 30,20 filltoborder'   color_filltoborder_fuzz.png
#
# convert color_test.png   -fill white \
#         -draw 'color 30,20 reset'      color_reset.png


def color_test():
    w = 100
    h = 60
    img = Image(width=w, height=h, background=Color('skyblue'))
    with Drawing() as draw:
        draw.stroke_color = Color('none')
        draw.fill_color = Color('dodgerblue')
        draw.ellipse((50, 30), (40, 20))
        draw.fill_color = Color('blue')
        draw.circle((50, 30), (40, 20))
        draw.stroke_width = 5
        draw.stroke_color = Color('black')
        draw.fill_color = Color('none')
        draw.line((0, 30), (100, 30))
        draw.stroke_color = Color('royalblue')
        draw.line((50, 0), (50, 60))
        draw(img)
    return img


with color_test() as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.border_color = Color('royalblue')
        draw.color(30, 20, 'filltoborder')
        draw(img)
        img.save(filename='sample11a.png')

with color_test() as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.border_color = Color('blue')
        draw.color(30, 20, 'filltoborder')
        draw(img)
        img.save(filename='sample11b.png')

with color_test() as img:
    setfuzz(img, 0.30*img.quantum_range)  # =30%
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.border_color = Color('blue')
        draw.color(30, 20, 'filltoborder')
        draw(img)
        img.save(filename='sample11c.png')
        # NOTE: result is a little different from original

with color_test() as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.color(30, 20, 'reset')
        draw(img)
        img.save(filename='sample11d.png')
