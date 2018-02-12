from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from image import *
from textutil import calcSuitableFontsize, calcSuitableImagesize
import os


def save(img, function):
    path = 'image/' + function.__name__ + ".png"
    print(path)
    img.save(filename=path)


rose = Image(filename='rose:')
grad = Image(filename='gradient:', width=400, height=400)
logo = Image(filename='logo:')
text = Image(filename='label:Confirm', width=200, height=60)

rose.save(filename='image/rose.png')
grad.save(filename='image/grad.png')
logo.save(filename='image/logo.png')
text.save(filename='image/text.png')


with rose.clone() as t:
    f = adaptiveblur
    f(t, 5.0, 3.0)
    save(t, f)

with grad.clone() as t:
    f = addnoise
    f(t, 'gaussian')
    save(t, f)

with rose.clone() as t:
    f = autogamma
    f(t)
    save(t, f)

with rose.clone() as t:
    f = autolevel
    f(t)
    save(t, f)

with grad.clone() as t:
    f = blackthreshold
    f(t, Color('gray(50%)'))
    save(t, f)

with rose.clone() as t:
    f = brightnesscontrast
    f(t, -30, 0)
    save(t, f)

with rose.clone() as t:
    f = blur
    f(t, 0, 3)
    save(t, f)

with rose.clone() as t:
    f = charcoal
    f(t, 5, 1)
    save(t, f)

with grad.clone() as t:
    f = chop
    t.gravity = 'north_west'
    f(t, 0, 00, 200, 200)
    save(t, f)

with grad.clone() as t:
    f = clut
    with Image(filename='gradient:red-blue', width=1, height=100) as p:
        p.rotate(90)
        f(t, p)
        save(t, f)

with grad.clone() as t:
    f = colorize
    f(t, Color('red'), Color('gray(25%)'))
    save(t, f)

with grad.clone() as t:
    f = comment
    f(t, 'hello')
    save(t, f)

with rose.clone() as t:
    f = contrast
    f(t, False)
    save(t, f)

with rose.clone() as t:
    f = convolve
    k = [1/16, 2/16, 1/16,
         2/16, 4/16, 2/16,
         1/16, 2/16, 1/16]
    f(t, 3, k)
    save(t, f)

with logo.clone() as t:
    f = cycle
    f(t, 5)
    save(t, f)

with rose.clone() as t:
    f = despeckle
    # TODO: add speckle noise
    f(t)
    save(t, f)

with logo.clone() as t:
    f = edge
    f(t, 3)
    save(t, f)

with logo.clone() as t:
    f = emboss
    f(t, 0, 3)
    save(t, f)

with logo.clone() as t:
    f = morphology
    f(t, 'dilate', 1, 'Diamond')
    save(t, f)

with logo.clone() as t:
    f = motionblur
    f(t, 30, 10, 45)
    save(t, f)

with logo.clone() as t:
    f = shade
    f(t, True, 45, 135)
    save(t, f)

with text.clone() as t:
    with text.clone() as p:
        f = shadow
        p.negate()
        f(p, 100, 2, 10, 10)
        t.composite_channel('default_channels', p, 'overlay')
        save(t, f)

with logo.clone() as t:
    f = shave
    f(t, 100, 100)
    save(t, f)

with grad.clone() as t:
    f = shear
    f(t, Color('red'), 0, 10)
    save(t, f)

with Image(width=100, height=100, background=Color('black')) as t:
    f = sparsecolor
    f(t, 'default_channels', 'bilinear',
      [0, 0,     1.0, 0.0, 0.0, 1.0,
       100, 100, 0.0, 1.0, 1.0, 1.0])
    save(t, f)

with logo.clone() as t:
    f = spread
    f(t, 'bilinear', 20)
    save(t, f)

with grad.clone() as t:
    f = wave
    f(t, 40, 200)
    save(t ,f)

with grad.clone() as t:
    f = whitethreshold
    f(t, Color('gray(50%)'))
    save(t, f)

with Drawing() as d:
    text = 'check'
    d.font = 'Arial'
    d.font_size = 36
    size = calcSuitableImagesize(d, text)
    print('calcSuitableImagesize: ', size)

with Image(width=100, height=100) as t:
    with Drawing() as d:
        text = 'check'
        d.font = 'Arial'
        fontsize = calcSuitableFontsize(d, text, width=100)
        print('calcSuitableImagesize[W]: ', fontsize)
        fontsize = calcSuitableFontsize(d, text, height=100)
        print('calcSuitableImagesize[H]: ', fontsize)
