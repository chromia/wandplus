#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
import os

# this is original code.

font_normal = 'Noto-Sans'
font_italic = 'Noto-Sans-Italic'
font_bold = 'Noto-Sans-Bold'
if os.name == 'nt':
    font_normal = 'Arial'
    font_italic = 'Arial-Italic'
    font_bold = 'Arial-Bold'

w = 500
h = 350
with Drawing() as draw:
    with Image(width=w, height=h, background=Color('lightblue')) as img:
        draw.font_size = 32
        draw.fill_color = Color('blue')

        # [Style]
        draw.font = font_normal
        draw.text(0, 30, '[Style]')
        # Italic ( you must use italic-compliant font, e.g. Arial,  )
        draw.font = font_italic
        draw.font_style = 'italic'
        draw.text(0, 60, 'Italic')
        draw.font_style = 'normal'  # default
        # Bold ( you must use bold-compliant font, e.g. Courier,  )
        draw.font = font_bold
        draw.text(0, 90, 'Bold')
        # Underline
        draw.font = font_normal
        draw.text_decoration = 'underline'
        draw.text(0, 120, 'Underline')  # Is the line rather thin?
        # Overline
        draw.text_decoration = 'overline'
        draw.text(0, 160, 'Overline')
        # Strike
        draw.text_decoration = 'line_through'
        draw.text(0, 190, 'Strike')
        draw.text_decoration = 'no'  # default
        # Non-Antialias
        draw.text_antialias = False
        draw.text(0, 220, 'Antialias-off')
        draw.text_antialias = True  # default

        # [Stroke]
        draw.fill_color = Color('dodgerblue')
        draw.stroke_color = Color('blue')
        draw.stroke_width = 1
        draw.text(200, 30, '[Stroke]')
        # Non-Antialias
        draw.stroke_antialias = False
        draw.text(200, 60, 'Antialias-off')
        draw.stroke_antialias = True  # default
        # Opacity
        draw.stroke_opacity = 0.3
        draw.text(200, 90, 'Opacity')
        draw.stroke_opacity = 1.0  # default
        # Width
        draw.stroke_width = 2.0
        draw.text(200, 120, 'Width')
        draw.stroke_width = 1
        draw.stroke_color = Color('none')  # default

        # [Space]
        draw.fill_color = Color('blue')
        draw.text(200, 170, '[Space]')
        # Kerning
        draw.text_kerning = -2
        draw.text(200, 200, 'Kerning=-2')
        draw.text_kerning = 0
        draw.text(200, 230, 'Kerning=0')
        draw.text_kerning = 2
        draw.text(200, 260, 'Kerning=2')
        draw.text_kerning = 0
        # Word Space
        draw.text_interword_spacing = 10
        draw.text(200, 290, 'Word Space 10')
        draw.text_interword_spacing = 20
        draw.text(200, 320, 'Word Space 20')

        draw(img)
        img.save(filename='sample14.png')
