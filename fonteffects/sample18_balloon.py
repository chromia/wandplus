from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
# convert -size 320x100 xc:lightblue -font Candice -pointsize 72 \
#         -fill black  -stroke black  -strokewidth 5  -annotate +25+65 'Anthony' \
#         -fill white  -stroke white  -strokewidth 1  -annotate +25+65 'Anthony' \
#         font_balloon.jpg


w = 320
h = 100
with Image(width=w, height=h, background=Color('lightblue')) as img:
    with Drawing() as draw:
        text = 'Anthony'
        draw.font = 'Candice'
        draw.font_size = 72
        draw.gravity = 'center'
        draw.fill_color = Color('black')
        draw.stroke_color = Color('black')
        draw.stroke_width = 5
        draw.text(0, 0, text)
        draw.fill_color = Color('white')
        draw.stroke_color = Color('white')
        draw.stroke_width = 1
        draw.text(0, 0, text)
        draw(img)
        img.save(filename='sample18.png')
