#!/usr/bin/env python2
"""
TRASFORMAS 6 CUBIC PROJECTIONS TO EQUIRECTANGULAR PROJECTION

Requires:
    Hugin (nona command line tool ) http://hugin.sourceforge.net/
    Panotools (http://search.cpan.org/~bpostle/Panotools-Script-0.25/)

Example usage:
    http://vinayhacks.blogspot.fi/2010/11/converting-equirectangular-panorama-to.html

"""

import os
import shlex
import subprocess
import sys
import glob

def run(cmd, *args, **kwargs):
    params = shlex.split(cmd.format(*args, **kwargs))
    subprocess.call(params)


def project_equirectangular(cube_faces):
    op_dir = cube_faces[0].rpartition('/')[0]
    print('op_dir: ' + op_dir)
    op_file = op_dir + '/final_erect.tif'
    print('op_file: ' + op_file)
    run("cubic2erect {front} {right} {back} {left} {up} {down} {output}",
            right=cube_faces[0],
            up=cube_faces[1],
            back=cube_faces[2],
            down=cube_faces[3],
            front=cube_faces[4],
            left=cube_faces[5],
            output=op_file
        )
    run("convert " + op_file + " " + op_file.rpartition('.')[0]+".jpg")
    os.remove(op_file)

def main():
    directory = sys.argv[1]
    print('directory: ' + directory)
    all_dirs = glob.glob(directory+'/*/')
    print('all_dirs: ' + str(all_dirs))
    for folder in all_dirs:
        folder = glob.glob(folder+'/*.jpg')
        print('files: ' + str(folder))
        print(folder[0])
        print(folder[1])
        print(folder[2])
        print(folder[3])
        print(folder[4])
        print(folder[5])
        project_equirectangular(folder)

if __name__ == "__main__":
    main()
