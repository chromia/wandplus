from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
# convert -size 320x100 xc:lightblue -font Candice -pointsize 72 \
#         -draw "fill black text 27,67 'Anthony' \
#                           text 25,68 'Anthony' \
#                           text 23,67 'Anthony' \
#                           text 22,65 'Anthony' \
#                           text 23,63 'Anthony' \
#                           text 25,62 'Anthony' \
#                           text 27,63 'Anthony' \
#                           text 28,65 'Anthony' \
#                fill white text 25,65 'Anthony' " \
#         font_outlined_12.jpg


def outline2(draw, text, x, y, outcolor, incolor):
    draw.fill_color = outcolor
    draw.text(x-2, y-2, text)
    draw.text(x, y-3, text)
    draw.text(x+2, y-2, text)
    draw.text(x-3, y, text)
    draw.text(x, y, text)
    draw.text(x+3, y, text)
    draw.text(x-2, y+2, text)
    draw.text(x, y+3, text)
    draw.text(x+2, y+2, text)
    draw.fill_color = incolor
    draw.text(x, y, text)


w = 320
h = 100
with Image(width=w, height=h, background=Color('lightblue')) as img:
    with Drawing() as draw:
        text = 'Anthony'
        draw.font = 'Candice'
        draw.font_size = 72
        draw.gravity = 'forget'
        outline2(draw, text, 25, 65, Color('black'), Color('white'))
        draw(img)
        img.save(filename='sample10.png')
