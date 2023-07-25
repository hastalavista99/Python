# the program below is used to create a gif
# the images files are keyed in on the command line and placed in an endless loop

import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[3]], duration=1500, loop=0
)
