from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
#  convert -size 320x100 xc:lightblue -font Candice -pointsize 72 \
#          -fill navy -annotate +25+65 'Anthony' \
#          -distort Arc 120  -trim +repage \
#          -bordercolor lightblue -border 10  font_arc.jpg


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
    img.distort('arc', [120], True)
    img.trim(color=Color('lightblue'))
    img.frame(matte=Color('lightblue'), width=10, height=10)
    img.save(filename='sample32.png')
