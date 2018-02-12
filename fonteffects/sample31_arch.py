from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.image import wave

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
#  convert -size 320x100 xc:lightblue -font Candice -pointsize 72 \
#          -fill navy  -annotate +25+65 'Anthony' \
#          -background lightblue -wave -50x640 -crop x110+0+10 \
#          font_wavy.jpg


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
    img.background_color = Color('lightblue')
    wave(img, -50, 640)
    img.crop(0, 10, width=img.width, height=110)
    img.save(filename='sample31.png')
