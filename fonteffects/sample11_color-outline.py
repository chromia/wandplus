from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
# convert -size 320x100 xc:lightblue \
#         -font Candice -pointsize 72  -gravity center \
#         -draw "fill navy         text  2,2  'Anthony' \
#                fill navy         text  0,3  'Anthony' \
#                fill navy         text  3,0  'Anthony' \
#                fill dodgerblue   text  0,2  'Anthony' \
#                fill dodgerblue   text  2,0  'Anthony' \
#                fill dodgerblue   text -2,2  'Anthony' \
#                fill dodgerblue   text  2,-2 'Anthony' \
#                fill lavender     text -2,-2 'Anthony' \
#                fill lavender     text  0,-3 'Anthony' \
#                fill lavender     text -3,0  'Anthony' \
#                fill skyblue      text  0,-2 'Anthony' \
#                fill skyblue      text -2,0  'Anthony' \
#                fill blue         text  0,0  'Anthony' " \
#         font_colourful.jpg


def outline3(draw, text, x, y):
    draw.fill_color = Color('navy')
    draw.text(x+2, y+2, text)
    draw.text(x, y+3, text)
    draw.text(x+3, y, text)
    draw.fill_color = Color('dodgerblue')
    draw.text(x, y+2, text)
    draw.text(x+2, y, text)
    draw.text(x-2, y+2, text)
    draw.text(x+2, y-2, text)
    draw.fill_color = Color('lavender')
    draw.text(x-2, y-2, text)
    draw.text(x, y-3, text)
    draw.text(x-3, y, text)
    draw.fill_color = Color('skyblue')
    draw.text(x, y-2, text)
    draw.text(x+2, y, text)
    draw.fill_color = Color('blue')
    draw.text(x, y, text)


w = 320
h = 100
with Image(width=w, height=h, background=Color('lightblue')) as img:
    with Drawing() as draw:
        text = 'Anthony'
        draw.font = 'Candice'
        draw.font_size = 72
        draw.gravity = 'forget'
        outline3(draw, text, 25, 65)
        draw(img)
        img.save(filename='sample11.png')
