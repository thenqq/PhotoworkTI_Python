
#   Импорты

import numpy as np
from PIL import Image
from random import randint
from numpy.core.arrayprint import printoptions
from numpy.core.numeric import identity
from numpy.lib.function_base import i0

#-------------

#   Функции

def console_output(i_a): # вывод в консоль
    count = 0
    print("[", end='')
    for i in i_a:
        count+=1
        print("[", end='')
        for j in i:
            print(j, end='')
        if count != len(i_a):
            print("]")
        else:
            print("]", end='')
    print("]")

    pass

def decim_to_binary(i_a): # из десятичной в бинарную

    img_binary_list = []
    for i in i_a:
        number_line = []
        for j in i:
            number_list = []
            for k in j:
                number = k
                binary_number = 0
                binary_number_str = '0'
                rank = 1
                if (number == 0) :
                    binary_number = 0
                    number_list.append(binary_number_str * 7 + str(binary_number))
                elif (number == 1) :
                    binary_number = 1
                    number_list.append(binary_number_str * 7 + str(binary_number))
                elif (number == 2) :
                    binary_number = 10
                    number_list.append(binary_number_str * 6 + str(binary_number))
                elif (number == 3) :
                    binary_number = 11
                    number_list.append(binary_number_str * 6 + str(binary_number))
                elif (number >= 4 and number <= 7) :
                    binary_number += 1*100
                    while (number >= 2):
                        binary_number += (number % 2) * rank
                        number = number // 2
                        rank = rank * 10
                    number_list.append(binary_number_str * 5 + str(binary_number))
                elif (number >= 8 and number <= 15) :
                    binary_number += 1*1000
                    while (number >= 2):
                        binary_number += (number % 2) * rank
                        number = number // 2
                        rank = rank * 10
                    number_list.append(binary_number_str * 4 + str(binary_number))
                elif (number >= 16 and number <= 31) :
                    binary_number += 1*10000
                    while (number >= 2):
                        binary_number += (number % 2) * rank
                        number = number // 2
                        rank = rank * 10
                    number_list.append(binary_number_str * 3 + str(binary_number))
                elif (number >= 32 and number <= 63) :
                    binary_number += 1*100000
                    while (number >= 2):
                        binary_number += (number % 2) * rank
                        number = number // 2
                        rank = rank * 10
                    number_list.append(binary_number_str * 2 + str(binary_number))
                elif (number >= 64 and number <= 127) :
                    binary_number += 1*1000000
                    while (number >= 2):
                        binary_number += (number % 2) * rank
                        number = number // 2
                        rank = rank * 10
                    number_list.append(binary_number_str * 1 + str(binary_number))
                else :
                    binary_number += 1*10000000
                    while (number >= 2):
                        binary_number += (number % 2) * rank
                        number = number // 2
                        rank = rank * 10
                    number_list.append(str(binary_number))
            number_line.append(number_list)
        img_binary_list.append(number_line)
    return img_binary_list

def noice_img(i_a_b): # шумка
    img_binary_noice_list = []
    for i in i_a_b:
        number_line = []
        for j in i:
            number_list = []
            for k in j:
                line = k
                pos = randint(0,7)
                temp = list(line)
                if temp[pos] == '1':
                    temp[pos] = '0'
                else:
                    temp[pos] = '1'
                line = ''.join(temp)
                number_list.append(line)
            number_line.append(number_list)
        img_binary_noice_list.append(number_line)
    return img_binary_noice_list

def binary_to_decim(i_a_b): # из бинарной в десятичную
    img_binary_noice_list = []
    for i in i_a_b:
        number_line = []
        for j in i:
            number_list = []
            for k in j:
                number = 0
                line_two = ''
                count = 0
                for r in k: 
                    line_two = r + line_two
                for r in line_two:
                    if r == '1':
                        number += 2 ** count
                    count += 1
                number_list.append(number)
            number_line.append(number_list)
        img_binary_noice_list.append(number_line)
    return img_binary_noice_list
    pass

#-------------

#   Основной код

img = Image.open("D:/VSrepos/PhotoworkTI_Python/img/circle.jpg")

#       Первый шаг - вывод фото на экран и массива в консоль

#img.show() # вывод на экран

img_array = np.asarray(Image.open("D:/VSrepos/PhotoworkTI_Python/img/wp.jpg").convert('RGB')) # массив 
print()
#console_output(img_array)   # вывод массива в консоль

#       Второй шаг - зашумление фото

img_array_binary = np.array(decim_to_binary(img_array)) # перевод в бинарку 
#print()
#console_output(img_array_binary) # вывод бинарки

img_array_binary_noice = np.array(noice_img(img_array_binary)) # "шумим" массим
#print()
#console_output(img_array_binary_noice) # вывод шумки

img_decim_noice_np = np.array(binary_to_decim(img_array_binary_noice))
print()
#console_output(img_decim_noice_np) # вывод шумки в десятичной для вывода в фотку

img2 = Image.fromarray(img_decim_noice_np, 'RGB')
img2.save("D:/VSrepos/PhotoworkTI_Python/img/wp2.jpg") # сэйв массива в фотку

img2.show() # вывод шумной фотки


#-------------