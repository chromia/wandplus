from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.image import shadow

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
# convert -size 300x100 xc:none -font Candice -pointsize 72 \
#         -fill white  -stroke black  -annotate +25+65 'Anthony' \
#         \( +clone -background navy  -shadow 70x4+5+5 \) +swap \
#         -background lightblue -flatten  -trim +repage  font_shadow_soft.jpg


w = 300
h = 100
with Image(width=w, height=h) as img:
    with Drawing() as draw0:
        text = 'Anthony'
        draw0.font = 'Candice'
        draw0.font_size = 72
        draw0.gravity = 'forget'

        x = 25
        y = 65

        # drawing shadow
        with draw0.clone() as draw:
            draw.fill_color = Color('white')
            draw.text(x, y, text)
            draw(img)
        img.background_color = Color('navy')
        shadow(img, 70, 4, 5, 5)

        # drawing foreground text
        with draw0.clone() as draw:
            draw.fill_color = Color('white')
            draw.stroke_color = Color('black')
            draw.text(x, y, text)
            draw(img)

        # add background color
        with Image(width=img.width, height=img.height,
                   background=Color('lightblue')) as result:
            result.composite(img, 0, 0)
            result.trim()
            result.save(filename='sample24.png')
