#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from image import *
from textutil import calcSuitableFontsize, calcSuitableImagesize
import os


if __name__ != '__main__':
    import sys
    sys.exit(0)


def save(img, function, channel=False):
    if channel:
        path = 'image/' + function.__name__ + "_ch.png"
    else:
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

f = adaptiveblur
with rose.clone() as t:
    f(t, 5.0, 3.0)
    save(t, f)
with rose.clone() as t:
    f(t, 5.0, 3.0, channel='red')
    save(t, f, True)

f = adaptiveresize
with rose.clone() as t:
    f(t, int(t.width*1.5), int(t.height*2.0))
    save(t, f)

f = adaptivesharpen
with rose.clone() as t:
    f(t, 5, 5)
    save(t, f)
with rose.clone() as t:
    f(t, 5, 5, channel='red')
    save(t, f, True)

f = adaptivethreshold
with logo.clone() as t:
    f(t, 20, 20, int(0.1*t.quantum_range))
    save(t, f)

f = addnoise
with grad.clone() as t:
    f(t, 'gaussian')
    save(t, f)
with grad.clone() as t:
    f(t, 'gaussian', channel='red')
    save(t, f, True)

f = affinetransform
with rose.clone() as t:
    with Drawing() as d:
        d.affine([2.0, 0.0, 0.0, 2.0, 0.0, 0.0])
        f(t, d)  # not work correctly
        save(t, f)

f = autogamma
with rose.clone() as t:
    f(t)
    save(t, f)
with rose.clone() as t:
    f(t, channel='red')
    save(t, f, True)

f = autolevel
with rose.clone() as t:
    f(t)
    save(t, f)
with rose.clone() as t:
    f(t, channel='red')
    save(t, f, True)

f = blackthreshold
with grad.clone() as t:
    f(t, Color('gray(50%)'))
    save(t, f)

f = blueshift
with logo.clone() as t:
    f(t, 0.5)
    save(t, f)

f = brightnesscontrast
with rose.clone() as t:
    f(t, -30, 0)
    save(t, f)
with rose.clone() as t:
    f(t, -30, 0, channel='red')
    save(t, f, True)

f = blur
with rose.clone() as t:
    f(t, 0, 3)
    save(t, f)
with rose.clone() as t:
    f(t, 0, 3, channel='red')
    save(t, f, True)

f = charcoal
with rose.clone() as t:
    f(t, 5, 1)
    save(t, f)

f = chop
with grad.clone() as t:
    t.gravity = 'north_west'
    f(t, 0, 00, 200, 200)
    save(t, f)

f = clamp  # TODO: more useful code
with rose.clone() as t:
    f(t)
    save(t, f)
with rose.clone() as t:
    f(t, channel='red')
    save(t, f, True)

# f = clip
# with rose.clone() as t:
#     f(t)
#     save(t, f)


f = clut
with Image(filename='gradient:red-blue', width=1, height=100) as p:
    p.rotate(90)
    with grad.clone() as t:
        f(t, p)
        save(t, f)
    with grad.clone() as t:
        f(t, p, channel='green')
        save(t, f, True)

xml = """
<ColorCorrectionCollection xmlns="urn:ASC:CDL:v1.2">
    <ColorCorrection id="cc03345">
        <SOPNode>
            <Slope> 0.9 1.2 0.5 </Slope>
            <Offset> 0.4 -0.5 0.6 </Offset>
            <Power> 1.0 0.8 1.5 </Power>
        </SOPNode>
        <SATNode>
            <Saturation> 0.85 </Saturation>
        </SATNode>
    </ColorCorrection>
</ColorCorrectionCollection>
"""
f = colordecisionlist
with rose.clone() as t:
    f(t, xml)
    save(t, f)

f = colorize
with grad.clone() as t:
    f(t, Color('red'), Color('gray(25%)'))
    save(t, f)

f = colormatrix
with logo.clone() as t:
    kernel = [
        0.5, 0.0, 0.0, 0.0, 0.0,
        0.0, 1.5, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.5, 0.0, 0.0,
        0.0, 0.0, 0.0, 1.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 1.0
    ]
    f(t, 5, 5, kernel)
    save(t, f)

f = comment
with grad.clone() as t:
    f(t, 'hello')
    save(t, f)

f = constitute
with Image() as t:
    w = 2
    h = 2
    b = b'\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\xFF\x00'
    f(t, w, h, 'RGB', 'char', b)
    save(t, f)

f = contrast
with rose.clone() as t:
    f(t, False)
    save(t, f)

