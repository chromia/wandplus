from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.image import blur, spread

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
#  convert -size 320x100 xc: \
#          -font Candice -pointsize 72 -annotate +25+65 'Anthony' \
#          -spread 1 -blur 0x1 -threshold 50% -blur 0x1 font_dirty_print.jpg


w = 320
h = 100
with Image(width=w, height=h, background=Color('white')) as img:
    with Drawing() as draw:
        text = 'Anthony'
        draw.font = 'Candice'
        draw.font_size = 72
        draw.gravity = 'forget'
        draw.fill_color = Color('black')
        draw.text(25, 65, text)
        draw(img)
        spread(img, 'bilinear', 1)
        blur(img, 0, 1)
        img.threshold(0.5)
        blur(img, 0, 1)
        img.save(filename='sample27.png')
