'''
    Usage: python scripts/seperate_images.py --image_dir <Image directory>
    Example: python scripts/seperate_images.py --image_dir all_images --new_dirs [no|0|False]
'''

import os
import os.path as P
import shutil
import glob
import argparse


def delete_IDD_images(root_dir):
    jpg_files = sorted(
        [P.join(root_dir, file) for file in os.listdir(root_dir) if file.endswith('.jpg')])

    for idx, file in enumerate(jpg_files):
        f = P.splitext(file)[0]
        name = f'{f}.xml'
        if not P.exists(name):
            os.remove(file)
        print(f"\r{idx} images processed.", end='')
    print()
    return None


def main():
    parser = argparse.ArgumentParser(
        description="Move images that don't have tags based on xml files")
    parser.add_argument('-i', '--image_dir', help="Root image dir")
    args = parser.parse_args()
    delete_IDD_images(args.image_dir)


if __name__ == "__main__":
    main()
