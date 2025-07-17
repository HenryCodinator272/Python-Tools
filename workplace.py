import PIL.Image as Image
import numpy as np

def load_array(filename):
    src = Image.open(f'images/snake_parts/{filename}.png')
    array = np.array(src)
    array = np.transpose(array, (2, 0, 1))
    array = np.delete(array, 3, 0)
    return array

src = Image.open('images/snake_parts/snake_head_down_light.png')
src = src.rotate(90)
src.save('images/snake_parts/snake_head_right_light.png')



