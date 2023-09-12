import os
from PIL import Image

dir_path = os.getcwd()

for filename in os.listdir(dir_path):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        img = Image.open(filename)
        new_size = (1024, 576)
        img = img.resize(new_size)
        new_filename = os.path.splitext('weekly')[0] + '.webp'
        img.save(new_filename, 'webp', lossless=False, quality=80)
        os.remove(filename)
print('Готово!')
