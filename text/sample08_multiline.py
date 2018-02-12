from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.textutil import calcSuitableImagesize

# http://www.imagemagick.org/Usage/text/
# original imagemagick command:
# convert -background lightblue  -fill blue  -font Ravie -pointsize 20 \
#           label:'ImageMagick\nRules - OK!'     label_multiline.gif

with Drawing() as draw:
    text = 'ImageMagick\nRules - OK!'
    draw.font = 'Ravie'
    draw.font_size = 20
    (w, h) = calcSuitableImagesize(draw, text, multiline=True)
    with Image(width=w, height=h, background=Color('lightblue')) as img:
        draw.gravity = 'north_west'
        draw.fill_color = Color('blue')
        draw.text(0, 0, text)
        draw(img)
        img.save(filename='sample08.png')
