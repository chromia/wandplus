from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.image import shade

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
#  convert -size 320x100 xc:black -font Candice -pointsize 72 \
#          -fill white   -annotate +25+65 'Anthony' \
#          -shade 140x45  font_beveled.jpg


w = 320
h = 100
with Image(width=w, height=h, background=Color('black')) as img:
    with Drawing() as draw:
        text = 'Anthony'
        draw.font = 'Candice'
        draw.font_size = 72
        draw.gravity = 'center'
        draw.fill_color = Color('white')
        draw.text(0, 0, text)
        draw(img)
        shade(img, True, 140, 45)
        img.save(filename='sample28.png')
