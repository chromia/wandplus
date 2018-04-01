#!/usr/bin/env python

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# http://www.imagemagick.org/Usage/draw/#arcs
# original imagemagick command:
# curve="M 12,27  C 7,37  18,50 18,60  S  0,80 10,94
#        S 40,74 50,78  S 60,99 76,95  S 72,70 75,65
#        S 95,55 95,42  S 69,37 66,32  S 67,2  53,7
#        S 43,17 35,22  S 17,17 12,27  Z"
# c_ctrls=`echo $curve | \
#            sed '1s/\([0-9]\)  *\([0-9]\)/\1 M \2/;
#                 s/S/M/g; s/C/ /;' -`
# convert -size 100x100 xc:white \
#         -draw "stroke None  fill Green  path '$curve'" \
#         -draw "stroke Red   fill None   path '$c_ctrls'" \
#         curvy_splash.gif

commands = [
    'M', (12, 27), 'C', (7, 37), (18, 50), (18, 60), 'S', (0, 80), (10, 94),
    'S', (40, 74), (50, 78), 'S', (60, 99), (76, 95), 'S', (72, 70), (75, 65),
    'S', (95, 55), (95, 42), 'S', (69, 37), (66, 32), 'S', (67, 2), (53, 7),
    'S', (43, 17), (35, 22), 'S', (17, 17), (12, 27), 'Z'
]
controls = [
    'M', (12, 27), (7, 37), 'M', (18, 50), (18, 60), 'M', (0, 80), (10, 94),
    'M', (40, 74), (50, 78), 'M', (60, 99), (76, 95), 'M', (72, 70), (75, 65),
    'M', (95, 55), (95, 42), 'M', (69, 37), (66, 32), 'M', (67, 2), (53, 7),
    'M', (43, 17), (35, 22), 'M', (17, 17), (12, 27), 'Z'
]


def draw_commands(draw, commands):
    cmd_list = []
    index = 0
    while index < len(commands):
        cmdtype = commands[index]
        cmdpoints = []
        if not isinstance(cmdtype, str):
            raise TypeError('expected a string not', type(cmdtype))
        index = index + 1
        while index < len(commands) and isinstance(commands[index], tuple):
            cmdpoints.append(commands[index])
            index = index + 1
        cmd_list.append((cmdtype, cmdpoints))
    for (cmdtype, cmdpoints) in cmd_list:
        if cmdtype == 'M':
            draw.path_move(cmdpoints[0])
            for point in cmdpoints[1:]:
                draw.path_line(point)
        elif cmdtype == 'C':
            draw.path_curve(controls=cmdpoints[:-1], to=cmdpoints[-1])
        elif cmdtype == 'L':
            for point in cmdpoints:
                draw.path_line(point)
        elif cmdtype == 'S':
            assert(len(cmdpoints) == 2)
            draw.path_curve(smooth=True, controls=cmdpoints[0],
                            to=cmdpoints[1])
        elif cmdtype == 'Z':
            draw.path_close()
        else:
            raise ValueError('this type is not supported', cmdtype)


with Image(width=100, height=100, background=Color('white')) as img:
    with Drawing() as draw:
        draw.stroke_color = Color('none')
        draw.fill_color = Color('green')
        draw.path_start()
        draw_commands(draw, commands)
        draw.path_finish()

        draw.stroke_color = Color('red')
        draw.fill_color = Color('none')
        draw.path_start()
        draw_commands(draw, controls)
        draw.path_finish()
        draw(img)
    img.save(filename='sample26.png')
