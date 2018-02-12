from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.image import sparsecolor, shadow
from wandplus.textutil import calcSuitableImagesize

# http://www.imagemagick.org/Usage/fonts/
# original imagemagick command:
#  convert -font Times-Bold -pointsize 64 \
#                     -background none  label:"Colorful Arc" \
#          \( +clone -sparse-color Barycentric '0,%h blue %w,0 red' \
#             \) -compose In -composite \
#          -virtual-pixel transparent -distort arc 120 \
#          \( +clone -background black -shadow 100x2+4+4 \
#             \) +swap -background white -compose over -layers merge +repage \
#          colorful_arc.jpg


text = 'Colorful Arc'
with Drawing() as draw:
    draw.font = 'Times-Bold'
    draw.font_size = 64
    (w, h) = calcSuitableImagesize(draw, text)

    # make gradient image(blue -> red)
    gradient = Image(width=w, height=h, background=Color('black'))
    channel = 'default_channels'  # see CHANNELS in 'wand/image.py'
    #                                              x  y  R    G    B    A
    sparsecolor(gradient, channel, 'barycentric', [0, h, 0.0, 0.0, 1.0, 1.0,
                                                   w, 0, 1.0, 0.0, 0.0, 1.0])

    # make text image
    textimg = Image(width=w, height=h)
    draw.gravity = 'center'
    draw.fill_color = Color('white')
    draw.text(0, 0, text)
    draw(textimg)

    # make text with gradient
    textimg.composite_channel(channel, gradient, 'in')

    # curve it
    textimg.distort('arc', [120], True)

    # add shadow
    shadowimg = textimg.clone()
    shadowimg.background_color = Color('black')
    shadow(shadowimg, 100, 2, 4, 4)

    # composite all
    canvas = Image(width=textimg.width, height=textimg.height,
                   background=Color('white'))
    canvas.composite(shadowimg, 0, 0)
    canvas.composite(textimg, 0, 0)
    canvas.save(filename='sample39.png')

    gradient.destroy()
    textimg.destroy()
    shadowimg.destroy()
    canvas.destroy()
