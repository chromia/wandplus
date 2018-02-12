from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.image import shade, autolevel, morphology, adaptiveblur

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
#  convert -size 320x100 xc:black -font Candice -pointsize 72 \
#          -fill white   -annotate +25+65 'Anthony' \
#          -gamma 2  +level 0,1000 -white-threshold 999 \
#          -morphology Distance Euclidean:4,1000 -auto-level \
#          -shade 135x30 -auto-level +level 10,90% \
#          -adaptive-blur 0x2  font_conic_smoothed.jpg


w = 320
h = 100
with Image(width=w, height=h, background=Color('black')) as img:
    with Drawing() as draw:
        text = 'Anthony'
        draw.font = 'Candice'
        draw.font_size = 72
        draw.gravity = 'forget'
        draw.fill_color = Color('white')
        draw.text(25, 65, text)
        draw(img)
    img.gamma(2)
    morphology(img, 'distance', 1, 'Euclidean:4')
    autolevel(img)
    shade(img, True, 135, 30)
    autolevel(img)
    adaptiveblur(img, 0, 2)
    img.save(filename='sample30.png')
