
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

def print_array(arr): # вывод массив в столбик аля красиво
    for a in arr:
        for elem in a:
            print("{}".format(elem).rjust(3), end="")
        print(end="\n")

def ihatematrices(idk): # весь алгоритм кодирования и прочего интересного стаффа тут
    return
    
#-------------

#   Основной код

img = Image.open("D:/VSrepos/PhotoworkTI_Python/img/circle.jpg")

#       Первый шаг - вывод фото на экран и массива в консоль

#img.show() # вывод на экран

img_array = np.asarray(Image.open("D:/VSrepos/PhotoworkTI_Python/img/circle.jpg").convert('RGB')) # массив 
print()
console_output(img_array)   # вывод массива в консоль

#       Второй шаг - зашумление фото

img_array_binary = np.array(decim_to_binary(img_array)) # перевод в бинарку 
print()
console_output(img_array_binary) # вывод бинарки

img_array_binary_noice = np.array(noice_img(img_array_binary)) # "шумим" массим
print()
console_output(img_array_binary_noice) # вывод шумки

img_decim_noice_np = np.array(binary_to_decim(img_array_binary_noice))
print()
console_output(img_decim_noice_np) # вывод шумки в десятичной для вывода в фотку

img2 = Image.fromarray(img_decim_noice_np, 'RGB')
img2.save("D:/VSrepos/PhotoworkTI_Python/img/circle2.jpg") # сэйв массива в фотку

#img2.show() # вывод шумной фотки

#       Третий шаг - работа с фото (кодирование и т.п.)


# проверочная матрица G

