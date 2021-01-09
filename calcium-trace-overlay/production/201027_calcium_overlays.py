from PIL import Image
import os.path
from os import listdir
import argparse

# initalize command line argument parser
parser = argparse.ArgumentParser(description="Create trace overlay from calcium imaging microscope screenshot.")
parser.add_argument('path', type=str, help='path to target')
args = parser.parse_args()

def process_file(input, output):
# Creates overlay file
# - input (str): path to input file
# - output (str): path to output file

    try:
        # open file
        im = Image.open(input).convert("RGBA")

    except:
        print("There was an error opening the file" + input + " as an image")
    
    else:
        # load file parameters
        n = im.load()
        s = im.size

        # loop through every pixel in image
        for x in range(s[0]):
            for y in range(s[1]):

                # grab pixel color values 
                r,g,b,a = n[x,y]

                # make pixel transparent if on black/white scale
                if r == g and r == b:
                    n[x,y] = 0, 0, 0, 0
                
                # turn all overlays colors red
                # (remove if you want to keep colors or change this value to change overlay color)
                else:
                    n[x,y] = 255, 25, 25, 255

        # save image
        im.save(output, "PNG")

def pass_files(path):
# Work through all the files in a path
# - path (str): path of file/folder to work through

    # if path is a folder, work through all files there
    if os.path.isdir(path):
        for file in listdir(path):
            pass_files(path + "/" + file)

    # if path is a file, process that file
    elif os.path.isfile(path):
        process_file(path, os.path.splitext(path)[0] + '_cutout.png')

pass_files(args.path)
