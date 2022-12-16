import os
import sys
from PIL import Image

root = "C:/Users/Haoyang Cai/Desktop/RESIDE-beta/"
os.mkdir(root + "processed_hazy/")
os.mkdir(root + "processed_clear/")

count = 10000
for f in os.listdir(root + "hazy"):
    f_no_ext, _ = os.path.splitext(f)
    im_args = f_no_ext.split('_')
    haze_density = float(im_args[-1])
    index = im_args[0]
    if haze_density >= 0.1:
        im_hazy = Image.open(root + "hazy/" + f)
        im_hazy_resize = im_hazy.resize((512, 512), Image.ANTIALIAS)
        im_hazy_resize.save(root + "processed_hazy/" + str(count) + ".png", 'PNG')

        im_clear = Image.open(root + "clear/" + index + ".jpg")
        im_clear_resize = im_clear.resize((512, 512), Image.ANTIALIAS)
        im_clear_resize.save(root + "processed_clear/" + str(count) + ".png", "PNG")

        count += 1