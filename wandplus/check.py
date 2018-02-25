#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
import image as wpi
from textutil import calcSuitableFontsize, calcSuitableImagesize
import os
import unittest


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


class CheckImage(unittest.TestCase):

    def test_adaptiveblur(self):
        f = wpi.adaptiveblur
        with rose.clone() as t:
            f(t, 5.0, 3.0)
            save(t, f)
        with rose.clone() as t:
            f(t, 5.0, 3.0, channel='red')
            save(t, f, True)

    def test_adaptiveresize(self):
        f = wpi.adaptiveresize
        with rose.clone() as t:
            f(t, int(t.width*1.5), int(t.height*2.0))
            save(t, f)

    def test_adaptivesharpen(self):
        f = wpi.adaptivesharpen
        with rose.clone() as t:
            f(t, 5, 5)
            save(t, f)
        with rose.clone() as t:
            f(t, 5, 5, channel='red')
            save(t, f, True)

    def test_adaptivethreshold(self):
        f = wpi.adaptivethreshold
        with logo.clone() as t:
            f(t, 20, 20, int(0.1*t.quantum_range))
            save(t, f)

    def test_addnoise(self):
        f = wpi.addnoise
        with grad.clone() as t:
            f(t, 'gaussian')
            save(t, f)
        with grad.clone() as t:
            f(t, 'gaussian', channel='red')
            save(t, f, True)

    def test_affinetransform(self):
        f = wpi.affinetransform
        with rose.clone() as t:
            with Drawing() as d:
                d.affine([2.0, 0.0, 0.0, 2.0, 0.0, 0.0])
                f(t, d)  # not work correctly
                save(t, f)

    def test_autogamma(self):
        f = wpi.autogamma
        with rose.clone() as t:
            f(t)
            save(t, f)
        with rose.clone() as t:
            f(t, channel='red')
            save(t, f, True)

    def test_autolevel(self):
        f = wpi.autolevel
        with rose.clone() as t:
            f(t)
            save(t, f)
        with rose.clone() as t:
            f(t, channel='red')
            save(t, f, True)

    def test_blackthreshold(self):
        f = wpi.blackthreshold
        with grad.clone() as t:
            f(t, Color('gray(50%)'))
            save(t, f)

    def test_blueshift(self):
        f = wpi.blueshift
        with logo.clone() as t:
            f(t, 0.5)
            save(t, f)

    def test_brightnesscontrast(self):
        f = wpi.brightnesscontrast
        with rose.clone() as t:
            f(t, -30, 0)
            save(t, f)
        with rose.clone() as t:
            f(t, -30, 0, channel='red')
            save(t, f, True)

    def test_blur(self):
        f = wpi.blur
        with rose.clone() as t:
            f(t, 0, 3)
            save(t, f)
        with rose.clone() as t:
            f(t, 0, 3, channel='red')
            save(t, f, True)

    def test_charcoal(self):
        f = wpi.charcoal
        with rose.clone() as t:
            f(t, 5, 1)
            save(t, f)

    def test_chop(self):
        f = wpi.chop
        with grad.clone() as t:
            t.gravity = 'north_west'
            f(t, 0, 00, 200, 200)
            save(t, f)

    def test_clamp(self):
        f = wpi.clamp  # TODO: more useful code
        with rose.clone() as t:
            f(t)
            save(t, f)
        with rose.clone() as t:
            f(t, channel='red')
            save(t, f, True)

    def test_clip(self):
        f = wpi.clip
        with rose.clone() as t:
            f(t)
            save(t, f)

    def test_clut(self):
        f = wpi.clut
        with Image(filename='gradient:red-blue', width=1, height=100) as p:
            p.rotate(90)
            with grad.clone() as t:
                f(t, p)
                save(t, f)
            with grad.clone() as t:
                f(t, p, channel='green')
                save(t, f, True)

    def test_colordecisionlist(self):
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
        f = wpi.colordecisionlist
        with rose.clone() as t:
            f(t, xml)
            save(t, f)

    def test_colorize(self):
        f = wpi.colorize
        with grad.clone() as t:
            f(t, Color('red'), Color('gray(25%)'))
            save(t, f)

    def test_colormatrix(self):
        f = wpi.colormatrix
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

    def test_comment(self):
        f = wpi.comment
        with grad.clone() as t:
            f(t, 'hello')
            save(t, f)

    def test_constitute(self):
        f = wpi.constitute
        with Image() as t:
            w = 2
            h = 2
            b = b'\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\xFF\x00'
            f(t, w, h, 'RGB', 'char', b)
            save(t, f)

    def test_contrast(self):
        f = wpi.contrast
        with rose.clone() as t:
            f(t, False)
            save(t, f)

    def test_convolve(self):
        f = wpi.convolve
        kernel = [1/16, 2/16, 1/16,
                  2/16, 4/16, 2/16,
                  1/16, 2/16, 1/16]
        with rose.clone() as t:
            f(t, 3, kernel)
            save(t, f)
        with rose.clone() as t:
            f(t, 3, kernel, channel='red')
            save(t, f, True)

    def test_cyclecolormap(self):
        f = wpi.cyclecolormap
        with logo.clone() as t:
            f(t, 5)
            save(t, f)

    def test_cipher(self):
        f = wpi.encipher
        with rose.clone() as t:
            f(t, 'password')
            save(t, f)
            f = wpi.decipher
            f(t, 'password')
            save(t, f)

    def test_deskew(self):
        f = wpi.deskew
        with Image(width=80, height=40, background=Color('black')) as t:
            f(t, 0.5*t.quantum_range)  # TODO: find an skewed image as sample
            save(t, f)

    def test_despeckle(self):
        f = wpi.despeckle
        with rose.clone() as t:
            # TODO: add speckle noise
            f(t)
            save(t, f)

    def test_edge(self):
        f = wpi.edge
        with logo.clone() as t:
            f(t, 3)
            save(t, f)

    def test_emboss(self):
        f = wpi.emboss
        with logo.clone() as t:
            f(t, 0, 3)
            save(t, f)

    def test_enhance(self):
        f = wpi.enhance
        with Image(filename='plasma:', width=100, height=100) as t:
            f(t)
            save(t, f)

    def test_equalize(self):
        f = wpi.equalize
        with rose.clone() as t:
            f(t)
            save(t, f)
        with rose.clone() as t:
            f(t, channel='red')
            save(t, f, True)

    def test_extent(self):
        f = wpi.extent
        with rose.clone() as t:
            t.gravity = 'center'
            t.background_color = Color('blue')
            f(t, -10, -10, rose.width+20, rose.height+20)
            save(t, f)

    def test_filterimage(self):
        f = wpi.filterimage
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

    def test_floodfillpaint(self):
        f = wpi.floodfillpaint
        with logo.clone() as t:
            f(t, Color('green'), 0.10*t.quantum_range, Color('white'), 0, 0)
            save(t, f)

    def test_fft(self):
        f = wpi.forwardfouriertransform  # require IM build option '--with-fftw'
        with logo.clone() as t:      # I couldn't build on Windows...
            f(t, True)
            save(t, f)  # includes two images(magnitude&phase)
            f = wpi.inversefouriertransform
            with t.sequence[0].clone() as mag:
                with t.sequence[1].clone() as phase:
                    wpi.blur(mag, 0, 0.5)  # as degradation
                    t2 = mag
                    f(t2, phase, True)
                    save(t2, f)

    def test_haldclut(self):
        f = wpi.haldclut  # TODO: more useful code
        with Image(filename='hald:12') as p:
            with rose.clone() as t:
                f(t, p)
                save(t, f)
            with rose.clone() as t:
                f(t, p, channel='red')
                save(t, f, True)

    def test_implode(self):
        f = wpi.implode
        with rose.clone() as t:
            f(t, 1.0)
            save(t, f)

    def test_label(self):
        f = wpi.label
        with rose.clone() as t:
            f(t, 'hello')
            save(t, f)

    def test_localcontrast(self):
        f = wpi.localcontrast
        with logo.clone() as t:
            f(t, 5, 30)
            save(t, f)

    def test_magnify(self):
        f = wpi.magnify
        with rose.clone() as t:
            f(t)
            save(t, f)

    def test_minify(self):
        f = wpi.minify
        with rose.clone() as t:
            f(t)
            save(t, f)

    def test_montage(self):
        f = wpi.montage
        with rose.clone() as base:
            with Image() as dst:
                rows = 2
                columns = 3
                for i in range(rows * columns):
                    wpi.add(dst, base)

                tile = "{0}x{1}+0+0".format(columns, rows)
                thumb = "80x50+4+3"
                frame = "15x15+3+3"
                mode = "frame"
                with Drawing() as d:
                    with f(dst, d, tile, thumb, mode, frame) as result:
                        save(result, f)

    def test_morphology(self):
        f = wpi.morphology
        with logo.clone() as t:
            f(t, 'dilate', 1, 'Diamond')
            save(t, f)
        with logo.clone() as t:
            f(t, 'dilate', 1, 'Diamond', channel='red')
            save(t, f, True)

    def test_motionblur(self):
        f = wpi.motionblur
        with logo.clone() as t:
            f(t, 30, 10, 45)
            save(t, f)
        with logo.clone() as t:
            f(t, 30, 10, 45, channel='red')
            save(t, f, True)

    def test_oilpaint(self):
        f = wpi.oilpaint
        with rose.clone() as t:
            f(t, 2.0)
            save(t, f)

    def test_opaquepaint(self):
        f = wpi.opaquepaint
        with logo.clone() as t:
            f(t, Color('red'), Color('blue'), 1.0, False)
            save(t, f)
        with logo.clone() as t:
            f(t, Color('red'), Color('blue'), 1.0, False, channel='blue')
            save(t, f, True)

    def test_orderedposterize(self):
        f = wpi.orderedposterize
        with grad.clone() as t:
            f(t, 'o4x4,3,3')
            save(t, f)
        with grad.clone() as t:
            f(t, 'o4x4,3,3', channel='red')
            save(t, f, True)

    def test_polaroid(self):
        f = wpi.polaroid
        with logo.clone() as t:
            with Drawing() as d:
                f(t, d, 1.0)
                save(t, f)

    def test_posterize(self):
        f = wpi.posterize
        with rose.clone() as t:
            f(t, 3, True)
            save(t, f)

    def test_raiseimage(self):
        f = wpi.raiseimage
        with rose.clone() as t:
            f(t, 10, 10, 10, 10, True)
            save(t, f)

    def test_randomthreshold(self):
        f = wpi.randomthreshold
        with text_a.clone() as t:
            rng = t.quantum_range
            f(t, int(rng * 0.05), int(rng * 0.95))
            save(t, f)
        with text_a.clone() as t:
            rng = t.quantum_range
            f(t, int(rng * 0.05), int(rng * 0.95), channel='red')
            save(t, f, True)

    def test_remap(self):
        f = wpi.remap
        with logo.clone() as t:
            with rose.clone() as p:
                f(t, p, 'nodither')
                save(t, f)

    def test_resample(self):
        f = wpi.resample
        with rose.clone() as t:
            dpi = 72 * 2
            f(t, dpi, dpi, 'lanczos', 1.0)
            save(t, f)

    def test_roll(self):
        f = wpi.roll
        with rose.clone() as t:
            f(t, 10, 10)
            save(t, f)

    def test_rotationalblur(self):
        f = wpi.rotationalblur
        with rose.clone() as t:
            f(t, 45)
            save(t, f)
        with rose.clone() as t:
            f(t, 45, channel='red')
            save(t, f, True)

    def test_scale(self):
        f = wpi.scale
        with rose.clone() as t:
            f(t, t.width*2, t.height*2)
            save(t, f)

    def test_segment(self):
        f = wpi.segment
        with logo.clone() as t:
            f(t, 'rgb', False, 5, 20)
            save(t, f)

    def test_selectiveblur(self):
        f = wpi.selectiveblur
        with logo.clone() as t:
            f(t, 20, 20, 0.5*t.quantum_range)
            save(t, f)
        with logo.clone() as t:
            f(t, 20, 20, 0.5*t.quantum_range, channel='red')
            save(t, f, True)

    def test_separate_channel(self):
        f = wpi.separate_channel
        with rose.clone() as t:
            f(t, 'red')
            save(t, f)

    def test_sepiatone(self):
        f = wpi.sepiatone
        with rose.clone() as t:
            f(t, 0.5*t.quantum_range)
            save(t, f)

    def test_shade(self):
        f = wpi.shade
        with logo.clone() as t:
            f(t, True, 45, 135)
            save(t, f)

    def test_shadow(self):
        f = wpi.shadow
        with text.clone() as t:
            with text.clone() as p:
                p.negate()
                f(p, 100, 2, 10, 10)
                t.composite_channel('default_channels', p, 'overlay')
                save(t, f)

    def test_sharpen(self):
        f = wpi.sharpen
        with rose.clone() as t:
            f(t, 3, 3)
            save(t, f)
        with rose.clone() as t:
            f(t, 3, 3, channel='red')
            save(t, f, True)

    def test_shave(self):
        f = wpi.shave
        with logo.clone() as t:
            f(t, 100, 100)
            save(t, f)

    def test_shear(self):
        f = wpi.shear
        with grad.clone() as t:
            f(t, Color('red'), 0, 10)
            save(t, f)

    def test_sigmoidalcontrast(self):
        f = wpi.sigmoidalcontrast
        with rose.clone() as t:
            f(t, True, 3, 3)
            save(t, f)
        with rose.clone() as t:
            f(t, True, 3, 3, channel='red')
            save(t, f, True)

    def test_sketch(self):
        f = wpi.sketch
        with logo.clone() as t:
            f(t, 10, 10, 45)
            save(t, f)

    def test_solarize(self):
        f = wpi.solarize
        with rose.clone() as t:
            f(t, 0.4*t.quantum_range)
            save(t, f)
        with rose.clone() as t:
            f(t, 0.4*t.quantum_range, channel='red')
            save(t, f, True)

    def test_splice(self):
        f = wpi.splice
        with rose.clone() as t:
            t.gravity = 'center'
            f(t, t.width//2, t.height//2, 20, 20)
            save(t, f)

    def test_sparsecolor(self):
        f = wpi.sparsecolor
        with Image(width=100, height=100, background=Color('black')) as t:
            f(t, 'default_channels', 'bilinear',
              [0, 0,     1.0, 0.0, 0.0, 1.0,
               100, 100, 0.0, 1.0, 1.0, 1.0])
            save(t, f)

    def test_spread(self):
        f = wpi.spread
        with logo.clone() as t:
            f(t, 'bilinear', 20)
            save(t, f)

    def test_statistic(self):
        f = wpi.statistic
        with rose.clone() as t:
            f(t, 'gradient', 4, 4)
            save(t, f)
        with rose.clone() as t:
            f(t, 'gradient', 4, 4, channel='red')
            save(t, f, True)

    def test_stegano(self):
        f = wpi.stegano
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
                        wpi.setsizeoffset(q, w, h, offset)
                        q.read(filename='stegano:' + tmpfile)
                        save(q, f)
                except Exception:
                    raise
                finally:
                    os.remove(tmpfile)

    def test_stereo(self):
        f = wpi.stereo
        with rose.clone() as t:
            with rose.clone() as p:
                p.negate()
                with f(t, p) as q:
                    save(q, f)

    def test_swirl(self):
        f = wpi.swirl
        with rose.clone() as t:
            f(t, 180)
            save(t, f)

    def test_texture(self):
        f = wpi.texture
        with Image(width=300, height=200) as t:
            with rose.clone() as p:
                with f(t, p) as q:
                    save(q, f)

    def test_thumbnail(self):
        f = wpi.thumbnail
        with logo.clone() as t:
            f(t, 100, 100)
            save(t, f)

    def test_tint(self):
        f = wpi.tint
        with rose.clone() as t:
            f(t, Color('rgb'), Color('gray(25%)'))
            save(t, f)

    def test_vignette(self):
        f = wpi.vignette
        with logo.clone() as t:
            wpi.minify(t)
            t.background_color = Color('black')
            f(t, 0, 10, 20, 20)
            save(t, f)

    def test_wave(self):
        f = wpi.wave
        with grad.clone() as t:
            f(t, 40, 200)
            save(t, f)

    def test_whitethreshold(self):
        f = wpi.whitethreshold
        with grad.clone() as t:
            f(t, Color('gray(50%)'))
            save(t, f)


class CheckTextUtil(unittest.TestCase):

    def test_imagesize(self):
        with Drawing() as d:
            text = 'check'
            d.font = 'Arial'
            d.font_size = 36
            size = calcSuitableImagesize(d, text)
            print('calcSuitableImagesize: ', size)
            self.assertTrue(size[0] > 0 and size[1] > 0)

    def test_fontsize(self):
        w = 100
        h = 100
        with Drawing() as d:
            text = 'check'
            d.font = 'Arial'
            fontsize = calcSuitableFontsize(d, text, width=w)
            print('calcSuitableImagesize[W]: ', fontsize)
            self.assertTrue(fontsize > 0)
            fontsize = calcSuitableFontsize(d, text, height=h)
            print('calcSuitableImagesize[H]: ', fontsize)
            self.assertTrue(fontsize > 0)


if __name__ == '__main__':
    unittest.main()