f = convolve
kernel = [1/16, 2/16, 1/16,
          2/16, 4/16, 2/16,
          1/16, 2/16, 1/16]
with rose.clone() as t:
    f(t, 3, kernel)
    save(t, f)
with rose.clone() as t:
    f(t, 3, kernel, channel='red')
    save(t, f, True)

f = cycle
with logo.clone() as t:
    f(t, 5)
    save(t, f)

with rose.clone() as t:
    encipher(t, 'password')
    decipher(t, 'password')
    save(t, decipher)

f = deskew
with Image(width=80, height=40, background=Color('black')) as t:
    f(t, 0.5*t.quantum_range)  # TODO: find an skewed image as sample
    save(t, f)

f = despeckle
with rose.clone() as t:
    # TODO: add speckle noise
    f(t)
    save(t, f)

f = edge
with logo.clone() as t:
    f(t, 3)
    save(t, f)

f = emboss
with logo.clone() as t:
    f(t, 0, 3)
    save(t, f)

f = enhance
with Image(filename='plasma:', width=100, height=100) as t:
    f(t)
    save(t, f)

f = equalize
with rose.clone() as t:
    f(t)
    save(t, f)
with rose.clone() as t:
    f(t, channel='red')
    save(t, f, True)

f = extent
with rose.clone() as t:
    t.gravity = 'center'
    t.background_color = Color('blue')
    f(t, -10, -10, rose.width+20, rose.height+20)
    save(t, f)

f = filterimage
kernel = [  # Sobel filter
    -1.0, 0.0, 1.0,
    -2.0, 0.0, 2.0,
    -1.0, 0.0, 1.0,
]
with rose.clone() as t:
    f(t, 3, 3, kernel)
    save(t, f)
with rose.clone() as t:
    f(t, 3, 3, kernel, channel='red')
    save(t, f, True)

f = floodfillpaint
with logo.clone() as t:
    f(t, Color('green'), 0.10*t.quantum_range, Color('white'), 0, 0)
    save(t, f)

f = haldclut  # TODO: more useful code
with Image(filename='hald:12') as p:
    with rose.clone() as t:
        f(t, p)
        save(t, f)
    with rose.clone() as t:
        f(t, p, channel='red')
        save(t, f, True)

f = implode
with rose.clone() as t:
    f(t, 1.0)
    save(t, f)

f = label
with rose.clone() as t:
    f(t, 'hello')
    save(t, f)

f = localcontrast
with logo.clone() as t:
    f(t, 5, 30)
    save(t, f)

f = magnify
with rose.clone() as t:
    f(t)
    save(t, f)

f = minify
with rose.clone() as t:
    f(t)
    save(t, f)

f = montage
with rose.clone() as base:
    with Image() as dst:
        rows = 2
        columns = 3
        for i in range(rows * columns):
            add(dst, base)

        tile = "{0}x{1}+0+0".format(columns, rows)
        thumb = "80x50+4+3"
        frame = "15x15+3+3"
        mode = "frame"
        with Drawing() as d:
            with f(dst, d, tile, thumb, mode, frame) as result:
                save(result, f)

f = morphology
with logo.clone() as t:
    f(t, 'dilate', 1, 'Diamond')
    save(t, f)
with logo.clone() as t:
    f(t, 'dilate', 1, 'Diamond', channel='red')
    save(t, f, True)

f = motionblur
with logo.clone() as t:
    f(t, 30, 10, 45)
    save(t, f)
with logo.clone() as t:
    f(t, 30, 10, 45, channel='red')
    save(t, f, True)

f = oilpaint
with rose.clone() as t:
    f(t, 2.0)
    save(t, f)

f = opaquepaint
with logo.clone() as t:
    f(t, Color('red'), Color('blue'), 1.0, False)
    save(t, f)
with logo.clone() as t:
    f(t, Color('red'), Color('blue'), 1.0, False, channel='blue')
    save(t, f, True)

f = orderedposterize
with grad.clone() as t:
    f(t, 'o4x4,3,3')
    save(t, f)
with grad.clone() as t:
    f(t, 'o4x4,3,3', channel='red')
    save(t, f, True)

f = polaroid
with logo.clone() as t:
    with Drawing() as d:
        f(t, d, 1.0)
        save(t, f)

f = posterize
with rose.clone() as t:
    f(t, 3, True)
    save(t, f)

f = raiseimage
with rose.clone() as t:
    f(t, 10, 10, 10, 10, True)
    save(t, f)

