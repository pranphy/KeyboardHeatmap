#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : Prakash [प्रकाश]
# date   : 2019-09-22 17:37

import click


from kbhmap.heatmap import Heatmap

@click.command()

@click.option ('-i', '--input','infile',default=None, type=str,help='input file name')
@click.option ('-o', '--output','outfile',default=None, type=str, help='output file name')
@click.option ('-l', '--layout',default='qwerty',type=click.Choice(['qwerty','bakamana']),help='keyboard layout to use')
@click.option ('-s', '--sigma','sigma',default=3 ,type=float,help='sigma value to smoothen heatmap')
@click.option ('-c', '--cmap','cmap',default='YlGnBu' ,type=str,help='colormap to use')
@click.option ('-d', '--dpi','dpi',default=265 ,type=int,help='dpi of resulting image')

def  main(infile,outfile,layout,sigma,cmap,dpi):
    """
    a tool to generate the keyboard heatmap. It reads the text from 
    the input file and generates the heatmap. The heatmap can be configured. 
    The output heatmap image is saved in a file with name passed 
    as the `output` parameter. The smoothness of the heatmap
    can be controlld with `-s --sigma` option. The resolution
    of th output image can be set with `-d --dpi` parameter.

    """
    HM = Heatmap(layout)
    text = open(infile,'r').read()
    print(f'Processing {infile}.',end=' ')
    HM.make_heatmap(text,layout,sigmas=sigma,cmap=cmap)
    print('done')
    HM.save(outfile,dpi=dpi)


if __name__ == '__main__':
    main()
