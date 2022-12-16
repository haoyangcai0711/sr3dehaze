import os
import sys
from PIL import Image

path = "C:/Users/Haoyang Cai/Desktop/reside_tianze/haze_thumb/"
resized_path = "C:/Users/Haoyang Cai/Desktop/reside_tianze/haze_thumb_resized/"
os.mkdir(resized_path)

for f in os.listdir(path):
    im = Image.open(path + f)
    im_resize = im.resize((512, 512), Image.ANTIALIAS)
    f_no_ext, _ = os.path.splitext(f)
    im_resize.save(resized_path + f_no_ext + "_resized.png", 'PNG')