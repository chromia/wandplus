#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.textutil import calcSuitableImagesize

# http://www.imagemagick.org/Usage/text/
# original imagemagick commands:

# env LC_CTYPE=en_AU.utf8 \
#     printf "\u2018single\u2019 - \u201Cdouble\u201D" | \
#       convert -background lightblue -fill blue -pointsize 36 \
#               label:@-  label_quotes.gif

# perl -e 'binmode(STDOUT, ":utf8"); \
#     print "\x{201C}Unicode \x{2018}\x{263A}\x{2019} Please\x{201D}";' |\
#       convert -background lightblue -fill blue -pointsize 36 \
#               label:@-  label_unifun.gif

# graphics_utf -N 2701 2718 |\
#     convert -font Mincho -pointsize 32 label:@-   label_dingbats.gif

# graphics_utf -N 2620 2630 |\
#     convert -font Mincho   -pointsize 40 label:@- label_misc.gif

text = """\u2018single\u2019 - \u201Cdouble\u201D
\u201CUnicode \u2018\u263A\u2019 Please\u201D
"""
text += ''.join([chr(r) for r in range(0x2701, 0x2719)]) + '\n'
text += ''.join([chr(r) for r in range(0x2620, 0x2630)])

with Drawing() as draw:
    draw.font = 'DejaVu-Sans'
    draw.font_size = 36
    (w, h) = calcSuitableImagesize(draw, text, multiline=True)
    with Image(width=w, height=h, background=Color('lightblue')) as img:
        draw.gravity = 'north_west'
        draw.fill_color = Color('blue')
        draw.text(0, 0, text)
        draw(img)
        img.save(filename='sample13.png')
