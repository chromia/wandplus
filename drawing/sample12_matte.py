#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.image import setfuzz

# http://www.imagemagick.org/Usage/draw/
# original imagemagick command:
# convert color_test.png   -fill none \
#         -draw 'matte 30,20 floodfill'      matte_floodfill.png
#
# convert color_test.png   -fill none   -fuzz 15%   \
#         -draw 'matte 30,20 floodfill'      matte_floodfill_fuzz.png
#
# convert color_test.png   -fill '#00000080' \
#         -draw 'matte 30,20 reset'      matte_reset.png


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
        draw.fill_color = Color('none')
        draw.matte(30, 20, 'floodfill')
        draw(img)
        img.save(filename='sample12a.png')

with color_test() as img:
    setfuzz(img, 0.15*img.quantum_range)
    with Drawing() as draw:
        draw.fill_color = Color('none')
        draw.matte(30, 20, 'floodfill')
        draw(img)
        img.save(filename='sample12b.png')

with color_test() as img:
    with Drawing() as draw:
        draw.fill_color = Color('#00000080')
        draw.matte(30, 20, 'reset')
        draw(img)
        img.save(filename='sample12c.png')
