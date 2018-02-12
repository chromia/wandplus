from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.textutil import calcSuitableImagesize
import os

# http://www.imagemagick.org/Usage/text/
# original imagemagick command:
# convert -background lightblue -fill blue -pointsize 48 \
#           -font ZenKaiUni label:@chinese_words.utf8   label_utf8.gif

fontname = 'WenQuanYi-Micro-Hei'  # Linux(Ubuntu)
if os.name == 'nt':
    fontname = 'SimSun-&-NSimSun'  # Windows

with Drawing() as draw:
    text = '测试用的汉字'  # Chinese
    draw.font = fontname
    draw.font_size = 48
    (w, h) = calcSuitableImagesize(draw, text)
    with Image(width=w, height=h, background=Color('lightblue')) as img:
        draw.gravity = 'north_west'
        draw.fill_color = Color('blue')
        draw.text(0, 0, text)
        draw(img)
        img.save(filename='sample12.png')
