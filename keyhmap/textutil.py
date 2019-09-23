#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : Prakash [प्रकाश]
# date   : 2019-09-22 18:02

import numpy as np

asc_map = [
    ['त्र', 'q'],
    ['त्त', 'Q'],
    ['क्ष', 'I'],
    ['श्र', '>'],
    ['ज्ञ', '!'],
    ['द्ध', '$'],
    ['क्', 'S'],
    ['ध्', 'W'],
    ['च्', 'R'],
    ['त्', 'T'],
    ['थ्', 'Y'],
    ['म्', 'D'],
    ['न्', 'G'],
    ['स्', ':'],
    ['श्', 'Z'],
    ['ह्', 'X'],
    ['ल्', 'N'], # Multi char end here
    ['०', '0'],
    ['१', '1'],
    ['२', '2'],
    ['३', '3'],
    ['४', '4'],
    ['५', '5'],
    ['६', '6'],
    ['७', '7'],
    ['८', '8'],
    ['९', '9'],
    ['ध', 'w'],
    ['भ', 'e'],
    ['च', 'r'],
    ['त', 't'],
    ['थ', 'y'],
    ['ग', 'u'],
    ['ष', 'i'],
    ['य', 'o'],
    ['उ', 'p'],
    ['ब', 'a'],
    ['क', 's'],
    ['म', 'd'],
    ['ा', 'f'],
    ['न', 'g'],
    ['ज', 'h'],
    ['व', 'j'],
    ['प', 'k'],
    ['ि', 'l'],
    ['श', 'z'],
    ['ह', 'x'],
    ['अ', 'c'],
    ['ख', 'v'],
    ['द', 'b'],
    ['ल', 'n'],
    ['आ','A'],
    ['ऐ', 'E'],
    ['ऊ', 'U'],
    ['इ', 'O'],
    ['ए', 'P'],
    ['ँ', 'F'],
    ['झ', 'H'],
    ['ो', 'J'],
    ['फ', 'K'],
    ['ी', 'L'],
    ['ऋ', 'C'],
    ['ॐ', 'V'],
    ['ौ', 'B'],
    ['ः', 'M'],
    ['ञ','`'],
    ['ई', '@'],
    ['घ', '#'],
    ['छ', '%'],
    ['ट', '^'],
    ['ठ', '&'],
    ['ड', '\u002a'], # Asterisk right there
    ['ढ', '('],
    ['ण', ')'],
    ['ओ', '_'],
    ['ं', '+'],
    ['।', '.'],
    ['्',"\u005c"], # That's backslash
    ['र', '/'],
    ['औ', '='],
    ['ृ', '['],
    ['ु', "'"],
    ['ू','"'],
    ['े', ']'],
    ['ै', '}'],
    ['ङ', '<'],
    ['स', ';']
]

uni_map = [[x[1],x[0]] for x in asc_map]


def re_transform(txt,trmap):
    tr_txt = txt
    for trule in trmap:
        tr_txt = tr_txt.replace(trule[0],trule[1])
    return tr_txt

def to_uni(asc_txt):
    return re_transform(asc_txt,uni_map)


def to_ascii(nep_txt):
    return re_transform(nep_txt,asc_map)


def get_frequencies(text,layout='qwerty'):
    if layout == 'bakamana':
        text = to_ascii(text)
    unique,count = np.unique([char for char in text],return_counts=True)
    return dict(zip(unique,count))
