#!/usr/bin/env python

CopyRight = '''
/**************************************************************************
 *
 * Copyright 2010 VMware, Inc.
 * All Rights Reserved.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software and associated documentation files (the
 * "Software"), to deal in the Software without restriction, including
 * without limitation the rights to use, copy, modify, merge, publish,
 * distribute, sub license, and/or sell copies of the Software, and to
 * permit persons to whom the Software is furnished to do so, subject to
 * the following conditions:
 *
 * The above copyright notice and this permission notice (including the
 * next paragraph) shall be included in all copies or substantial portions
 * of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
 * OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.
 * IN NO EVENT SHALL VMWARE AND/OR ITS SUPPLIERS BE LIABLE FOR
 * ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
 * TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
 * SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 *
 **************************************************************************/

/**
 * @file
 * SRGB translation.
 *
 * @author Brian Paul <brianp@vmware.com>
 * @author Michal Krol <michal@vmware.com>
 * @author Jose Fonseca <jfonseca@vmware.com>
 */
'''


import math


def srgb_to_linear(x):
    if x <= 0.04045:
        return x / 12.92
    else:
        return math.pow((x + 0.055) / 1.055, 2.4)


def linear_to_srgb(x):
    if x >= 0.0031308:
        return 1.055 * math.pow(x, 0.41666) - 0.055
    else:
        return 12.92 * x

def generate_srgb_tables():
    print 'const float'
    print 'util_format_srgb_8unorm_to_linear_float_table[256] = {'
    for j in range(0, 256, 4):
        print '   ',
        for i in range(j, j + 4):
            print '%.7e,' % (srgb_to_linear(i / 255.0),),
        print
    print '};'
    print
    print 'const uint8_t'
    print 'util_format_srgb_to_linear_8unorm_table[256] = {'
    for j in range(0, 256, 16):
        print '   ',
        for i in range(j, j + 16):
            print '%3u,' % (int(srgb_to_linear(i / 255.0) * 255.0 + 0.5),),
        print
    print '};'
    print
    print 'const uint8_t'
    print 'util_format_linear_to_srgb_8unorm_table[256] = {'
    for j in range(0, 256, 16):
        print '   ',
        for i in range(j, j + 16):
            print '%3u,' % (int(linear_to_srgb(i / 255.0) * 255.0 + 0.5),),
        print
    print '};'
    print


def main():
    print '/* This file is autogenerated by u_format_srgb.py. Do not edit directly. */'
    print
    # This will print the copyright message on the top of this file
    print CopyRight.strip()
    print
    print '#include "u_format_srgb.h"'
    print
    generate_srgb_tables()    


if __name__ == '__main__':
    main()
