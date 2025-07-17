import numpy as np
import PIL.Image as Image
import os
import time
import keyboard
import matplotlib.pyplot as plt
from workplace import load_array

# this file will recreate google snake
'''
count = 0
display_array1 = np.zeros((128,128))
display_array = np.stack((display_array1, np.zeros((128,128))))
display_array = np.concatenate((display_array, np.zeros((1,128,128))), axis=0).astype(np.uint8)
'''
# Light Green Chunks RGB = (167, 217, 72)
# Dark Green Chunks RGB = (142, 204, 57)
# Darker Green Border RGB = (87, 138, 52)
bing = [0, 42, 72, 95, 113, 127, 139, 148, 156, 163, 170, 175, 180, 184, 187, 191, 194, 197, 199, 201, 204, 205, 207, 209, 211, 212, 213, 215, 216, 217, 218, 219, 220, 221, 222, 223, 223, 224, 225, 226, 226, 227, 227, 228, 228, 229, 230, 230, 230, 231, 231, 232, 232, 233, 233, 233, 234, 234, 234, 235, 235, 235, 235, 236, 236, 236, 237, 237, 237, 237, 238, 238, 238, 238, 238, 239, 239, 239, 239, 239, 240, 240, 240, 240, 240, 240, 240, 241, 241, 241, 241, 241, 241, 241, 242, 242, 242, 242, 242, 242, 242, 242, 243, 243, 243, 243, 243, 243, 243, 243, 243, 244, 244, 244, 244, 244, 244, 244, 244, 244, 244, 244, 244, 245, 245, 245, 245, 245, 245, 245, 245, 245, 245, 245, 245, 245, 245, 246, 246, 246, 246, 246, 246, 246, 246, 246, 246, 246, 246, 246, 246, 246, 246, 246, 246, 247, 247, 247, 247, 247, 247, 247, 247, 247, 247, 247, 247, 247, 247, 247, 247, 247, 247, 247, 247, 247, 247, 247, 248, 248, 248, 248, 248, 248, 248, 248, 248, 248, 248, 248, 248, 248, 248, 248, 248, 248, 248, 248, 248, 248, 248, 248, 248, 248, 248, 248, 248, 248, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 249, 250, 250, 250, 250, 250, 250]

#----------------------------------CANVAS---------------------------------------
def initial():

    display_array1 = np.zeros((128, 128))
    display_array = np.stack((display_array1, np.zeros((128, 128))))
    display_array = np.concatenate((display_array, np.zeros((1, 128, 128))), axis=0).astype(np.uint8)

    for band in range(len(display_array)):
        for row in range(len(display_array[band])):
            for col in range(len(display_array[band][row])):
                if 0 <= row < 4 or 0 <= col < 4 or  124 <= col < 128 or 124 <= row < 128: #if it's a border
                    if band == 0:
                        display_array[band][row][col] = 87
                    if band == 1:
                        display_array[band][row][col] = 138
                    if band == 2:
                        display_array[band][row][col] = 52
                elif int((row - 4) / 8) % 2 == int((col - 4) / 8) % 2: #if it's light green
                    if band == 0:
                        display_array[band][row][col] = 167
                    if band == 1:
                        display_array[band][row][col] = 217
                    if band == 2:
                        display_array[band][row][col] = 72
                else: #if it's dark green
                    if band == 0:
                        display_array[band][row][col] = 142
                    if band == 1:
                        display_array[band][row][col] = 204
                    if band == 2:
                        display_array[band][row][col] = 57

    return display_array
#------------------------------Initialization-----------------------------------
np.printoptions(linewidth = 512, threshold = 512)

data_array = np.zeros((15,15)).astype(np.uint8)
#print(data_array)

#------------------------------data array storage-------------------------------

dark_cherry = load_array('dark_cherry')
light_cherry = load_array('light_cherry')

