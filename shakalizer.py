import os
from PIL import Image

dir_path = os.getcwd()

for filename in os.listdir(dir_path):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        sd_img = Image.open(filename)
        hd_img = Image.open(filename)
        sd_img_size=(1024, 576)
        hd_img_size=(1920, 1080)
        sd_img = sd_img.resize(sd_img_size)
        sd_filename = os.path.splitext('weekly')[0] + '.webp'
        hd_filename = os.path.splitext('weeklyHD')[0] + '.webp'
        sd_img.save(sd_filename, 'webp', lossless=False, quality=80)
        if hd_img.size[0] > 1920:
            hd_img = hd_img.resize(hd_img_size)
        hd_img.save(hd_filename, 'webp', lossless=False, quality=99)
        os.remove(filename)
print('Готово!')
