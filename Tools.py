import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
import copy
import time






#with open('./README.md','w') as f:
    #f.write('I created this repository to make tools that are useful for other projects. \n It\'s also where im teaching myself a lot of python packages.')

def longest_palindrome_finder(str):
    palindrome_size = 1
    start = 0
    for j in range(len(str)):
        for p in range(len(str)):
            n = p
            i = j
            if str[i] == str[n] and n - i + 1 > palindrome_size:
                lower_index = i
                substr_size = n - i + 1
                while str[i] == str[n]:
                    # print(f'{i},{n}')
                    if lower_index == n:
                        palindrome_size = substr_size
                        # print(size)
                        start = lower_index
                    i += 1
                    n -= 1
                    if i >= len(str) or n < 0:
                        break
    return start, start + palindrome_size - 1, str[start:start + palindrome_size]

'''
Island
Counter 👹👹👹
'''



def island_counter(array):
    def recursive(changed_array, y, x, array, constant):
        if len(changed_array) > y >= 0 and len(changed_array[y]) > x >= 0 and constant != 0:
            if changed_array[y][x] == constant:
                array.append((y + 1, x + 1))
                changed_array[y][x] = 0
                recursive(changed_array, y, x - 1, array, constant)
                recursive(changed_array, y + 1, x, array, constant)
                recursive(changed_array, y - 1, x, array, constant)
                recursive(changed_array, y, x + 1, array, constant)
        else:
            pass
    for row in array:
        print(row)
    print('')
    changed_array = copy.deepcopy(array)
    final_list = []
    for y in range(len(array)):
        for x in range(len(array[y])):
            constant = array[y][x]
            temp_array = []
            recursive(changed_array, y, x, temp_array, constant)
            if len(temp_array) > 0:
                final_list.append(temp_array)
    return len(final_list), final_list


# print(island_counter([[0,1,0,1,1],[0,1,1,1,1],[1,0,0,0,0],[1,0,0,1,1,1,1,1,0,1, 2, 2]]))

'''
Base
Conversion 👹👹👹
'''

def base_conversion(base, number, count=1, lister=[]):
    if number > 0:
        checker = 1
        base_size = 1
        while number >= base * checker:
            checker *= base
            base_size += 1
        digit = 0
        while number >= (digit + 1) * checker:
            digit += 1
        number -= digit * checker
        if count == 1:
            lister = []
            for i in range(base_size):
                lister.append(0)
        lister[base_size - 1] = digit
        return base_conversion(base=base, number=number, count=2, lister=lister)

    elif number == 0 and count == 2:
        string = ''
        for i in range(len(lister)):
            string = f'{string}{lister[len(lister) - (i + 1)]}'
        return string
    elif number == 0 and count == 1:
        return '0'

'''
Math
24 and above
calculator 👹👹👹
'''

def challenge(string, target):
    string = str(string)
    list_base4 = []
    operations = len(string) - 1
    for i in range(4 ** operations):
        append = base_conversion(4, i)[-operations:]
        while len(append) < operations:
            append = f'0{append}'
        list_base4.append(append)
    string1 = ''
    for i in string:
        string1 = f'{string1}{i}-'
    string1 = string1.rstrip('-')
    # print(string1)
    # print(list_base4)
    yay_list = []
    for trial in list_base4:
        trial = str(trial)
        string1 = list(string1)
        try:
            for index in range(operations):
                # print(index)
                if trial[index] == '0':
                    string1[2 * index + 1] = '+'
                if trial[index] == '1':
                    string1[2 * index + 1] = '-'
                if trial[index] == '2':
                    string1[2 * index + 1] = '*'
                if trial[index] == '3':
                    string1[2 * index + 1] = '/'
            string1 = ''.join(string1)
            if eval(string1) == target:
                print(f'{string1}: {eval(string1)}')
                yay_list.append((string1))
        except ZeroDivisionError:
            pass
        finally:
            pass
    return yay_list


