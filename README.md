# Wand+
Examples and Supplemental libraries for [Wand(Python binding of ImageMagick)](https://github.com/dahlia/wand)  
This repository includes:

- Supplemental Library('wandplus' module)
- Examples using Wand/Wand+

## wandplus module

- 70 over image filtering functions not included in Wand  
(blur, edge, emboss, filter, motionblur, posterize, sepiatone, and so on)
- Image conversion functions with Numpy
    - You can achieve cooperation with PyOpenCV, Pillow, etc.

## Examples

- Wand is good library. But there are few examples. So I translated only a small part of [ImageMagick command line examples](http://www.imagemagick.org/Usage/) to Python script

    - [./examples/text/](https://github.com/chromia/wandplus/tree/master/examples/text/): ["Text to Image Handling" examples](http://www.imagemagick.org/Usage/text/)
    - [./examples/fonteffects/](https://github.com/chromia/wandplus/tree/master/examples/fonteffects/): ["Compound Font Effects" examples](http://www.imagemagick.org/Usage/fonts/)
    - [./examples/drawing/](https://github.com/chromia/wandplus/tree/master/examples/drawing): ["Drawing" examples](http://www.imagemagick.org/Usage/draw/)

# Prerequisites

- [ImageMagick](http://imagemagick.org/script/index.php)(Version 6.x. not 7.x)
- [Wand](http://docs.wand-py.org/en/0.4.4/)(Version 0.4.4)

# License

Wand+ is released under MIT License(same as Wand).  
See ./LICENSE file
