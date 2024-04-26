

import skimage.io as io
import imageio  # Use imageio for saving images
import os
import cv2
import matplotlib.pyplot as plt

save_path = os.getcwd()

img = io.imread("raw_file.mha", plugin='simpleitk')
if not os.path.exists(save_path):
    os.makedirs(save_path)
for i in range(len(img)):
    # Use imageio.imwrite to save the image
    imageio.imwrite(os.path.join(save_path, f'{i+1}.png'), img[i])
print(save_path)