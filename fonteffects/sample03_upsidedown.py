from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
# convert -size 320x100 xc:lightblue -font Candice -pointsize 72 \
#         -fill Navy     -annotate 180x180+300+35 'Anthony' \
#         font_upsidedown.jpg


w = 320
h = 100
with Image(width=w, height=h, background=Color('lightblue')) as img:
    with Drawing() as draw:
        text = 'Anthony'
        draw.font = 'Candice'
        draw.font_size = 72
        draw.gravity = 'center'
        draw.fill_color = Color('navy')
        draw.text(0, 0, text)
        draw(img)
        img.flip()  # flip vertically
        img.flop()  # flip horizontally
        img.save(filename='sample03.png')
