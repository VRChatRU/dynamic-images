import os
from PIL import Image

dir_path = os.getcwd()

for filename in os.listdir(dir_path):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        sd_img = Image.open(filename)
        hd_img = Image.open(filename)
        sd_img = sd_img.resize(1024, 576)
        sd_filename = os.path.splitext('weekly')[0] + '.webp'
        hd_filename = os.path.splitext('weeklyHD')[0] + '.webp'
        sd_img.save(sd_filename, 'webp', lossless=False, quality=80)
        if hd_img.size[0] > 1920:
            hd_img = hd_img.resize(1920, 1080)
        hd_img.save(hd_filename, 'webp', lossless=True, quality=100)
        os.remove(filename)
print('Готово!')
