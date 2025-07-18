import PIL.Image as Image
import numpy as np

def load_array(filename):
    image = Image.open(f'images/snake_parts/{filename}.png')
    array = np.array(image)
    array = np.transpose(array, (2, 0, 1))
    array = np.delete(array, 3, 0)
    return array



def save_images(file_base_name):
    for mode in ['dark', 'light']:
        for direction in [['up', 'left'], ['left', 'down'], ['down', 'right'],]:
            src = Image.open(f'images/snake_parts/{file_base_name}_{direction[0]}_{mode}.png')
            src = src.rotate(90)
            src.save(f'images/snake_parts/{file_base_name}_{direction[1]}_{mode}.png')
save_images('lower_body')



