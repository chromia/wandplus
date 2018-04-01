#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/#arcs

w = 100
h = 60
bgcolor = Color('skyblue')

# original imagemagick command:
# Elliptical Arcs :   A  radius_x,y  angle   large,sweep  x,y
# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "path 'M 30,40  A 30,15 0 0,0 70,20'"    path_arc.gif

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.path_start()
        draw.path_move((30, 40))
        draw.path_elliptic_arc(radius=(30, 15), to=(70, 20))
        draw.path_finish()
        draw(img)
    img.save(filename='sample22a.png')

# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "path 'M 30,40  A 30,15 0 0,1 70,20'"    path_arc2.gif

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.path_start()
        draw.path_move((30, 40))
        draw.path_elliptic_arc(radius=(30, 15), to=(70, 20), clockwise=True)
        draw.path_finish()
        draw(img)
    img.save(filename='sample22b.png')

# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "path 'M 30,40  A 30,15 0 1,0 70,20'"    path_arc3.gif

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.path_start()
        draw.path_move((30, 40))
        draw.path_elliptic_arc(radius=(30, 15), to=(70, 20), large_arc=True)
        draw.path_finish()
        draw(img)
    img.save(filename='sample22c.png')

# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "path 'M 30,40  A 30,15 0 1,1 70,20'"    path_arc4.gif

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.path_start()
        draw.path_move((30, 40))
        draw.path_elliptic_arc(radius=(30, 15), to=(70, 20),
                               large_arc=True, clockwise=True)
        draw.path_finish()
        draw(img)
    img.save(filename='sample22d.png')

# Closed and angled elliptical arcs  (defined by two edge points)
# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "path 'M 30,40  A 30,20  20  0,0 70,20 Z '" path_arc5.gif

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.path_start()
        draw.path_move((30, 40))
        draw.path_elliptic_arc(radius=(30, 20), to=(70, 20), rotation=20)
        draw.path_close()
        draw.path_finish()
        draw(img)
    img.save(filename='sample22e.png')

# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "path 'M 30,40  A 30,20  20  1,1 70,20 Z '" path_arc6.gif

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.path_start()
        draw.path_move((30, 40))
        draw.path_elliptic_arc(radius=(30, 20), to=(70, 20), rotation=20,
                               large_arc=True, clockwise=True)
        draw.path_close()
        draw.path_finish()
        draw(img)
    img.save(filename='sample22f.png')

# convert -size 100x60 xc:skyblue -fill white -stroke black \
#         -draw "path 'M 30,40  A 30,20  20  0,0 70,20 \
#                               A 30,20  20  1,0 30,40 Z '" path_arc7.gif

with Image(width=w, height=h, background=bgcolor) as img:
    with Drawing() as draw:
        draw.fill_color = Color('white')
        draw.stroke_color = Color('black')
        draw.path_start()
        draw.path_move((30, 40))
        draw.path_elliptic_arc(radius=(30, 20), to=(70, 20), rotation=20)
        draw.path_elliptic_arc(radius=(30, 20), to=(30, 40), rotation=20,
                               large_arc=True)
        draw.path_close()
        draw.path_finish()
        draw(img)
    img.save(filename='sample22g.png')
