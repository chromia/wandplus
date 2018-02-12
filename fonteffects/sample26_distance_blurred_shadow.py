from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
import math

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
# convert -size 320x40 xc:lightblue  -font Candice -pointsize 72 \
#           -fill RoyalBlue -annotate 0x125+20+0 'Anthony' \
#           \( -size 320x45 gradient:black -append \) \
#           -compose Blur -set option:compose:args 20x5+45 -composite \
#           \( -size 320x60 xc:lightblue \
#              -fill Navy    -annotate 0x0+20+59   'Anthony' \) \
#           +swap -append   font_var_blur.jpg

# This example is incomplete.

w = 320
h = 100
with Image(width=w, height=h, background=Color('lightblue')) as img:
    with Drawing() as draw0:
        text = 'Anthony'
        draw0.font = 'Candice'
        draw0.font_size = 72
        draw0.gravity = 'forget'

        x = 25
        y = 65
        angle = 125
        adjustx = -6
        adjusty = 32
        adjusth = int(h*0.4)
        maxsigma = 5

        # make shadow imagemagick
        with Image(width=w, height=adjusth, background=Color('lightblue')) as shadow:
            with shadow.clone() as shearedtext:
                with draw0.clone() as draw:
                    # draw sheared shadow(see also sample05)
                    skewangle = math.fmod(angle, 360)
                    if (0 <= skewangle and skewangle < 90) or (270 <= skewangle and skewangle < 360):
                        skewangle = skewangle * -1.0
                    draw.translate(x, y-adjusty)  # 3.positioning
                    draw.skew(skewangle, 0)  # 2.skewing
                    draw.scale(1.0, math.cos(math.radians(angle)))  # 1.flipping & shlinking vertically
                    draw.gravity = 'north_west'
                    draw.fill_color = Color('royalblue')
                    draw.text(0, 0, text)
                    draw(shearedtext)
                # linear blur
                # It's TOO WASTERFUL code. FIX me.
                for by in range(shadow.height):
                    with shearedtext.clone() as work:
                        work.gaussian_blur(0, by/(shadow.height-1)*maxsigma)
                        shadow.composite(work[0:work.width, by:by+1], 0, by)

            # drawing foreground text
            with draw0.clone() as draw:
                draw.fill_color = Color('navy')
                draw.text(x, y, text)
                draw(img)

            # composite
            img.composite(shadow, x+adjustx, y)
            img.save(filename='sample26.png')
