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
text_a = Image(width=70, height=60)
with Drawing() as draw:
    draw.font = 'Arial'
    draw.font_size = 50
    draw.gravity = 'center'
    draw.fill_color = Color('white')
    draw.stroke_color = Color('black')
    draw.text(0, 0, 'A')
    draw(text_a)

rose.save(filename='image/rose.png')
grad.save(filename='image/grad.png')
logo.save(filename='image/logo.png')
text.save(filename='image/text.png')
text_a.save(filename='image/a.png')

with rose.clone() as t:
    f = adaptiveblur
    f(t, 5.0, 3.0)
    save(t, f)

with rose.clone() as t:
    f = adaptiveresize
    f(t, int(t.width*1.5), int(t.height*2.0))
    save(t, f)

with rose.clone() as t:
    f = adaptivesharpen
    f(t, 5, 5)
    save(t, f)

with logo.clone() as t:
    f = adaptivethreshold
    f(t, 20, 20, int(0.1*t.quantum_range))
    save(t, f)

with grad.clone() as t:
    f = addnoise
    f(t, 'gaussian')
    save(t, f)

with rose.clone() as t:
    f = affinetransform
    with Drawing() as d:
        d.affine([2.0, 0.0, 0.0, 2.0, 0.0, 0.0])
        f(t, d)  # not work correctly
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

with Image(filename='plasma:', width=100, height=100) as t:
    f = enhance
    f(t)
    save(t, f)

with rose.clone() as t:
    f = extent
    t.gravity = 'center'
    t.background_color = Color('blue')
    f(t, -10, -10, rose.width+20, rose.height+20)
    save(t, f)

with rose.clone() as t:
    f = haldclut
    with Image(filename='hald:12') as p:
        f(t, p)
        save(t, f)

with rose.clone() as t:
    f = implode
    f(t, 1.0)
    save(t, f)

with rose.clone() as t:
    f = label
    f(t, 'hello')
    save(t, f)

with rose.clone() as t:
    f = magnify
    f(t)
    save(t, f)

with rose.clone() as t:
    f = minify
    f(t)
    save(t, f)

with logo.clone() as t:
    f = morphology
    f(t, 'dilate', 1, 'Diamond')
    save(t, f)

with logo.clone() as t:
    f = motionblur
    f(t, 30, 10, 45)
    save(t, f)

with rose.clone() as t:
    f = oilpaint
    f(t, 2.0)
    save(t, f)

with logo.clone() as t:
    f = opaquepaint
    f(t, Color('red'), Color('blue'), 1.0, False)
    save(t, f)

with grad.clone() as t:
    f = orderedposterize
    f(t, 'o4x4,3,3')
    save(t, f)

with logo.clone() as t:
    f = polaroid
    with Drawing() as d:
        f(t, d, 1.0)
        save(t, f)

with rose.clone() as t:
    f = posterize
    f(t, 3, True)
    save(t, f)

with rose.clone() as t:
    f = raiseimage
    f(t, 10, 10, 10, 10, True)
    save(t, f)

with text_a.clone() as t:
    f = randomthreshold
    rng = t.quantum_range
    f(t, int(rng * 0.05), int(rng * 0.95))
    save(t, f)

with logo.clone() as t:
    with rose.clone() as p:
        f = remap
        f(t, p, 'nodither')
        save(t, f)

with rose.clone() as t:
    f = resample
    dpi = 72 * 2
    f(t, dpi, dpi, 'lanczos', 1.0)
    save(t, f)

with rose.clone() as t:
    f = roll
    f(t, 10, 10)
    save(t, f)

with rose.clone() as t:
    f = rotationalblur
    f(t, 45)
    save(t, f)

with rose.clone() as t:
    f = scale
    f(t, t.width*2, t.height*2)
    save(t, f)

with logo.clone() as t:
    f = segment
    f(t, 'rgb', False, 5, 20)
    save(t, f)

with logo.clone() as t:
    f = selectiveblur
    f(t, 20, 20, 0.5*t.quantum_range)
    save(t, f)

with rose.clone() as t:
    f = separate_channel
    f(t, 'red')
    save(t, f)

with rose.clone() as t:
    f = sepiatone
    f(t, 0.5*t.quantum_range)
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

with rose.clone() as t:
    f = sharpen
    f(t, 3, 3)
    save(t, f)

with rose.clone() as t:
    f = sigmoidalcontrast
    f(t, True, 3, 3)
    save(t, f)

with logo.clone() as t:
    f = sketch
    f(t, 10, 10, 45)
    save(t, f)

with rose.clone() as t:
    f = solarize
    f(t, 0.4*t.quantum_range)
    save(t, f)

with rose.clone() as t:
    f = splice
    t.gravity = 'center'
    f(t, t.width//2, t.height//2, 20, 20)
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

with rose.clone() as t:
    f = statistic
    f(t, 'gradient', 4, 4)
    save(t, f)

with rose.clone() as t:
    f = stegano
    w = 50
    h = 40
    offset = 15
    tmpfile = 'tmp.png'
    with Image(width=w, height=h, background=Color('white')) as p:
        with Drawing() as d:
            d.gravity = 'center'
            d.fill_color = Color('black')
            d.text(0, 0, 'Watch\nthe\nPidgeon')
            d(p)
        with f(t, p, offset) as q:
            q.save(filename=tmpfile)
        try:
            with Image() as q:
                setsizeoffset(q, w, h, offset)
                q.read(filename='stegano:' + tmpfile)
                save(q, f)
        except Exception:
            raise
        finally:
            os.remove(tmpfile)

with rose.clone() as t:
    f = stereo
    with rose.clone() as p:
        p.negate()
        with f(t, p) as q:
            save(q, f)

with rose.clone() as t:
    f = swirl
    f(t, 180)
    save(t, f)

with Image(width=300, height=200) as t:
    f = texture
    with rose.clone() as p:
        with f(t, p) as q:
            save(q, f)

with logo.clone() as t:
    f = thumbnail
    f(t, 100, 100)
    save(t, f)

with rose.clone() as t:
    f = tint
    f(t, Color('rgb'), Color('gray(25%)'))
    save(t, f)

with logo.clone() as t:
    f = vignette
    r = t.quantum_range
    minify(t)
    t.background_color = Color('black')
    f(t, 0, 10, 20, 20)
    save(t, f)

with grad.clone() as t:
    f = wave
    f(t, 40, 200)
    save(t, f)

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
