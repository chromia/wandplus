from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.textutil import calcSuitableImagesize

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
#  convert -font Candice -pointsize 32 -background lightblue \
#          -fill navy label:"Anthony's IM Examples" \
#          -virtual-pixel background  -distort Arc 340 \
#          font_circle.jpg


with Drawing() as draw:
    text = 'Anthony\'s IM Examples'
    draw.font = 'Candice'
    draw.font_size = 32
    draw.gravity = 'center'
    (w, h) = calcSuitableImagesize(draw, text)
    with Image(width=w, height=h, background=Color('lightblue')) as img:
        draw.fill_color = Color('navy')
        draw.text(0, 0, text)
        draw(img)
        img.distort('arc', [340], False)
        img.save(filename='sample33.png')
