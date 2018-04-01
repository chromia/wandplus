#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.image import blur
from wandplus.textutil import calcSuitableImagesize

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
#  convert -fill dodgerblue -background black -font Anaconda -pointsize 72 \
#          label:' I M  Examples ' -bordercolor black -border 30x30 \
#          \( +clone -blur 0x25 -level 0%,50% \) \
#          -compose screen -composite    neon_sign.gif


with Drawing() as draw:
    text = ' I M  Examples '
    draw.font = 'Anaconda-Regular'
    draw.font_size = 72
    (w, h) = calcSuitableImagesize(draw, text)

    # make text image
    textimg = Image(width=w, height=h, background=Color('black'))
    draw.gravity = 'center'
    draw.fill_color = Color('dodgerblue')
    draw.text(0, 0, text)
    draw(textimg)
    textimg.border(Color('black'), 30, 30)

    # make shadow image
    shadowimg = textimg.clone()
    blur(shadowimg, 0, 25)
    shadowimg.level(black=0.0, gamma=1.0, white=0.5)

    # composite all
    canvas = Image(width=shadowimg.width, height=shadowimg.height)
    canvas.composite(shadowimg, 0, 0)
    canvas.composite_channel('default_channels', textimg, 'screen')
    canvas.save(filename='sample40.png')

    shadowimg.destroy()
    textimg.destroy()
    canvas.destroy()
