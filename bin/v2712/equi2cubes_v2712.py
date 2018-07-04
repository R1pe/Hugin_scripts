#!/usr/bin/env python2
"""
EQUIRECTANGULAR PROJECTION CONVERSION SCRIPT

Requires:
    Hugin (nona command line tool ) http://hugin.sourceforge.net/
    Panotools (http://search.cpan.org/~bpostle/Panotools-Script-0.25/)

Example usage:
    http://vinayhacks.blogspot.fi/2010/11/converting-equirectangular-panorama-to.html
Documentation .pto -file:
    http://hugin.sourceforge.net/docs/nona/nona.txt

"""

import os
import shlex
import subprocess
import sys
import glob
import shutil

def run(cmd, *args, **kwargs):
    params = shlex.split(cmd.format(*args, **kwargs))
    subprocess.call(params)


def project_panorama(target_path, panorama_projection):
    output = target_path.rpartition('/')[0] + "/cube_face"
    run("nona -o {output} {proj}",
            output=output,
            proj=panorama_projection
        )
    return [output+'0000.tif',
            output+'0001.tif',
            output+'0002.tif',
            output+'0003.tif',
            output+'0004.tif',
            output+'0005.tif'];


def ptoFileGenerate(target_path):
    output1 = target_path.rpartition('.')[0] + '.pto'
    output2 = output1.rpartition('/')[-1]
    run("erect2cubic --erect={input_img} --ptofile={pto_file}",
            input_img=target_path,
            pto_file=output2
        )
    pto_file = output1.rpartition('/')[-1]
    return pto_file

def tif2jpg_conversion(directory):
    run("convert {in_file} {out_file}",
            in_file = directory+'/*.tif',
            out_file = directory+'/cube_face.jpg'
        )
    for file in os.listdir(directory):
        if file.endswith(".tif"):
            os.remove(os.path.join(directory, file))

def createDirectoryForImage(image):
    directory_for_img = image.rpartition('.')[0]
    if not os.path.exists(directory_for_img):
        os.makedirs(directory_for_img)
    return directory_for_img

def main():
    path = sys.argv[1]
    files = glob.glob(path+"*.JPG")
    files = files + glob.glob(path+"*.jpg")
    for file in files:
        op_dir = createDirectoryForImage(file)
        destination = op_dir+'/'+file.rpartition('/')[-1]
        os.rename(file, destination)
        panorama_projection = ptoFileGenerate(destination);
        cube_face = project_panorama(destination, panorama_projection)
        os.remove(panorama_projection)
        os.remove(destination)
        tif2jpg_conversion(op_dir)

if __name__ == "__main__":
    main()
