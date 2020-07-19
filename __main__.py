#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse as AP
import sys

import numpy
from PIL import Image

def parse_meta(lines):
    meta = str(lines[0][0])
    dims = [16, 16]
    colors = {}
    for line in lines:
        if line.startswith(meta + '!size'):
            dims = line.split(' ')[1:]
            assert len(dims) == 2, 'Error: image size should be two integers separated by space!'
        elif line.startswith(meta + '!'):
            character = line[2]
            color_hex = line[4:]
            colors[str(character)] = hex2rgba(color_hex)
    return {
        'meta': meta,
        'width': int(dims[0]),
        'height': int(dims[1]),
        'colors': colors
    }

def filter_meta_lines(lines, meta):
    return [line for line in lines if not line.startswith(meta['meta'])]

def convert(lines, meta):
    width = meta['width']
    height = meta['height']
    lines = [pad_strip(line, width) for line in lines]
    line = ''.join(lines)
    data = []
    for c in line:
        data.extend(convert_character(c, meta))
    expected = height * width * 4
    actual = len(data)
    assert expected == actual, f'Expected image of size {expected}={width}*{height}*4, but got {actual} bytes/characters!'
    return numpy.ndarray(shape=(height, width, 4),
        buffer=numpy.array(data, dtype='uint8'),
        dtype='uint8'
    )

def pad_strip(line, width):
    line = line.rstrip('\n')
    if len(line) < width:
        line = line + (' ' * (width - len(line)))
    return line

def convert_character(char, meta):
    colors = meta['colors']
    return colors.get(str(char), hex2rgba('FF00FFFF'))

def hex2rgba(hex):
    hex = hex.lstrip('#').upper()
    return [int(hex[i:i+2], 16) for i in [0, 2, 4, 6]]

def write_image(image_data, filename):
    img = Image.fromarray(image_data)
    img.save(filename)

def main(args):
    lines = []
    for line in sys.stdin:
        lines.append(line)
    meta = parse_meta(lines)
    lines = filter_meta_lines(lines, meta)
    image_data = convert(lines, meta)
    write_image(image_data, args.outfile)

if __name__ == "__main__":
    parser = AP.ArgumentParser(description="Text to 2D image converter.")
    parser.add_argument("-o", "--outfile",
                        type=str, default="stdin.png",
                        help="Output filename.")
    args = parser.parse_args()
    main(args)
