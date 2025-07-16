import numpy as np
import rasterio
import copy
import sys
import PIL.Image as Image
import pillow_avif
import time
import matplotlib.pyplot as plt
import random

def band_hex_separation(hex_list):
    final_list = []
    for i in hex_list:
        conversion = []
        for band in range(3):
            if band == 0:
                conversion.append(int(i[1:3], 16))
            if band == 1:
                conversion.append(int(i[3:5], 16))
            if band == 2:
                conversion.append(int (i[5:7], 16))
        final_list.append(conversion)
    return final_list

print(band_hex_separation(['#00FF41','#00E138','#00C330','#00A528', '#008720', '#000000']))

np.set_printoptions(threshold=np.inf, linewidth=512)

'''

sys.setrecursionlimit(10000) # Replace new_limit with a suitable integer

def recursive(changed_array, y, x, array, constant):
    if len(changed_array)>y>=0 and len(changed_array[y])>x>=0 and constant != 0:
        if changed_array[y][x] == constant:
            array.append((y+1, x+1))
            changed_array[y][x] = 0
            recursive(changed_array, y, x - 1, array, constant)
            recursive(changed_array, y + 1 , x, array, constant)
            recursive(changed_array, y - 1, x, array, constant)
            recursive(changed_array, y, x + 1, array, constant)
        else:
            pass


def island_counter(array):
    for row in array:
        print(row)
    print('')
    changed_array = copy.deepcopy(array)
    final_list=[]
    for y in range(len(array)):
        for x in range(len(array[y])):
            constant = array[y][x]
            temp_array = []
            recursive(changed_array, y, x, temp_array, constant)
            if len(temp_array) > 0:
                final_list.append(temp_array)
    return len(final_list)


'''


'''
file_path='../data/gt_post/mexico-earthquake_00000000_post_disaster_target.png'
with rasterio.open(file_path) as src:
    array=src.read().squeeze()
    print(array)
    array = (array*255/5).astype(np.uint8)
    img = Image.fromarray(array)

    img.save('../data/imagedata.png')

print(island_counter(array))
'''

(3, 1024, 1024)
'''
#with Image.open('../data/Henry_neon_trial.avif') as img:
    #img.save('../data/imagedata1.png')
with rasterio.open('../data/imagedata1.png') as src:
    array = src.read()
    #array = array.squeeze()
    for y in range(640):
        for x in range(640):
            if array[0][y][x] < 150:
                array[0][y][x] = 255
            else:
                array[0][y][x] = 0
            if 256 > array[1][y][x] > 180:
                array[1][y][x] = 255
            else:
                array[1][y][x] = 0
            if 0 < array[2][y][x] < 30:
                array[2][y][x] = 255
            else:
                array[2][y][x] = 0
            if not array[0][y][x] == array[1][y][x] == array[2][y][x] == 255:
                array[0][y][x], array[1][y][x], array[2][y][x] = 0, 0, 0


    #array[0] = np.where(array[0]<10, 255, 0).astype('uint8')
    #array[1] = np.where(190 > array[1] > 150, 255, 0).astype('uint8')
    #array[2] = np.where(80 > array[2] > 30, 255, 0).astype('uint8')
    #array[0] = np.where(array[0] == array[1] == array[2] == 255, 255, 0).astype('uint8')
    #array[1] = np.where(array[0] == array[1] == array[2] == 255, 255, 0).astype('uint8')
    #array[2] = np.where(array[0] == array[1] == array[2] == 255, 255, 0).astype('uint8')

    array = np.transpose(array, (1, 2, 0))
    print(np.shape(array))
    img = Image.fromarray(array, 'RGB')
    img.save('../data/imagedata2.png')

    print(np.shape(array))
'''
array = [[],128,128]
for i in range(3):
    array[i] = np.zeros((128,128), dtype=np.uint8)
#array = np.transpose(array, (1, 2, 0))
#img = Image.fromarray(array, 'RGB')
#img.save('../data/imagedata3.png')

#array = np.transpose(array, (2, 0, 1))

