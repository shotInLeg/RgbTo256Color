#!/usr/bin/env python
# coding: utf8
import math

from argparse import ArgumentParser


COLOR_MAPPING = [
    (0, 0, 0),
    (128, 0, 0),
    (0, 128, 0),
    (128, 128, 0),
    (0, 0, 128),
    (128, 0, 128),
    (0, 128, 128),
    (192, 192, 192),
    (128, 128, 128),
    (255, 0, 0),
    (0, 255, 0),
    (255, 255, 0),
    (0, 0, 255),
    (255, 0, 255),
    (0, 255, 255),
    (255, 255, 255),
    (0, 0, 0),
    (0, 0, 95),
    (0, 0, 135),
    (0, 0, 175),
    (0, 0, 215),
    (0, 0, 255),
    (0, 95, 0),
    (0, 95, 95),
    (0, 95, 135),
    (0, 95, 175),
    (0, 95, 215),
    (0, 95, 255),
    (0, 135, 0),
    (0, 135, 95),
    (0, 135, 135),
    (0, 135, 175),
    (0, 135, 215),
    (0, 135, 255),
    (0, 175, 0),
    (0, 175, 95),
    (0, 175, 135),
    (0, 175, 175),
    (0, 175, 215),
    (0, 175, 255),
    (0, 215, 0),
    (0, 215, 95),
    (0, 215, 135),
    (0, 215, 175),
    (0, 215, 215),
    (0, 215, 255),
    (0, 255, 0),
    (0, 255, 95),
    (0, 255, 135),
    (0, 255, 175),
    (0, 255, 215),
    (0, 255, 255),
    (95, 0, 0),
    (95, 0, 95),
    (95, 0, 135),
    (95, 0, 175),
    (95, 0, 215),
    (95, 0, 255),
    (95, 95, 0),
    (95, 95, 95),
    (95, 95, 135),
    (95, 95, 175),
    (95, 95, 215),
    (95, 95, 255),
    (95, 135, 0),
    (95, 135, 95),
    (95, 135, 135),
    (95, 135, 175),
    (95, 135, 215),
    (95, 135, 255),
    (95, 175, 0),
    (95, 175, 95),
    (95, 175, 135),
    (95, 175, 175),
    (95, 175, 215),
    (95, 175, 255),
    (95, 215, 0),
    (95, 215, 95),
    (95, 215, 135),
    (95, 215, 175),
    (95, 215, 215),
    (95, 215, 255),
    (95, 255, 0),
    (95, 255, 95),
    (95, 255, 135),
    (95, 255, 175),
    (95, 255, 215),
    (95, 255, 255),
    (135, 0, 0),
    (135, 0, 95),
    (135, 0, 135),
    (135, 0, 175),
    (135, 0, 215),
    (135, 0, 255),
    (135, 95, 0),
    (135, 95, 95),
    (135, 95, 135),
    (135, 95, 175),
    (135, 95, 215),
    (135, 95, 255),
    (135, 135, 0),
    (135, 135, 95),
    (135, 135, 135),
    (135, 135, 175),
    (135, 135, 215),
    (135, 135, 255),
    (135, 175, 0),
    (135, 175, 95),
    (135, 175, 135),
    (135, 175, 175),
    (135, 175, 215),
    (135, 175, 255),
    (135, 215, 0),
    (135, 215, 95),
    (135, 215, 135),
    (135, 215, 175),
    (135, 215, 215),
    (135, 215, 255),
    (135, 255, 0),
    (135, 255, 95),
    (135, 255, 135),
    (135, 255, 175),
    (135, 255, 215),
    (135, 255, 255),
    (175, 0, 0),
    (175, 0, 95),
    (175, 0, 135),
    (175, 0, 175),
    (175, 0, 215),
    (175, 0, 255),
    (175, 95, 0),
    (175, 95, 95),
    (175, 95, 135),
    (175, 95, 175),
    (175, 95, 215),
    (175, 95, 255),
    (175, 135, 0),
    (175, 135, 95),
    (175, 135, 135),
    (175, 135, 175),
    (175, 135, 215),
    (175, 135, 255),
    (175, 175, 0),
    (175, 175, 95),
    (175, 175, 135),
    (175, 175, 175),
    (175, 175, 215),
    (175, 175, 255),
    (175, 215, 0),
    (175, 215, 95),
    (175, 215, 135),
    (175, 215, 175),
    (175, 215, 215),
    (175, 215, 255),
    (175, 255, 0),
    (175, 255, 95),
    (175, 255, 135),
    (175, 255, 175),
    (175, 255, 215),
    (175, 255, 255),
    (215, 0, 0),
    (215, 0, 95),
    (215, 0, 135),
    (215, 0, 175),
    (215, 0, 215),
    (215, 0, 255),
    (215, 95, 0),
    (215, 95, 95),
    (215, 95, 135),
    (215, 95, 175),
    (215, 95, 215),
    (215, 95, 255),
    (215, 135, 0),
    (215, 135, 95),
    (215, 135, 135),
    (215, 135, 175),
    (215, 135, 215),
    (215, 135, 255),
    (215, 175, 0),
    (215, 175, 95),
    (215, 175, 135),
    (215, 175, 175),
    (215, 175, 215),
    (215, 175, 255),
    (215, 215, 0),
    (215, 215, 95),
    (215, 215, 135),
    (215, 215, 175),
    (215, 215, 215),
    (215, 215, 255),
    (215, 255, 0),
    (215, 255, 95),
    (215, 255, 135),
    (215, 255, 175),
    (215, 255, 215),
    (215, 255, 255),
    (255, 0, 0),
    (255, 0, 95),
    (255, 0, 135),
    (255, 0, 175),
    (255, 0, 215),
    (255, 0, 255),
    (255, 95, 0),
    (255, 95, 95),
    (255, 95, 135),
    (255, 95, 175),
    (255, 95, 215),
    (255, 95, 255),
    (255, 135, 0),
    (255, 135, 95),
    (255, 135, 135),
    (255, 135, 175),
    (255, 135, 215),
    (255, 135, 255),
    (255, 175, 0),
    (255, 175, 95),
    (255, 175, 135),
    (255, 175, 175),
    (255, 175, 215),
    (255, 175, 255),
    (255, 215, 0),
    (255, 215, 95),
    (255, 215, 135),
    (255, 215, 175),
    (255, 215, 215),
    (255, 215, 255),
    (255, 255, 0),
    (255, 255, 95),
    (255, 255, 135),
    (255, 255, 175),
    (255, 255, 215),
    (255, 255, 255),
    (8, 8, 8),
    (18, 18, 18),
    (28, 28, 28),
    (38, 38, 38),
    (48, 48, 48),
    (58, 58, 58),
    (68, 68, 68),
    (78, 78, 78),
    (88, 88, 88),
    (98, 98, 98),
    (108, 108, 108),
    (118, 118, 118),
    (128, 128, 128),
    (138, 138, 138),
    (148, 148, 148),
    (158, 158, 158),
    (168, 168, 168),
    (178, 178, 178),
    (188, 188, 188),
    (198, 198, 198),
    (208, 208, 208),
    (218, 218, 218),
    (228, 228, 228),
    (238, 238, 238),
]


