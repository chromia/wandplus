from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
# convert -size 320x100 xc:lightblue  -font Candice -pointsize 72 \
#         -fill Navy -draw "translate 28,68  skewX -20  text 0,0 'Anthony'" \
#         font_slanted.jpg


w = 320
h = 100
with Image(width=w, height=h, background=Color('lightblue')) as img:
    with Drawing() as draw:
        text = 'Anthony'
        draw.font = 'Candice'
        draw.font_size = 72
        draw.gravity = 'forget'
        draw.fill_color = Color('navy')
        draw.translate(28, 68)
        draw.skew(-20, 0)
        draw.text(0, 0, text)
        draw(img)
        img.save(filename='sample06.png')
