from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
import math

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
# convert -size 320x115 xc:lightblue  -font Candice -pointsize 72 \
#         -fill Navy      -annotate 0x0+12+55   'Anthony' \
#         -fill RoyalBlue -annotate 0x130+25+80 'Anthony' \
#         font_slewed.jpg


w = 320
h = 115
with Image(width=w, height=h, background=Color('lightblue')) as img:
    with Drawing() as draw:
        text = 'Anthony'
        draw.font = 'Candice'
        draw.font_size = 72
        draw.gravity = 'forget'
        draw.fill_color = Color('navy')
        draw.text(12, 55, text)

        # NOTE: annotate option format of IM is {SlewX}x{SlewY}+{X}+{Y}
        # But Wand doesn't have slew function,
        # so we emulate it by rotate,translate,skew,scale
        x = 25
        y = 80
        angle = 130
        skewangle = math.fmod(angle, 360)
        if (0 <= skewangle and skewangle < 90) or (270 <= skewangle and skewangle < 360):
            skewangle = skewangle * -1.0
        draw.translate(x, y)  # 3.positioning
        draw.skew(skewangle, 0)  # 2.skewing
        draw.scale(1.0, math.cos(math.radians(angle)))  # 1.flipping & shlinking vertically
        draw.fill_color = Color('royalblue')
        draw.text(0, 0, text)
        draw(img)
        img.save(filename='sample05.png')
