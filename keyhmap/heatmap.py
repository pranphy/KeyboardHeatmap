#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : Prakash [प्रकाश]
# date   : 2019-09-22 17:40

import os

import numpy as np
import matplotlib.pyplot as plt

from . import textutil as utl

class  Heatmap():
    def __init__(self,layout='qwerty'):
        self.layout = layout
        self.key_map = self.__make_map()
        self.heatmap_array = np.zeros(shape=(20,60))
        self.curdir = os.path.dirname(os.path.abspath(__file__))


    def __make_map(self):
        # here is how the map works, I looked at the keyboard layout
        # The rectangular grid of keys are uneven but the uneven keys are 
        # non printable. Moss of the printable keys are even 
        # so I tried to represent the keys with a grid of numbers
        # Felt lazy to type now. Read the code below and figure it out.
        # so I start out with setting top left corner whichis 
        # the key `~ and s
        char_data = [
            [0,0,r'`~ 1! 2@ 3# 4$ 5% 6^ 7& 8* 9( 0) -_ =+'],
            [4,5,r'qQ wW eE rR tT yY uU iI oO pP [{ ]} \|'],
            [8,7,r'aA sS dD fF gG hH jJ kK lL ;: \'"'],
            [12,8,r'zZ xX cC vV bB nN mM ,< .> /?']
        ]

        char_map = {}
        width = 4
        height = 4
        for row in char_data:
            r,c = row[0],row[1]
            chars = row[2]
            for i,char in enumerate(chars.split(' ')):
                char_map[char] = ((r,c+ i*width), (r+height,c+ (i+1)*width))
        
        char_map[' '] = ((16,13),(20,47))
        char_map['\n'] = ((8,51),(12,60))
        char_map['lshift'] = ((12,0),(16,8))
        return char_map
    
    def get_cells(self,e):
        return [(r,c) for r in range(e[0][0],e[1][0]) for c in range(e[0][1],e[1][1])]
    
    def get_cells_for_char(self,char,ignore_other=True,verbose=False):
        try:
            char_map = self.key_map
            key = [x for x in char_map.keys() if char in x][0]
            cell_edges = char_map[key]
            
            cells = self.get_cells(cell_edges)
            if key.index(char) == 1:
                cells += self.get_cells(char_map['lshift'])
            return cells

        except Exception:
            if ignore_other:
                if verbose:
                    print(f'Warning:: `{char}` ignored')
                return []
            else:
                raise KeyError(f'{char} not found in the map')
    
    def __scale_char(self,key,factor=0.30):
        for r,c in self.get_cells(self.key_map[key]):
            self.heatmap_array[r][c] *= factor
        

    def __fill_heatmap(self,char_dict,ignore_other=True,verbose=False,normalize=True):
        for char,freq in char_dict.items():
            for r,c in self.get_cells_for_char(char,ignore_other,verbose):
                self.heatmap_array[r][c] += freq
        
        self.__scale_char('lshift')
        self.__scale_char(' ')
        if normalize:
            self.heatmap_array /= np.sum(self.heatmap_array)

    def make_heatmap(self,data,layout=None,ignore_other=True,verbose=False,alpha=0.8,sigmas=None,**kwargs):
        normalize = True
        layout = layout or self.layout
        if isinstance(data,dict):
            if layout == 'bakamana':
                data =  {utl.to_ascii(k):v for k,v in data.items()}
                
            self.__fill_heatmap(data,ignore_other,verbose,normalize)
        elif isinstance(data,str):
            char_dict = utl.get_frequencies(data,layout)
            self.__fill_heatmap(char_dict,ignore_other,verbose,normalize)
        else:
            print('Datatype not handled yet')
            raise Exception("Unknown datatype, can not make heatmap")
        if sigmas is not None:
            import scipy as sp
            import scipy.ndimage
            sigma = (sigmas,sigmas)
            self.heatmap_array = sp.ndimage.filters.gaussian_filter(self.heatmap_array,sigma,mode='constant')
        self.__make_plot(alpha,**kwargs)
    
    def __make_plot(self,alpha,**kwargs):
        fig, ax = plt.subplots()
        plt.xticks([])
        plt.yticks([])
        plt.axis('off')

        

        __ = ax.imshow(self.heatmap_array,interpolation='gaussian',zorder=1,alpha=alpha,**kwargs)
        
        img = plt.imread(f'{self.curdir}/images/keyboard_{self.layout}.png')

        __ = ax.imshow(img, zorder=0, extent=[0,59.3, 19.4, 0])
        self.heatmap_figure = fig
        
    def show(self):
        self.heatmap_figure.show()

    def save(self,op_filename=None,save_dir='.',dpi=265,**kwargs):
        op_filename = op_filename or f'heatmap_{self.layout}.png'
        op_path = os.path.join(save_dir,op_filename)
        
        self.heatmap_figure.savefig(
            op_path,
            dpi=dpi,
            pad_inches=0,
            transparent=True,
            bbox_inches='tight',
            **kwargs
        )
        print(f'{op_path} written.')

