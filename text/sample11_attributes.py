from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.textutil import calcSuitableFontsize

# http://www.imagemagick.org/Usage/text/
# original imagemagick command:
# convert -background white -fill dodgerblue  -font Candice \
#            -strokewidth 2  -stroke blue   -undercolor lightblue \
#            -size 165x70 -gravity center label:Anthony     label_color.gif

w = 165
h = 70
with Drawing() as draw:
    text = 'Anthony'
    draw.font = 'Candice'
    draw.font_size = calcSuitableFontsize(draw, text, width=w, height=h)
    with Image(width=w, height=h, background=Color('white')) as img:
        draw.gravity = 'center'
        draw.text_under_color = Color('lightblue')
        draw.fill_color = Color('dodgerblue')
        draw.stroke_color = Color('blue')
        draw.stroke_width = 2
        draw.text(0, 0, text)
        draw(img)
        img.save(filename='sample11.png')
