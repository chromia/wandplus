from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.image import blur

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
# convert -size 320x100 xc:lightblue -font Candice -pointsize 72 \
#         -stroke black -strokewidth 8 -annotate +25+65 'Anthony' -blur 0x8 \
#         -fill white   -stroke none   -annotate +25+65 'Anthony' \
#         font_denser_soft_outline.jpg


w = 320
h = 100
with Image(width=w, height=h, background=Color('lightblue')) as img:
    with Drawing() as draw0:
        text = 'Anthony'
        draw0.font = 'Candice'
        draw0.font_size = 72
        draw0.gravity = 'forget'

        x = 25
        y = 65

        # drawing shadow
        with draw0.clone() as draw:
            draw.fill_color = Color('black')
            draw.stroke_color = Color('black')
            draw.stroke_width = 8
            draw.text(x, y, text)
            draw(img)
        blur(img, 0, 8)

        # drawing foreground text
        with draw0.clone() as draw:
            draw.fill_color = Color('white')
            draw.text(x, y, text)
            draw(img)

        img.save(filename='sample25.png')
