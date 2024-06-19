import os
from PIL import Image

dir_path = os.getcwd()

for filename in os.listdir(dir_path):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        img = Image.open(filename)
        img.resize(1024, 576).save(os.path.splitext('weekly')[0] + '.webp', 'webp', lossless=False, quality=80)
        if img.size.height[0] > 1920:
            img.resize(1920, 1080).save(os.path.splitext('weeklyHD')[0] + '.webp', 'webp', lossless=False, quality=100)
        else:
            img.save(os.path.splitext('weeklyHD')[0] + '.webp', 'webp', lossless=False, quality=80)
        os.remove(filename)
print('Готово!')