count = 0
def recursive_function(blob, ax = ''):
    plt.ion()
    bert = False
    global count
    global fig
    global im
    count += 1
    #time.sleep(2)
    hex_list = band_hex_separation(["#00FF00","#00CC00","#009900","#006600","#004400","#002200","#001100","#000000"])
    #print(hex_list)
    for band in range(3):
        for row in range(128):
            for col in range(128):
                if blob[band][row][col] == 254:
                    blob[band][row][col] = 0
    temp_array = copy.deepcopy(blob)
    list1 = []
    speed = []
    if np.random.randint(1,2) == 1:
        for number in range(np.random.randint(1, 2)): # make max higher for more strings
            list1.append(random.randrange(0, 128, 4)) #make step higher for more strings make sure its mod 4 tho
            speed.append(np.random.randint(7, 40)) #adjusts speed
        for stage in range(3):
            for x in list1:
                index = list1.index(x)
                for n in range(speed[index]):
                    temp_array[stage][n][x] = hex_list[0][stage]
                temp_array[stage][speed[index]][x] = 254
    #print(speed)
    for band in range(3):
        for row in range(128):
            for col in range(128):
                speed1 = 0
                row_temp = row
                if row < 127:
                    if blob[band][row][col] == hex_list[0][band] and blob[band][row+1][col] != hex_list[0][band]:
                        while row_temp >= 0 and blob[band][row_temp][col] == hex_list[0][band]:
                            speed1 += 1
                            row_temp -= 1
                    if blob[band][row][col] == hex_list[0][band] and blob[band][row+1][col] != hex_list[0][band] and row+1 < 128 - speed1:
                        for stage in range(speed1):
                            temp_array[band][row + stage + 1][col] = hex_list[0][band]
                        for w in range(3):
                            temp_array[w][row + speed1 + 1][col] = 254
                    if blob[band][row][col] == hex_list[0][band] and blob[band][row+1][col] != hex_list[0][band] and row+1 >= 128 - speed1:
                        for stage in range(128 - row):
                            temp_array[band][row + stage][col] = hex_list[0][band]
                if blob[band][row][col] > 0:
                    for stage in range(len(hex_list)):
                        if blob[band][row][col] == hex_list[stage][band]:
                            temp_array[band][row][col] = hex_list[stage + 1][band]


# check to see if you need to change it to white after everything

    #temp_array = np.transpose(temp_array, (1, 2, 0)).astype('uint8')
    #Image.fromarray(temp_array, 'RGB').save('../data/imagedata4.png')
    #temp_array = np.transpose(temp_array, (2, 0, 1)).astype('uint8')


    for row in range(128):
        for col in range(128):
            if temp_array[0][row][col] == 254:
                temp_array[1][row][col] = 254
                temp_array[2][row][col] = 254
            if 127 > row > 0 and temp_array[1][row][col] == 254 and temp_array[1][row-1][col] == hex_list[0][1] and temp_array[1][row+1][col] == hex_list[0][1]:
                for band in range(3):
                    temp_array[band][row][col] = hex_list[0][band]
            if row > 0 and temp_array[1][row][col] == 254 and temp_array[1][row-1][col] != hex_list[0][1]:
                temp_array[0][row][col] = temp_array[0][row-1][col]
                temp_array[1][row][col] = temp_array[1][row-1][col]
                temp_array[2][row][col] = temp_array[2][row-1][col]

    visual_array = np.transpose(temp_array, (1, 2, 0))

    odd_characters = '⅃ᗩ⅃Ƣ₳ØϗИᏴΔM₦Σ₥'

    if count == 1:
        fig, ax = plt.subplots()
        fig.patch.set_facecolor('black')
        im = ax.imshow(visual_array, alpha = 0)
        ax.axis('off')
        for row in range(128):
            for col in range(128):
                if col % 4 == 0 and row % 4 == 0:
                    if temp_array[1][row][col] != 0:
                        index = np.random.randint(0, 11)
                        plt.text(col, row, odd_characters[index], fontdict = { 'color' : (temp_array[0][row][col] / 255, temp_array[1][row][col] / 255, temp_array[2][row][col] / 255), 'fontsize' : 16 })

        plt.show()



    if count != 1:
        # Before drawing new frame
        for t in ax.texts:
            t.remove()

        for row in range(128):
            for col in range(128):
                if (col % 4 == 0 and row % 4 == 0) or temp_array[0][row][col] == 254:
                    if temp_array[1][row][col] != 0:
                        index = np.random.randint(0, 11)
                        plt.text(col, row, odd_characters[index], fontdict = { 'color' : (temp_array[0][row][col] / 255, temp_array[1][row][col] / 255, temp_array[2][row][col] / 255), 'fontsize' : 16 })
        im.set_data(visual_array)
        fig.canvas.draw()
        fig.canvas.flush_events()
    #temp_array = np.transpose(temp_array, (2, 0, 1)).astype('uint8')
    recursive_function(temp_array, ax=ax)
recursive_function(array)