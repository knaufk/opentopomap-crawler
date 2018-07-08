#!/usr/bin/env python

import math
import sys
import subprocess
import urllib.request
import os
import click

def deg2num(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 2.0 ** zoom
  xtile = int((lon_deg + 180.0) / 360.0 * n)
  ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
  return (xtile, ytile)

def get_arg(name): 
    try:
        args = arguments.Args()
        return args.grouped[name].get(0)
    except KeyError as err:
        print(help())
        sys.exit()

def download_tiles(lat_min, lat_max, lon_min, lon_max, zoom, target):
    for lat_tile in range(lat_min, lat_max +1):
        for lon_tile in range(lon_min, lon_max +1):
            print("Downloading tile {}/{} x {}/{} to {}".format(lat_tile, lat_max, lon_tile, lon_max, target))
            urllib.request.urlretrieve("https://a.tile.opentopomap.org/{}/{}/{}.png".format(zoom, lat_tile, lon_tile), "{}/{}_{}_{}.png".format(target, zoom, lon_tile, lat_tile))

def reconstruct_map(lat_min, lat_max, zoom, tiles_dir, result):
    rows=lat_max - lat_min +1
    concatCommand="montage -limit thread 8 -limit memory 30000MB -mode concatenate -tile {}x {}/*.png {}".format(rows, tiles_dir,result)
    print("Running 'montage' command: '{}'".format(concatCommand))
    process = subprocess.Popen(concatCommand.split(), env=dict(os.environ, MAGICK_TEMPORARY_PATH=tiles_dir) , stdout=subprocess.PIPE)
    output, error = process.communicate()
    if error is not None:
        print(error)

def create(directory):
    print("Creating working_directory '{}'".format(directory))
    if not os.path.exists(directory):
        os.makedirs(directory)

def cleanup(directory):
    print("Removing working directory '{}'".format(directory))
    [os.remove(os.path.join(directory,f)) for f in os.listdir(directory) if f.endswith(".png")]
    os.rmdir(directory)


@click.command()
@click.option('--lon1', help='longitude of a corner', default=7.06451)
@click.option('--lon2', help='longitude of opposite corner', default=6.83993)
@click.option('--lat1', help='latitude of a corner', default=50.98210)
@click.option('--lat2', help='latitude of oppostite corner', default=50.90433)
@click.option('--zoom', help='map zoom level', default=14)
@click.option('--working_dir', help='working directory of the script', default='./tmp', type=click.Path())
@click.argument('output', default='map.png', type=click.Path(exists=False))
def getotm(lon1, lon2, lat1, lat2, zoom, working_dir, output):
    """Simple tool to download a rectangular map from https://opentopomap.org/."""
    
    lat1_tile, lon1_tile=deg2num(lat1, lon1, zoom)
    lat2_tile, lon2_tile=deg2num(lat2, lon2, zoom)

    lat_min = min(lat1_tile, lat2_tile)
    lat_max = max(lat1_tile, lat2_tile)
    lon_min = min(lon1_tile, lon2_tile)
    lon_max = max(lon1_tile, lon2_tile)

    create(working_dir)

    download_tiles(lat_min, lat_max, lon_min, lon_max, zoom, working_dir)
    reconstruct_map(lat_min, lat_max, zoom, working_dir, output)

    cleanup(working_dir)

if __name__ == '__main__':
    getotm()