f = randomthreshold
rng = t.quantum_range
with text_a.clone() as t:
    f(t, int(rng * 0.05), int(rng * 0.95))
    save(t, f)
with text_a.clone() as t:
    f(t, int(rng * 0.05), int(rng * 0.95), channel='red')
    save(t, f, True)

f = remap
with logo.clone() as t:
    with rose.clone() as p:
        f(t, p, 'nodither')
        save(t, f)

f = resample
with rose.clone() as t:
    dpi = 72 * 2
    f(t, dpi, dpi, 'lanczos', 1.0)
    save(t, f)

f = roll
with rose.clone() as t:
    f(t, 10, 10)
    save(t, f)

f = rotationalblur
with rose.clone() as t:
    f(t, 45)
    save(t, f)
with rose.clone() as t:
    f(t, 45, channel='red')
    save(t, f, True)

f = scale
with rose.clone() as t:
    f(t, t.width*2, t.height*2)
    save(t, f)

f = segment
with logo.clone() as t:
    f(t, 'rgb', False, 5, 20)
    save(t, f)

f = selectiveblur
with logo.clone() as t:
    f(t, 20, 20, 0.5*t.quantum_range)
    save(t, f)
with logo.clone() as t:
    f(t, 20, 20, 0.5*t.quantum_range, channel='red')
    save(t, f, True)

f = separate_channel
with rose.clone() as t:
    f(t, 'red')
    save(t, f)

f = sepiatone
with rose.clone() as t:
    f(t, 0.5*t.quantum_range)
    save(t, f)

f = shade
with logo.clone() as t:
    f(t, True, 45, 135)
    save(t, f)

f = shadow
with text.clone() as t:
    with text.clone() as p:
        p.negate()
        f(p, 100, 2, 10, 10)
        t.composite_channel('default_channels', p, 'overlay')
        save(t, f)

f = sharpen
with rose.clone() as t:
    f(t, 3, 3)
    save(t, f)
with rose.clone() as t:
    f(t, 3, 3, channel='red')
    save(t, f, True)

f = sigmoidalcontrast
with rose.clone() as t:
    f(t, True, 3, 3)
    save(t, f)
with rose.clone() as t:
    f(t, True, 3, 3, channel='red')
    save(t, f, True)

f = sketch
with logo.clone() as t:
    f(t, 10, 10, 45)
    save(t, f)

f = solarize
with rose.clone() as t:
    f(t, 0.4*t.quantum_range)
    save(t, f)
with rose.clone() as t:
    f(t, 0.4*t.quantum_range, channel='red')
    save(t, f, True)

f = splice
with rose.clone() as t:
    t.gravity = 'center'
    f(t, t.width//2, t.height//2, 20, 20)
    save(t, f)

f = shave
with logo.clone() as t:
    f(t, 100, 100)
    save(t, f)

f = shear
with grad.clone() as t:
    f(t, Color('red'), 0, 10)
    save(t, f)

f = sparsecolor
with Image(width=100, height=100, background=Color('black')) as t:
    f(t, 'default_channels', 'bilinear',
      [0, 0,     1.0, 0.0, 0.0, 1.0,
       100, 100, 0.0, 1.0, 1.0, 1.0])
    save(t, f)

f = spread
with logo.clone() as t:
    f(t, 'bilinear', 20)
    save(t, f)

f = statistic
with rose.clone() as t:
    f(t, 'gradient', 4, 4)
    save(t, f)
with rose.clone() as t:
    f(t, 'gradient', 4, 4, channel='red')
    save(t, f, True)

f = stegano
with rose.clone() as t:
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

f = stereo
with rose.clone() as t:
    with rose.clone() as p:
        p.negate()
        with f(t, p) as q:
            save(q, f)

f = swirl
with rose.clone() as t:
    f(t, 180)
    save(t, f)

f = texture
with Image(width=300, height=200) as t:
    with rose.clone() as p:
        with f(t, p) as q:
            save(q, f)

f = thumbnail
with logo.clone() as t:
    f(t, 100, 100)
    save(t, f)

f = tint
with rose.clone() as t:
    f(t, Color('rgb'), Color('gray(25%)'))
    save(t, f)

f = vignette
with logo.clone() as t:
    r = t.quantum_range
    minify(t)
    t.background_color = Color('black')
    f(t, 0, 10, 20, 20)
    save(t, f)

f = wave
with grad.clone() as t:
    f(t, 40, 200)
    save(t, f)

f = whitethreshold
with grad.clone() as t:
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
