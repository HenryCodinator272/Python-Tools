import PIL.Image as Image
import numpy as np
def load_array(filename):
    src = Image.open(f'images/snake_parts/{filename}.png')
    array = np.array(src)
    array = np.transpose(array, (2, 0, 1))
    array = np.delete(array, 3, 0)
    return array

