from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.image import motionblur, wave

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
#  convert -size 320x120 xc:lightblue  -font Candice  -pointsize 72 \
#          -fill black  -annotate +25+95 'Anthony'  -motion-blur 0x25+90 \
#          -background lightblue -rotate 60  -wave 3x35  -rotate -60 \
#          -gravity center  -crop 320x120+0+0 +repage +gravity \
#          -fill navy   -annotate +25+95 'Anthony'   font_smoking.jpg


w = 320
h = 120
bgcolor = Color('lightblue')
with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        text = 'Anthony'
        draw.font = 'Candice'
        draw.font_size = 72
        draw.gravity = 'forget'
        x = 25
        y = 95
        draw.fill_color = Color('black')
        draw.text(x, y, text)
        draw(img)
        motionblur(img, 0, 25, 90)
        img.rotate(60, background=bgcolor)
        wave(img, 3, 35)
        img.rotate(-60, background=bgcolor)
        img.crop(width=w, height=h, gravity='center')
        draw.fill_color = Color('navy')
        draw.text(x, y, text)
        draw(img)
        img.save(filename='sample37.png')
