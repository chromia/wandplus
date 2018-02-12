from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.image import shave

# http://www.imagemagick.org/Usage/fonts/

#  convert -size 320x100 xc:transparent -font Candice -pointsize 72 \
#          -fill black        -annotate +24+64 'Anthony' \
#          -fill white        -annotate +26+66 'Anthony' \
#          -fill transparent  -annotate +25+65 'Anthony' \
#          trans_stamp.png
#  convert -size 320x180 plasma: -shave 0x40 plasma_background.jpg
#  composite trans_stamp.png   plasma_background.jpg  mask_result3.jpg


w = 320
h = 100
plasma_h = 180
text = 'Anthony'
font = 'Candice'
fontsize = 72
x = 25
y = 65

stamp = Image(width=w, height=h)
with Drawing() as draw:
    draw.font = font
    draw.font_size = fontsize
    draw.gravity = 'forget'
    draw.fill_color = Color('black')
    draw.text(x-1, y-1, text)
    draw.fill_color = Color('white')
    draw.text(x+1, y+1, text)
    draw.fill_color = Color('transparent')
    draw.text(x, y, text)
    draw(stamp)

plasma = Image(filename='plasma:', width=w, height=plasma_h)
shave(plasma, 0, 40)

plasma.composite(stamp, 0, 0)
plasma.save(filename='sample38.png')

stamp.destroy()
plasma.destroy()
