from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
# convert -size 320x100 xc:lightblue -font Candice -pointsize 72 \
#         -tile gradient:   -annotate +28+68 'Anthony' \
#         font_gradient.jpg


def draw_gradient_vertical(draw, w, h, color1, color2):
    draw.push()
    draw.stroke_width = 1
    draw.stroke_antialias = False
    for y in range(h):
        p = y / (h-1)
        r = int((color1.red * (1-p) + color2.red * p) * 255)
        g = int((color1.green * (1-p) + color2.green * p) * 255)
        b = int((color1.blue * (1-p) + color2.blue * p) * 255)
        col = Color('rgb({0},{1},{2})'.format(r, g, b))
        draw.stroke_color = col
        draw.line((0, y), (w, y))
    draw.pop()


w = 320
h = 100
with Image(width=w, height=h, background=Color('lightblue')) as img:
    with Drawing() as draw:
        text = 'Anthony'
        draw.font = 'Candice'
        draw.font_size = 72
        draw.gravity = 'center'

        # get text rectangle
        mt = draw.get_font_metrics(img, text)
        (txw, txh) = (int(mt.text_width), int(mt.text_height))

        # make gradient pattern
        draw.push_pattern('gradient', 0, 0, txw, txh)
        draw_gradient_vertical(draw, txw, txh, Color('white'), Color('black'))
        draw.pop_pattern()

        draw.set_fill_pattern_url('#gradient')  # fill with defined pattern
        draw.text(0, 0, text)
        draw(img)
        img.save(filename='sample02b.png')