class EActions(object):
    CLOSEST_RGB_COLOR = 'closest_rgb_color'
    CLOSEST_256_COLOR = 'closest_256_color'
    TERM256_TO_RGB = 'term256_to_rgb'
    RGB_TO_TERM256 = 'rgb_to_term256'

    ALL = [CLOSEST_RGB_COLOR, CLOSEST_256_COLOR, TERM256_TO_RGB, RGB_TO_TERM256]


def hex_to_rgb(hex_color):
    value = hex_color[1:]
    rgb = []
    current = ''
    for i in range(len(value)):
        current += value[i]
        if (i + 1) % 2 == 0:
            rgb.append(int(current, 16))
            current = ''
    return tuple(rgb)


def rgb_to_hex(rgb_color):
    hex_color = '#'
    for x in rgb_color:
        hex_color += hex(x)[2:]
    return hex_color


def closest_rgb_color(rgb_color):
    best_dist, best_color = 10 * 10, None

    r1, g1, b1 = rgb_color
    for color in COLOR_MAPPING:
        r2, g2, b2 = color
        dist = math.sqrt(
            (r1 - r2) ** 2 
            + (g1 - g2) ** 2 
            + (b1 - b2) ** 2 
        )

        if best_dist > dist:
            best_dist, best_color = dist, color

    return best_color, rgb_to_hex(best_color)


def closest_256_color(rgb_color):
    best_color, _ = closest_rgb_color(rgb_color)
    term256 = COLOR_MAPPING.index(best_color)
    return term256


def term256_to_rgb(term256_color):
    if term256_color < 0 or term256_color > 255:
        raise ValueError('Term256 color must be 0..255')

    rgb_color = COLOR_MAPPING[term256_color]
    return rgb_color, rgb_to_hex(rgb_color)


def rgb_to_term256(rgb_color):
    try:
        term256 = COLOR_MAPPING.index(best_color)
        return term256
    except Exception:
        raise ValueError('RGB color must be from pallete')


def parse_cmd():
    def color_type(value):
        if ',' in value:
            return tuple(map(lambda x: int(x), value.split(',')))
        elif value.startswith('#'):
            return hex_to_rgb(value)
        return int(value)

    parser = ArgumentParser(description='Script to get closest color from the palette.')
    parser.add_argument('-a', '--action', type=str, required=True, choices=EActions.ALL,
                        help='Mode to get color.')
    parser.add_argument('-c', '--color', type=color_type, required=True,
                        help='Color RGB or 256term ("256,76,98" or "#ff54e1" or "13")')

    options = parser.parse_args()
    return options


def main():
    options = parse_cmd()

    result = None
    if options.action == EActions.CLOSEST_RGB_COLOR:
        result = closest_rgb_color(options.color)
    elif options.action == EActions.CLOSEST_256_COLOR:
        result = closest_256_color(options.color)
    elif options.action == EActions.RGB_TO_TERM256:
        result = rgb_to_term256(options.color)
    elif options.action == EActions.TERM256_TO_RGB:
        result = term256_to_rgb(options.color)

    print(result)


if __name__ == '__main__':
    main()
