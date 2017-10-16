import argparse
import os
import glob
from PIL import Image
import imagehash

def renameImages(path, new_name):
    """ Renames all images in 'path' to a specific pattern.
        
    Inputs:
        - path: path of the firectory with the images.
        - new_name: string with the new name pattern for all files.
        Example: if new_name='cat', all the images will be renamed to
        'cat_1', 'cat_2', 'cat_3', etc.
    """
    # Types of file accepted by tensorflow API
    types = ("*.jpg", "*.png")

    # Rename images
    idx = 1
    for tp in types:
        for fpath in glob.glob(os.path.join(path, tp)):
            os.rename(fpath, os.path.join(path, new_name + "_" + str(idx) + tp[1:]))
            idx += 1
            
if __name__ == "__main__":
    # Path of the images
    parser = argparse.ArgumentParser()
    parser.add_argument("imgs_dir", help="Directory with images")
    parser.add_argument("new_name", help="New name for images")
    args = parser.parse_args()
    renameImages(args.imgs_dir, args.new_name)