#Задача Яндекс Контекс цифровые ребусы
from math import log2

n = int(input())
el_list = list(map(int, input().split()))
letter_dict = {
    0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h',
    8:'i', 9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o',
    15:'p', 16:'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v',
    22:'w', 23:'x', 24:'y', 25:'z', 26:' ',
}
list_result = []
result = ''
sum_letter = 0
list_result.append(letter_dict[int(log2(el_list[0]))])
for i in range(1, n):
    diff = el_list[i] - el_list[sum_letter]
    if diff < 0:
        diff = abs(diff)
    sum_letter += 1
    list_result.append(letter_dict[int(log2(diff))])
for letter in list_result:
    result += letter
print(result)