snake_head_down_dark = load_array('snake_head_down_dark')
snake_head_right_dark = load_array('snake_head_right_dark')
snake_head_left_dark = load_array('snake_head_left_dark')
snake_head_up_dark = load_array('snake_head_up_dark')

snake_head_down_light = load_array('snake_head_down_light')
snake_head_right_light = load_array('snake_head_right_light')
snake_head_left_light = load_array('snake_head_left_light')
snake_head_up_light = load_array('snake_head_up_light')

snake_head2_down_dark = load_array('snake_head2_down_dark')
snake_head2_right_dark = load_array('snake_head2_right_dark')
snake_head2_left_dark = load_array('snake_head2_left_dark')
snake_head2_up_dark = load_array('snake_head2_up_dark')

snake_head2_down_light = load_array('snake_head2_down_light')
snake_head2_right_light = load_array('snake_head2_right_light')
snake_head2_left_light = load_array('snake_head2_left_light')
snake_head2_up_light = load_array('snake_head2_up_light')

upper_body_right_dark = load_array('upper_body_right_dark')
upper_body_up_dark = load_array('upper_body_up_dark')
upper_body_right_light = load_array('upper_body_right_light')
upper_body_up_light = load_array('upper_body_up_light')

upper_body_right_up_dark = load_array('upper_body_right_up_dark')
upper_body_right_down_dark = load_array('upper_body_right_down_dark')
upper_body_left_up_dark = load_array('upper_body_left_up_dark')
upper_body_left_down_dark = load_array('upper_body_left_down_dark')

upper_body_right_up_light = load_array('upper_body_right_up_light')
upper_body_right_down_light = load_array('upper_body_right_down_light')
upper_body_left_up_light = load_array('upper_body_left_up_light')
upper_body_left_down_light = load_array('upper_body_left_down_light')


#-------------------function that generates a random fruit-----------------------

def random_orb(array, data):
    if 5 in data: #if there's an orb in the smaller data array
        for row in range(len(data)):
            for col in range(len(data[row])):
                if data[row][col] == 5:
                    if row % 2 == col % 2: #if the orb is in a light green square
                        for i in range(3):
                            array[i][row * 8 + 4: row * 8 + 12, col * 8 + 4: col * 8 + 12] = light_cherry[i]
                    else: #if the orb is in a dark green square
                        for i in range(3):
                            array[i][row * 8 + 4: row * 8 + 12, col * 8 + 4: col * 8 + 12] = dark_cherry[i]
    else: #if there isn't an orb then we must make one
        row = np.random.randint(len(data))
        col = np.random.randint(len(data[row]))
        if data[row][col] == 0: #if it isn't part of the snake
            data[row, col] = 5
            if row % 2 == col % 2: #if the square is light green
                for i in range(3):
                    array[i][row * 8 + 4: row * 8 + 12, col * 8 + 4: col * 8 + 12] = light_cherry[i]
            else: #if the square is dark green
                for i in range(3):
                    array[i][row * 8 + 4: row * 8 + 12, col * 8 + 4: col * 8 + 12] = dark_cherry[i]
        else: #if it's part of the snake then it tries again
            random_orb(array, data)

#----------------------------main function---------------------------------------

def snake_motion(data, head_list = None, direction = [], apple = None, count = 0):
    array = initial()
    '''
    count += 1
    print(count)
    '''
    count += 1

    #time.sleep(0.05)

    start_time = time.perf_counter()


