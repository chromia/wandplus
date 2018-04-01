#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# This is an original exsample.

"""
push/pop example
"""
with Image(width=200, height=100, background=Color('skyblue')) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.font_size = 24

        draw.text(10, 30, 'before push')

        draw.push()  # 'push' saves the state of context
        draw.stroke_color = Color('none')
        draw.fill_color = Color('red')
        draw.text(10, 60, 'pushed')
        draw.pop()  # 'pop' restores the state at the time 'push' was called

        draw.text(10, 90, 'after pop')

        draw(img)
    img.save(filename='sample28.png')
