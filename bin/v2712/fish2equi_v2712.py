#!/usr/bin/env python2
"""
PANORAMA CONVERSION EXAMPLE SCRIPT FOR DANIEL MELANDER

Requires:
    Hugin (nona command line tool ) http://hugin.sourceforge.net/
    PIL for exif data reading (available from pypi)

"""

import os
import shlex
import subprocess

import PIL
from PIL import Image

# Conversion files can be downloaded from
# https://github.com/ultramango/gear360pano/blob/master/gear360sm-r210.pto
# https://github.com/ultramango/gear360pano/blob/master/gear360sm-c200.pto

EXIF_MODEL = 272
ABS_PATH = os.path.dirname(os.path.abspath(__file__))

PANORAMA_MODELS = {
    'SM-C200': ABS_PATH + '/Projection/gear360sm-c200.pto',
    'SM-R210': ABS_PATH + '/Projection/gear360sm-r210.pto',
}

def run(cmd, *args, **kwargs):
    params = shlex.split(cmd.format(*args, **kwargs))
    subprocess.call(params)

def project_panorama(target_path, panorama_projection):
    output = target_path.rpartition('.')[0]
    run("nona -m JPEG -z 93 -o {output} --seam blend {proj} {input} {input}",
            output=output,
            proj=panorama_projection,
            input=target_path,
        )
    # Override the old image and make it a .jpg
    os.rename(output+'.jpg', target_path)


def main():
    import sys
    import glob
    import numpy as np
    # Get the files to a list
    dir_path = sys.argv[1]
    files = glob.glob(dir_path+"*.JPG")
    files = files + glob.glob(dir_path+"*.jpg")
    # For each file
    for file in files:
        img = PIL.Image.open(file)
        exif = img._getexif()
        # Gets the corresponding projection format based on EXIF data
        panorama_projection = PANORAMA_MODELS.get(exif.get(EXIF_MODEL, None), None)
        project_panorama(file, panorama_projection)

if __name__ == "__main__":
    main()