#-------------------------called when button is pressed---------------------------

    def direction1(event):
        key_name = event.name
        if key_name == 'up' and direction[0] != 'down':
            if direction[0] != 'up':
                direction.append('up')
                direction.pop(0)
        if key_name == 'down' and direction[0] != 'up':
            if direction[0] != 'down':
                direction.append('down')
                direction.pop(0)
        if key_name == 'left' and direction[0] != 'right':
            if direction[0] != 'left':
                direction.append('left')
                direction.pop(0)
        if key_name == 'right' and direction[0] != 'left':
            if direction[0] != 'right':
                direction.append('right')
                direction.pop(0)

    #------------------initializing----------------------

    random_orb(array, data)

    if head_list is None:
        random_orb(array, data)
        head_list = [[6, 2], [6, 1]]
        direction.append('right')

    #----------------directional input code-------------------
    keyboard.on_press_key('up', lambda e: direction1(e))
    keyboard.on_press_key('down', lambda f: direction1(f))
    keyboard.on_press_key('left', lambda g: direction1(g))
    keyboard.on_press_key('right', lambda h: direction1(h))

    #keyboard.wait('esc')

    #----------------deletes tail--------------------------

    data[head_list[-1][0]][head_list[-1][1]] = 0

    #------------------directional output code---------------------

    if direction[0] == 'right':
        if head_list[0][1] < 14:
            if data[head_list[0][0]][head_list[0][1] + 1] == 5:
                apple = True
            head_list.insert(0, [head_list[0][0], head_list[0][1] + 1])
            if apple is None:
                head_list.pop(-1)
            elif apple:
                data[head_list[1][0]][head_list[1][1] + 1] = 2
                random_orb(array, data)
        elif head_list[0][1] == 14:
            raise ValueError('You hit a wall! You lose!')

    if direction[0] == 'left':
        if head_list[0][1] > 0:
            if data[head_list[0][0]][head_list[0][1] - 1] == 5:
                apple = True
            head_list.insert(0, [head_list[0][0], head_list[0][1] - 1])
            if apple is None:
                head_list.pop(-1)
            elif apple:
                data[head_list[1][0]][head_list[1][1] - 1] = 2
                random_orb(array, data)
        elif head_list[0][1] == 0:
            raise ValueError('You hit a wall! You lose!')

    if direction[0] == 'up':
        if head_list[0][0] > 0:
            if data[head_list[0][0] - 1][head_list[0][1]] == 5:
                apple = True
            head_list.insert(0, [head_list[0][0] - 1, head_list[0][1]])
            if apple is None:
                head_list.pop(-1)
            elif apple:
                data[head_list[1][0] - 1, head_list[1][1]] = 2
                random_orb(array, data)
        elif head_list[0][0] == 0:
            raise ValueError('You hit a wall! You lose!')

    if direction[0] == 'down':
        if head_list[0][0] < 14:
            if data[head_list[0][0] + 1][head_list[0][1]] == 5:
                apple = True
            head_list.insert(0, [head_list[0][0] + 1, head_list[0][1]])
            if apple is None:
                head_list.pop(-1)
            elif apple:
                data[head_list[1][0] + 1][head_list[1][1]] = 2
                random_orb(array, data)
        elif head_list[0][0] == 14:
            raise ValueError('You hit a wall! You lose!')

    #--------------------updates tail in data array-----------------------

    if head_list.count(head_list[0]) == 2:
        raise ValueError('You crashed into yourself! You lose!')
    for coords in head_list:
        data[coords[0]][coords[1]] = 2

    #---------------------transcribes data array info to larger array for display-----------
    for number, coords in enumerate(head_list):
        row_snake = coords[0]
        col_snake = coords[1]
        if number == 0:
            if col_snake % 2 != row_snake % 2:
                for i in range(3):
                    if direction[0] == 'up':
                        array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = snake_head_up_dark[i]
                    if direction[0] == 'down':
                        array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = snake_head_down_dark[i]
                    if direction[0] == 'left':
                        array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = snake_head_left_dark[i]
                    if direction[0] == 'right':
                        array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = snake_head_right_dark[i]
            else:
                for i in range(3):
                    if direction[0] == 'up':
                        array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = snake_head_up_light[i]
                    if direction[0] == 'down':
                        array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = snake_head_down_light[i]
                    if direction[0] == 'left':
                        array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = snake_head_left_light[i]
                    if direction[0] == 'right':
                        array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = snake_head_right_light[i]
        elif number == 1:
            if col_snake % 2 != row_snake % 2:
                for i in range(3):
                    if direction[0] == 'up':
                        array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = \
                        snake_head2_up_dark[i]
                    if direction[0] == 'down':
                        array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = \
                        snake_head2_down_dark[i]
                    if direction[0] == 'left':
                        array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = \
                        snake_head2_left_dark[i]
                    if direction[0] == 'right':
                        array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = \
                        snake_head2_right_dark[i]
            else:
                for i in range(3):
                    if direction[0] == 'up':
                        array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = snake_head2_up_light[i]
                    if direction[0] == 'down':
                        array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = snake_head2_down_light[i]
                    if direction[0] == 'left':
                        array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = snake_head2_left_light[i]
                    if direction[0] == 'right':
                        array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = snake_head2_right_light[i]
        elif number <= (len(head_list) - 1) / 2:
            if col_snake % 2 != row_snake % 2:
                if head_list[number - 1][0] == head_list[number + 1][0]:
                    upper_body_right_dark[1] = np.where(upper_body_right_dark[1] == 204, 204, bing[number])
                    for i in range(3):
                            array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = \
                                upper_body_right_dark[i]
                elif head_list[number - 1][1] == head_list[number + 1][1]:
                    upper_body_up_dark[1] = np.where(upper_body_up_dark[1] == 204, 204, bing[number])
                    for i in range(3):
                        array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = \
                            upper_body_up_dark[i]
                elif head_list[number - 1][0] == head_list[number + 1][0] - 1 == head_list[number][0]:
                    upper_body_right_down_dark[1] = np.where(upper_body_right_down_dark[1] == 204, 204, bing[number])
                    for i in range(3):
                        array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = \
                            upper_body_right_down_dark[i]

            else:
                if head_list[number - 1][0] == head_list[number + 1][0]:
                    upper_body_right_light[1] = np.where(upper_body_right_light[1] == 217, 217, bing[number])
                    for i in range(3):
                            array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = \
                                upper_body_right_light[i]
                elif head_list[number - 1][1] == head_list[number + 1][1]:
                    upper_body_up_light[1] = np.where(upper_body_up_light[1] == 217, 217, bing[number])
                    for i in range(3):
                        array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = \
                            upper_body_up_light[i]

        else:
            for i in range(3):
                if i == 0:
                    array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = 157
                if i == 1:
                    array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = bing[number] #255 - 255/(number / 5 + 1)
                if i == 2:
                    array[i][row_snake * 8 + 4: row_snake * 8 + 12, col_snake * 8 + 4: col_snake * 8 + 12] = 255

        '''
        elif number == len(head_list) - 1:
        '''

    #-----------transposing for image processing---------------
    array = np.transpose(array, (1, 2, 0))


    fig, ax = plt.subplots()
    ax.axis('off')
    ax.imshow(array, interpolation = 'nearest')

    end_time = time.perf_counter()
    if 0.1 - (end_time - start_time) > 0:
        time.sleep(0.1 - (end_time - start_time))
    else:
        print(end_time - start_time, count)
    plt.show()
    #else:
        #im.set_data(array)
        #fig.canvas.draw()
        #fig.canvas.flush_events()

    image = Image.fromarray(array.astype(np.uint8))
    os.makedirs('images', exist_ok = True)
    image.save('images/test.png')
    #print(head_list)
    #-------------------------------------------------
    #print(f"\r{data}", end="", flush=True)
    #print(direction)
    #------------------------recursive to call next frame---------------------
    snake_motion(data = data, head_list = head_list, direction = direction, apple = None, count = count)


#random_orb(display_array, data_array)
#print(data_array)
snake_motion(data_array)
#---------------------------------TESTING---------------------------------------
#display_array = np.transpose(display_array, (1, 2, 0))
'''
image = Image.fromarray(display_array.astype(np.uint8))
os.makedirs('images', exist_ok=True)
image.save('images/test.png')
'''
#-------------------------------------------------------------------------------