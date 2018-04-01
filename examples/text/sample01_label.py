#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/text/
# original imagemagick command:
# convert -background lightblue -fill blue \
#           -font Candice -pointsize 72 label:Anthony \
#           label.gif

with Image(width=1, height=1) as dummy:
    with Drawing() as draw:
        text = 'Anthony'
        draw.font = 'Candice'
        draw.font_size = 72
        # calculate suitable canvas size & drawing offset
        #    see also more easy sample 'sample01_label2_simplify.py'
        mt = draw.get_font_metrics(dummy, text)
        (x, y, w, h) = (0, int(mt.descender), int(mt.text_width), int(mt.text_height+mt.y1))
        with Image(width=w, height=h, background=Color('lightblue')) as img:
            draw.fill_color = Color('blue')  # equals Color('#0000FF')
            draw.text(x, h+y, text)
            draw(img)
            img.save(filename='sample01a.png')
