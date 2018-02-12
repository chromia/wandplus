from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
# convert -size 320x100 xc:lightblue -font Candice -pointsize 72 \
#         -stroke black -strokewidth 4 -fill white \
#         -stroke black -annotate  +28+68 A  -stroke none -annotate  +28+68 A \
#         -stroke black -annotate  +90+68 n  -stroke none -annotate  +90+68 n \
#         -stroke black -annotate +120+68 t  -stroke none -annotate +120+68 t \
#         -stroke black -annotate +138+68 h  -stroke none -annotate +138+68 h \
#         -stroke black -annotate +168+68 o  -stroke none -annotate +168+68 o \
#         -stroke black -annotate +193+68 n  -stroke none -annotate +193+68 n \
#         -stroke black -annotate +223+68 y  -stroke none -annotate +223+68 y \
#         font_overlapped.jpg


def drawcharacter(draw, char, x, y, color):
    draw.stroke_color = color
    draw.text(x, y, char)
    draw.stroke_color = Color('none')
    draw.text(x, y, char)


w = 320
h = 100
with Image(width=w, height=h, background=Color('lightblue')) as img:
    with Drawing() as draw:
        draw.font = 'Candice'
        draw.font_size = 72
        draw.gravity = 'forget'
        draw.fill_color = Color('white')
        draw.stroke_width = 4
        drawcharacter(draw, 'A',  26, 68, Color('black'))
        drawcharacter(draw, 'n',  90, 68, Color('black'))
        drawcharacter(draw, 't', 120, 68, Color('black'))
        drawcharacter(draw, 'h', 138, 68, Color('black'))
        drawcharacter(draw, 'o', 168, 68, Color('black'))
        drawcharacter(draw, 'n', 193, 68, Color('black'))
        drawcharacter(draw, 'y', 223, 68, Color('black'))
        draw(img)
        img.save(filename='sample20.png')
