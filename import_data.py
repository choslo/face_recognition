from __future__ import print_function

import os
from shutil import copyfile

try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve
 
# full URLS:
# http://vision.ucsd.edu/datasets/yale_face_dataset_original/yalefaces.zip 

URLBASE = 'http://vision.ucsd.edu/datasets/yale_face_dataset_original/{}'
URLS = ['yalefaces.zip']
DATA = ['face_yale.zip']

def main(output_dir='data'):
    filenames = DATA
    full_urls = [URLBASE.format(url) for url in URLS]

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for url, filename in zip(full_urls, filenames):
        output_file = os.path.join(output_dir, filename)

        if os.path.exists(output_file):
            continue

        print("Downloading from {} ...".format(url))
        urlretrieve(url, filename=output_file)
        print("=> File saved as {}".format(output_file))


if __name__ == '__main__':
    main()