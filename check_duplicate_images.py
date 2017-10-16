import argparse
import collections
import os
import glob
import shutil
from PIL import Image
import imagehash

def checkDuplicates(path, path_test=None):
    """Checks if there are duplicate images in the directory 'path'
    and if any, moves the duplicates to a different folder.
    
    Additionally, a second directory 'path_test' can be added to
    check for duplicates there too.
    
    Inputs:
        - path: path of the firectory with the images.
        - path_test: (OPTIONAL) a second path with more images to check.
    """
    # Types of file accepted by tensorflow API
    types = ("*.jpg", "*.png")
    # Initialize dictionary of hashes
    hashes = collections.defaultdict(list)
    # Initialize list of duplicate images
    duplicates = []
    
    # Save hashes of images
    for tp in types:
        for fpath in glob.glob(os.path.join(path, tp)):
            h = imagehash.average_hash(Image.open(fpath))
            hashes[h].append(fpath)
            
    # Add hashes of path_test if flag is not none
    if path_test is not None:
        for tp in types:
            for fpath in glob.glob(os.path.join(path_test, tp)):
                h = imagehash.average_hash(Image.open(fpath))
                hashes[h].append(fpath)
    
    # Check if duplicates
    for h, fpaths in hashes.items():
        if len(fpaths) > 1:
            duplicates.append(fpaths[1:])
            
    # Save parent directory
    path_par = os.path.abspath(os.path.join(path, os.pardir))
    
    # Create folder (if it doesn't exist) to save duplicates 
    path_dup = os.path.join(path_par, "images_dup")
    if not os.path.exists(path_dup):
        os.makedirs(path_dup)
    
    # Move duplicates images from images to images_dup
    for d in duplicates:
        shutil.move(d[0], path_dup)

    if len(duplicates) == 0:
        print("A total of {} duplicate images was found.".format(len(duplicates)))
    else:
        print("A total of {} duplicate images was found. \n \
              List of duplicate images: \n ".format(len(duplicates)))
        print(duplicates)

if __name__ == "__main__":
    # Path of the images
    parser = argparse.ArgumentParser()
    parser.add_argument("train_imgs_dir", help="Directory with train images")
    parser.add_argument("test_imgs_dir", nargs="?", help="Directory with test images")
    args = parser.parse_args()
    checkDuplicates(args.train_imgs_dir, args.test_imgs_dir)





    