# challenge(806, 14)

'''
WIP
Clock 👹👹👹
'''


def clock_function(start=0, start_list=[0, 0, 0, 0]):
    time.sleep(1)
    ball = start
    ball += 1
    array_list = [[[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
                  [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
                  [[1, 1, 1], [0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 1]],
                  [[1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
                  [[1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]],
                  [[1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
                  [[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1]],
                  [[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
                  [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]],
                  [[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]]]
    main_array = np.zeros((7, 19)).astype('uint8')
    info_list = [1, 5, 11, 15]
    if start == 0:
        for index in info_list:
            for row in range(5):
                for col in range(3):
                    main_array[1 + row][index + col] = int(array_list[0][row][col])
    list_time = start_list
    #print(list_time)
    for i in range(4):
        number = list_time[i]
        index = info_list[i]
        for row in range(5):
            for col in range(3):
                main_array[1 + row][index + col] = int(array_list[number][row][col])
    main_array[2][9], main_array[4][9] = 1, 1
    if list_time[3] != 9:
        list_time[3] += 1
    elif list_time[3] == 9 and list_time[2] != 5:
        list_time[2], list_time[3] = list_time[2] + 1, 0
    elif list_time[3] == 9 and list_time[2] == 5 and list_time[1] != 9:
        list_time[1] += 1
        list_time[2], list_time[3] = 0, 0
    elif list_time[3] == 9 and list_time[2] == 5 and list_time[1] == 9 and list_time[0] != 5:
        list_time[0] += 1
        list_time[1], list_time[2], list_time[3] = 0, 0, 0
    elif list_time[3] == 9 and list_time[2] == 5 and list_time[1] == 9 and list_time[0] == 5:
        list_time[0], list_time[1], list_time[2], list_time[3] = 0, 0, 0, 0

    main_array = np.where(main_array == 0, 255, 0)
    #print(main_array)
    img = Image.fromarray(main_array.astype('uint8'))
    img.save('images/test1.png')
    #print(main_array)
    # time.sleep(1)
    if ball < 2000:
        clock_function(start=ball, start_list=list_time)


#clock_function()
'''
Working
Eval
Function() 👹👹👹
'''

def answer(expression):
    def is_float(test):
        try:
            float(test)
            return True
        except Exception:
            return False
        finally:
            pass
    def found(character, string):
        array = list(string)
        for n in array:
            if character == n:
                return True
        return False
    if isinstance(expression, list):
        transcribe = list(expression)
    if isinstance(expression, str):
        add = ''
        c = 0
        transcribe = []
        for n in range(len(expression)):
            if expression[n].isdigit() or expression[n] == '.':
                add = f'{add}{expression[n]}'
                c = 1
            elif c == 1:
                transcribe.append(add)
                transcribe.append(expression[n])
                add = ''
                c = 0
            else:
                transcribe.append(expression[n])
            if expression[n].isdigit() and n == len(expression) - 1:
                transcribe.append(add)
    absolute_occurrences = int(transcribe.count('|')) / 2
    count1 = 0
    index1 = -1
    # print(transcribe)
    while count1 < absolute_occurrences:
        index1 = transcribe.index('|', index1 + 1)
        index2 = transcribe.index('|', index1 + 1)
        count1 += 1
    if int(absolute_occurrences):
        val = answer(transcribe[index1 + 1:index2])
        if float(val) < 0:
            val = float(val)
            val *= -1
        transcribe[index1] = val
        for i in range(index2 - index1):
            transcribe.pop(index1 + 1)
        print(transcribe)
    c = 0
    while transcribe.count(' ') > 0:
        transcribe.remove(' ')
    print(transcribe)
    while int(transcribe.count('(')) or int(transcribe.count(')')):
        parentheses = []
        for n in range(len(transcribe)):
            if transcribe[n] == '(' or transcribe[n] == ')':
                parentheses.append(n)
        if int(len(parentheses)):
            for i in range(len(parentheses)):
                if (i + 1) < len(parentheses):
                    if transcribe[parentheses[i]] == '(' and transcribe[parentheses[i + 1]] == ')':
                        val = answer(transcribe[parentheses[i] + 1:parentheses[i + 1]])
                        for w in range(parentheses[i], parentheses[i + 1] + 1):
                            transcribe.pop(parentheses[i])
                        transcribe.insert(parentheses[i], val)
                        print(transcribe)
                        break
    if isinstance(transcribe, list):
        len1 = len(transcribe)
        for n in range(len1):
            if n > 0 and is_float(transcribe[len1 - n - 1]) and is_float(transcribe[len1 - n]):
                transcribe.insert(len1 - n, '*')
                print(transcribe)
    length = len(transcribe)
    for index in range(length):
        if index > 0 and is_float(transcribe[(length - 1) - index]) and transcribe[(length - 1) - index + 1] == '(':
            transcribe.insert(length - index, '*')
            print(transcribe)
        if index > 0 and transcribe[length - index - 1] == ')' and is_float(transcribe[length - index]):
            transcribe.insert(length - index, '*')
            print(transcribe)

    ops = '^-*/+'

    length2 = len(transcribe)
    for index in range(length2):
        if index > 0 and transcribe[length2 - index] == '-' and found(transcribe[length2 - index - 1], ops):
            transcribe.insert(length2 - index, '*')
            transcribe.insert(length2 - index, '-1')
            transcribe.pop(length2 - index + 2)
            print(transcribe)
        if index == length2 - 1 and transcribe[0] == '-':
            transcribe.insert(0, "*")
            transcribe.insert(0, "-1")
            transcribe.pop(2)
            print(transcribe)
    while int(transcribe.count("^")):
        for i in range(len(transcribe)):
            if transcribe[i] == '^':
                transcribe[i - 1] = float(transcribe[i - 1]) ** float(transcribe[i + 1])
                transcribe.pop(i)
                transcribe.pop(i)
                print(transcribe)
                break
    while int(transcribe.count("*")) or int(transcribe.count("/")) or int(transcribe.count("!")):
        for n in transcribe:
            if n == "*" or n == "!":
                type = 0
                break
            if n == "/":
                type = 1
                break
        if type == 0:
            for i in range(len(transcribe)):
                if transcribe[i] == '*':
                    transcribe[i - 1] = float(transcribe[i - 1]) * float(transcribe[i + 1])
                    transcribe.pop(i)
                    transcribe.pop(i)
                    print(transcribe)
                    break
                if transcribe[i] == '!':
                    total = 1
                    for n in range(int(transcribe[i - 1])):
                        total *= (n + 1)
                    transcribe[i - 1] = total
                    transcribe.pop(i)
                    print(transcribe)
                    break
        if type == 1:
            for i in range(len(transcribe)):
                if transcribe[i] == '/':
                    transcribe[i - 1] = float(transcribe[i - 1]) / float(transcribe[i + 1])
                    transcribe.pop(i)
                    transcribe.pop(i)
                    print(transcribe)
                    break
    while int(transcribe.count("+")) or int(transcribe.count("-")):
        for n in transcribe:
            if n == "+":
                type = 0
                break
            if n == "-":
                type = 1
                break
        if type == 0:
            for i in range(len(transcribe)):
                if transcribe[i] == '+':
                    transcribe[i - 1] = float(transcribe[i - 1]) + float(transcribe[i + 1])
                    transcribe.pop(i)
                    transcribe.pop(i)
                    print(transcribe)
                    break
        if type == 1:
            for i in range(len(transcribe)):
                if transcribe[i] == '-':
                    transcribe[i - 1] = float(transcribe[i - 1]) - float(transcribe[i + 1])
                    transcribe.pop(i)
                    transcribe.pop(i)
                    print(transcribe)
                    break
    return int(transcribe[0])

#print(answer('|-(5--3)^(4+6)/1|'))

