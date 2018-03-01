#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/#arcs

w = 100
h = 60
bgcolor = Color('skyblue')

# original imagemagick command:
#  convert -size 100x60 xc:skyblue -fill white -stroke black \
#          -draw "path 'M 30,40   A 3,2  45  0,0 70,20'" path_arc_x.gif

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.path_start()
        draw.path_move((30, 40))
        draw.path_elliptic_arc(radius=(3, 2), to=(70, 20), rotation=45)
        draw.path_finish()
        draw(img)
    img.save(filename='sample23a.png')

# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "path 'M 30,40   A 1,1  0  0,0 70,20'" path_hcircle.gif

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.path_start()
        draw.path_move((30, 40))
        draw.path_elliptic_arc(radius=(1, 1), to=(70, 20))
        draw.path_finish()
        draw(img)
    img.save(filename='sample23b.png')

# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "path 'M 30,40   A 1,1  0  0,0 70,20
#                                A 1,1  0  1,0 30,40  Z'" path_circle.gif

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.path_start()
        draw.path_move((30, 40))
        draw.path_elliptic_arc(radius=(1, 1), to=(70, 20))
        draw.path_elliptic_arc(radius=(1, 1), to=(30, 40), large_arc=True)
        draw.path_close()
        draw.path_finish()
        draw(img)
    img.save(filename='sample23c.png')

# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "path 'M 30,40   A 0,0  0  0,0 70,20'" path_arc_line.gif

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.path_start()
        draw.path_move((30, 40))
        draw.path_elliptic_arc(radius=(0, 0), to=(70, 20))
        draw.path_finish()
        draw(img)
    img.save(filename='sample23d.png')

# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "path 'M 30,40   A 50,50  0  0,0 70,20
#                                A 50,50  0  0,0 30,40  Z'" path_lens.gif

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.path_start()
        draw.path_move((30, 40))
        draw.path_elliptic_arc(radius=(50, 50), to=(70, 20))
        draw.path_elliptic_arc(radius=(50, 50), to=(30, 40))
        draw.path_finish()
        draw(img)
    img.save(filename='sample23e.png')

# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "path 'M 20,55  L 25,10  L 70,5 L 20,55 Z' "   triangle.gif

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        # use a designated function instead of path_* to write a smart code.
        draw.polygon([(25, 10), (70, 5), (20, 55)])
        draw(img)
    img.save(filename='sample23f.png')

# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "path 'M 20,55  A 100,100 0 0,0 25,10
#                               A 100,100 0 0,0 70,5
#                               A 100,100 0 0,0 20,55 Z' " triangle_curved.gif

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.path_start()
        draw.path_move((20, 55))
        draw.path_elliptic_arc(radius=(100, 100), to=(25, 10))
        draw.path_elliptic_arc(radius=(100, 100), to=(70, 5))
        draw.path_elliptic_arc(radius=(100, 100), to=(20, 55))
        draw.path_close()
        draw.path_finish()
        draw(img)
    img.save(filename='sample23g.png')

# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "path 'M 20,55  A 100,100 0 0,0 25,10
#                               A 100,100 0 0,1 70,5
#                               A 100,100 0 0,1 20,55 Z' " triangle_bulge.gif

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.path_start()
        draw.path_move((20, 55))
        draw.path_elliptic_arc(radius=(100, 100), to=(25, 10))
        draw.path_elliptic_arc(radius=(100, 100), to=(70, 5), clockwise=True)
        draw.path_elliptic_arc(radius=(100, 100), to=(20, 55), clockwise=True)
        draw.path_close()
        draw.path_finish()
        draw(img)
    img.save(filename='sample23h.png')
