import sys
import os
from PIL import Image


# grab first and secod argument:
image_folder = sys.argv[1]
output_folder = sys.argv[2]


# check if new/ exists, if not create it:
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# loop through pokadex, convert images to png files and save to new/:
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('All Done!')