G = np.array([[1, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
              [0, 1, 0, 0, 0, 0, 0, 0,  1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
              [0, 0, 1, 0, 0, 0, 0, 0,  1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
              [0, 0, 0, 1, 0, 0, 0, 0,  0, 1, 1, 0, 1, 0, 1, 0, 1, 0],
              [0, 0, 0, 0, 1, 0, 0, 0,  1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0,  0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 1, 0,  1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 1,  0, 0, 1, 1, 1, 0, 1, 0, 1, 1]])

# параметры n,k

n = 0
i_l_n = G[0]
for i in i_l_n: 
    n += 1

k = 8

print("\n n =", n, " k =", k)
print()

# проверочная матрица систематическая

ident_G = np.identity(k).astype(int) # строим единичную отталкиваясь от параметра к
equals_nonzeros = np.nonzero((G.sum(axis=0) > 1).astype(int))[0] # столбик суммой > 1, чтобы не брать столбики для единичной
equals_zeros = np.nonzero((G.sum(axis=0) == 0).astype(int))[0] # столбик суммой = 0, чтобы также не брать столбики для единичной
to_nonident = np.sort(np.hstack([equals_nonzeros, equals_zeros])) # собираем эти столбики в один массив
nonident = G[:, to_nonident] 
G_sys = np.hstack([ident_G, nonident]) # собираем полную систематическую матрицу

print('G_sys') # её вывод
print_array(G_sys)
print()

# таблица /i, c, wth/ и параметры d, t

d = np.array(range(2**k)) # создаем "столбик" веса строк или d 

matrix_i = ((d[:,None] & (1 << np.arange(k))[::-1]) > 0).astype(int) # матрица i от 0 до 255 в двоичной системе

matrix_c = np.zeros((2**k, n-k)) # половинка матрицы с, так как полный столбик с состоит из матрицы i и того что мы сложим исходя из индексов битов в i  

for i in range(len(matrix_i)): # заполнение этой половинки
    temp = np.array((nonident[np.nonzero(matrix_i[i]), :])[0])
    tempsum = temp.sum(axis=0)
    for j in range(len(tempsum)):
        tempsum[j] = tempsum[j]%2
    matrix_c[i] = tempsum
matrix_c = matrix_c.astype(int)

ic_mat = np.hstack([matrix_i, matrix_c]) # полноценный столбик с

matrix_icwth = np.hstack([matrix_i, ic_mat, ic_mat.sum(axis=1).reshape(-1, 1)]) # вся таблица /i, c, wth/

print('         i = k           |                         c = n                      | d ') 
print('----------------------------------------------------------------------------------')
print_array(matrix_icwth[:20]) # её вывод
print()

d_min = ic_mat.sum(axis=1)[1:].min() # поиск минимального d

t = (d_min - 1) / 2 # поиск t
print('t: ', t)
print()

# порождающая систематическая матрица H_sys

ident_H = np.identity(n-k).astype(int)

H_sys = np.hstack([nonident.T, ident_H])
print('H_sys')
print_array(H_sys)
print()

# порождающая систематическая транспонированная матрица H_sys_T

H_sys_T = H_sys.T
print('H_sys_T')
print_array(H_sys_T)
print()

#

img_array_binary_to_code = []

for i in img_array_binary:
    for j in i:
        for k in j:
            word = []
            qwe = np.zeros((8))
            for q in range(len(k)):
                word.append(int(k[q]))
            img_array_binary_to_code.append(word)                       
print(img_array_binary_to_code)
#print(len(img_array_binary_to_code)) # - 108
#print("m_i -", len(matrix_i)) # - 256

#for i in range(len(img_array_binary_to_code)):
for i in range(1):

    codeword = img_array_binary_to_code[i]
    print(codeword)

    # поиск этого слова в матрице i
    
    codeword_index = -1
    
    for j in matrix_i:
        codeword_index += 1
        line = j
        new_fcking_counter = 0
        for j in range(len(line)):
            if line[j] != codeword[j]:
                break
            else:
                new_fcking_counter += 1
        if new_fcking_counter == len(line):
            break
    print(codeword_index) # вывод индекса -- верно

    # берем значение с по индексу из матрицы c
    idkyo = 3
    v = ic_mat[idkyo]
    print('v')
    print('-------------------------')
    print(v)
    print()
    #print("i -",matrix_i[idkyo])
    #print("i index -", idkyo)
    #print()


    # ошибк а/и

    error_pointer = randint(1,t)

    if error_pointer == 2:
        i1 = 0
        i2 = 0
        while 1:
            i1 = randint(0,len(v)-1)
            i2 = randint(0,len(v)-1)
            if i1 != i2:
                break
        print("First error index is -", i1)
        print("Second error index is -", i2)
        v[i1] = np.bitwise_not(v[i1].astype(bool))
        v[i2] = np.bitwise_not(v[i2].astype(bool))
    elif error_pointer == 1:
        i1 = randint(0,len(v)-1)
        print("Error index is -", i1)
        v[i1] = np.bitwise_not(v[i1].astype(bool))
    else:
        print("There're no errors")
    #print('v')
    print('\n-------------------------')
    print(v)
    print()

    # добавляем таблицу /S, e/

    #   она состоит из трех матриц: 1) нет ошибок, 2) одна ошибка и 3) 2 ошибки

    # 1)
    matrix_S_zero = np.zeros((1,(len(H_sys_T[0]))))
    err_S_zero = np.zeros((1,n))
    matrix_S_zero = matrix_S_zero.astype(int)
    err_S_zero = err_S_zero.astype(int)
    matrix_se_zero = np.hstack([matrix_S_zero, err_S_zero])

    # 2)
    err_S_one = np.identity(n).astype(int)
    err_S_one = np.rot90(err_S_one)
    matrix_S_one = H_sys_T[::-1]
    matrix_se_one = np.hstack([matrix_S_one, (err_S_one)])

    # 3)
    
    err_sum = 0
    for i in range(n):
        err_sum += i
    err_S_two = np.zeros((err_sum, n))
    count = 0
    indexcount = 0
    plus_k = 1
    for i in reversed(range(n)):
        for k in range(i):
            line = err_S_two[count]
            line[indexcount] = 1
            line[k+plus_k] = 1
            count += 1
        indexcount += 1
        plus_k += 1
    indexcount = 0
    err_S_two = err_S_two.astype(int)
    matrix_S_two = np.zeros(((len(err_S_two)),(len(H_sys_T[0]))))
    for i, r in enumerate(err_S_two):
        temp_line = H_sys_T[np.nonzero(r)[0], :]
        matrix_S_two[i] = np.bitwise_xor(*temp_line)
    matrix_S_two = matrix_S_two.astype(int)
    matrix_se_two = np.hstack([matrix_S_two, err_S_two])

    print('           S = 10             |                       e = 18                      ')
    print('----------------------------------------------------------------------------------')
    print_array(matrix_se_zero)
    print_array(matrix_se_one)
    print_array(matrix_se_two)
    print()


    # поиск S'

    for i in range(1):
        temp = np.array((H_sys_T[np.nonzero(v), :])[0])
        S_new = temp.sum(axis=0)
        for i in range(len(S_new)):
            S_new[i] = S_new[i]%2
    print("S")
    print('-------------------------')
    print(S_new)
    print()

    # поиск с' = v + e

    print("Amount of errors -", error_pointer)
    print()
    if error_pointer == 2:
        e_index = 0
        for i in range(len(matrix_S_two)):
            e_index += 1
            line = matrix_S_two[i]
            new_fcking_counter = 0
            for j in range(len(line)):
                if line[j] != S_new[j]:
                    break
                else:
                    new_fcking_counter += 1
            if new_fcking_counter == len(line):
                break
            c = np.bitwise_xor(v, (err_S_two[e_index]))
        #print("Index of S-line -",e_index + 18)
        #print("e\n-------------------------\n", (err_S_two[e_index - 1]))
        #print("This fucking E-line -", err_S_two[(e_index - 1): (e_index)])
        print("e")
        print('-------------------------')
        print(err_S_two[e_index])

    elif error_pointer == 1:
        e_index = 0
        for i in range(len(matrix_S_one)):
            e_index += 1
            line = matrix_S_one[i]
            new_fcking_counter = 0
            for j in range(len(line)):
                if line[j] != S_new[j]:
                    break
                else:
                    new_fcking_counter += 1
            if new_fcking_counter == len(line):
                break
        c = np.bitwise_xor(v, err_S_one[e_index-1])
        #print("Index of S-line -",e_index)
        #print("e -", err_S_one[(e_index - 1)])
        #print("This fucking E-line -", err_S_one[(e_index - 1): (e_index)])
        print("e")
        print('-------------------------')
        print(err_S_one[(e_index - 1)])

    else:
        e_index = 1
        c = np.bitwise_xor(v, err_S_zero[e_index-1])
        #print("Index of S-line -",e_index-1)
        #print("e\n-------------------------\n", err_S_zero[e_index-1])
        #print("This fucking E-line -", err_S_zero[(e_index - 1): (e_index)])
        print("e")
        print('-------------------------')
        print(err_S_zero[(e_index - 1)])

    i = c[:8] # кодовое слово которое мы искали

    print("\nv")
    print('-------------------------')
    print(v)

    print("\nc' = v + e")
    print('-------------------------')
    print(c)

    


    print('\ni')
    print('-------------------------')
    print(i)

    #print("i -",matrix_i[idkyo])

#    img_array_matrix_output[i] = i

#print("asd")
#print(img_array_matrix_output)

# все считает верно. осталось заносить в матрицу для фотки и саму фотку выводить




#-------------