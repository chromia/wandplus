from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wandplus.image import autogamma, autolevel, blur, clut, shade, shadow
from wandplus.textutil import calcSuitableImagesize


# http://www.imagemagick.org/Usage/fonts/

# original turorial of chrome text by GIMP user group
# https://web.archive.org/web/20080315023524/http://gug.sunsite.dk/tutorials/tomcat16/
# more detailed description by Pete Trbovich
# http://penguinpetes.com/b2evo/index.php?p=351
# example of command-line code is by snibgo
# http://www.imagemagick.org/discourse-server/viewtopic.php?f=1&t=23904#p101702


# configuration
text = 'snibgo'
font = 'Arial-Black'
font_size = 160
maincolor = 'rgb(100%,100%,80%)'
# maincolor = 'rgb(255,255,204)'  # same as above
# maincolor = 'LightGoldenrodYellow'  # you can specify by color name
shadowcolor = 'rgb(0,0,75%)'


# const(don't change)
def_ch = 'default_channels'

# make CLUT table for metalic coloring
clut_width = 1
clut_height = 1000
clutimg = Image(filename='gradient:{0}-black'.format(maincolor),
                width=clut_width, height=clut_height)
clutimg.gamma(1.0)
with Image(filename='gradient:', width=clut_width, height=clut_height) as tmp:
    tmp.gamma(0.9)
    tmp.function('sinusoid', [2.25, 0.0, 0.5, 0.5])
    clutimg.composite_channel(def_ch, tmp, 'overlay')
clutimg.rotate(90)


# make text image
inputimg = None
with Drawing() as draw:
    draw.font = font
    draw.font_size = font_size
    (w, h) = calcSuitableImagesize(draw, text)
    inputimg = Image(width=w, height=h, background=Color('white'))
    draw.fill_color = Color('black')
    draw.gravity = 'center'
    draw.text(0, 0, text)
    draw(inputimg)
blur(inputimg, 0, 5)
inputimg.level(black=0.4, white=0.6)
blur(inputimg, 0, 3)
inputimg.alpha_channel = False


# start: making of matalic image
baseimg = Image(filename='gradient:rgb(100%,100%,100%)-black',
                width=inputimg.width, height=inputimg.height)

# 1.make masked text
with inputimg.clone() as tmp:
    tmp.negate()
    baseimg.composite_channel(def_ch, tmp, 'copy_opacity')
# baseimg.save(filename='sample41-1.png')

# 2.make bump map
with inputimg.clone() as tmp1:
    with inputimg.clone() as tmp2:
        tmp2.negate()
        tmp2.level(black=0.0, white=0.1)
        tmp1.composite_channel(def_ch, tmp2, 'copy_opacity')
    shade(tmp1, True, 315, 45)
    autogamma(tmp1)
    autolevel(tmp1)
    baseimg.composite_channel(def_ch, tmp1, 'overlay')
# baseimg.save(filename='sample41-2.png')

# 3.coloring
clut(baseimg, clutimg)
# baseimg.save(filename='sample41-3.png')

# 4.add shadow
metallicimg = baseimg.clone()
metallicimg.background_color = Color(shadowcolor)
shadow(metallicimg, 80, 2, 3, 3)
metallicimg.composite_channel(def_ch, baseimg, 'over')

# end:
metallicimg.save(filename='sample41.png')

# clean-up(as you like)
inputimg.destroy()
clutimg.destroy()
baseimg.destroy()
metallicimg.destroy()
