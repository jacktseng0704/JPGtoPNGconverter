import sys
import os
from PIL import Image

# run the code below in the command line
# python ./JPGtoPNGconverter.py ./Pokedex ./new
# what this basically do is
# 1. grab first and second argument and store in a variable
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# print(image_folder)
# print(output_folder)

# 2. check if new/ folder exists, if not create it
if not os.path.exists(output_folder):
    try:
        os.mkdir(output_folder)
    except OSError:
        print(f"Creation of the directory failed {output_folder}")
    else:
        print(f"Successfully created the directory {output_folder}")

# 3.loop through Pokedex, convert images to png
#   and save to the new folder.

# print(os.listdir(image_folder))

for filepath in os.listdir(image_folder):
    # print(f"{image_folder}\{filepath}")
    img = Image.open(f"{image_folder}\{filepath}")
    fname = os.path.splitext(filepath)[0]  # the same effect as filepath.split(".")[0]
    # print(img.filename) # prints the relative path of a file
    # print(filepath)  # prints the filename
    img.save(f"{output_folder}\{fname}.png", "png")
    print(f"Done creating {fname}.png")

