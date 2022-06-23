from time import sleep
import time
import random

def findSmallest(arr):#Возвращает индекс наименьшего значения
  smallest = arr[0] # переменная равна первому символу аргумента
  smallest_index = 0 # счетчик
  for i in range(0, len(arr)): #в переменную i запишем значение из переданного аргумента в диапозоне от первого до конца длинны списка
    #print('!!!', arr[i], '??', i, 'smallet равен', smallest)
    if arr[i] < smallest: #если символ в индексе i меньше первого символа аргумента 
      smallest = arr[i] # записывается символ под аргументом i на текущем шаге
      #print('warning', arr[i], 'smallest после if', smallest)
      smallest_index = i # по видемому это индекс наименьшего символа
  return smallest_index
#print(findSmallest(str(98789796542)))

def selectionSort(arr): # сортируем список
  new_arr = [] # сюда записывается результат в список
  for i in range(len(arr)): # с 0 по всей длинне списка 
    print(arr)
    smallest = findSmallest(arr) #  в переменную загружаем результат функции 
    new_arr.append(arr.pop(smallest))# .append добавляет в конец списка значение arr.pop (.pop берет значение по индексу из функции и выписывает их в переменную, в порядке убывания)
  return new_arr
#print(selectionSort([5, 3, 6, 2, 10, 3]))
#print('Новая функция ') бинарный поиск?
def max(list):
  if len(list) == 2: #если длинна аргумента 2 то следует вернуть 56 если 56 больше 5 иначе вернуть 5
    return list[0] if list[0] > list[1] else list[1]
  sub_max = max(list[1:]) # max находит большее число индексу после 1 игнорируя 56 
  return list[0] if list[0] > sub_max else sub_max
#print(max([10,56, 5, 55, 44, 102]))

def sum(string):
  result = 0
  i = 0
  while i < len(string):
    string_of = int(string[i])
    result += string_of
#    print("!!!", string_of)
    i += 1
  return result
#print(sum('2346'))

def quicksort(array):
    if len(array) < 2: # базовый случай
        return array
    else:
        pivotidx = random.randint(0, (len(array)-1))
        array[0], array[pivotidx] = array[pivotidx], array[0]
        pivot = array[0] # рекурсивный случай, опорный символ
#        print('!!!!', pivot)
        less = [i for i in array[1:] if i <= pivot] #Подмассив всех элементов меньших опорного
        greater = [i for i in array[1:] if  i > pivot] #Больше опорного
        return quicksort(less) + [pivot] + quicksort(greater)# с помощью конкатенации соединяються сначала меньшие затем опорный и те что больше опорного.
        #таким образом функция вызывает саму себя и сортирует весь массив
print(quicksort([10, 20, 9, 65, 70, 3, 100]))

def print_items2(list):
  for item in list:
    time.sleep(1)
    print(item)
print_items2([1,2,3,4])
print(time.asctime())



'''Здесь начинаются разного рода функции '''
# Функции toggle и toggled своебразные флаги работает на изменениях множеств, если флаг есть во множестве удаляет его, если нет добавляет. Переключатель
def toggle(flag, items):
    if flag in items:
        items.discard(flag)
    else:
        items.add(flag)

def toggled(flag, items):
    result = items.copy()
    if flag in result:
        result.discard(flag)
    result.add(flag)
    return result

READ_ONLY = 'read_only'
flags = set()
new_flags = toggled(READ_ONLY, flags)
print(READ_ONLY in flags)
print(READ_ONLY in new_flags)

#Эта функция должна принимать на вход коллекцию (некий iterator/iterable) и возвращать словарь (или подобная ему коллекция!),
#  где ключом будет элемент коллекции, а значением для ключа — список индексов коллекции, по которым встречается этот элемент.
def collect_indexes(collection):
    result = {}
    for index, item in enumerate(collection):
        result.setdefault(item, []).append(index)
    return result

from collections import defaultdict
def collect_indexes(items):
    result = defaultdict(list)
    for index, item in enumerate(items):
        result[item].append(index)
    return result

#функцию diff_keys(), которая должна принимать два словаря-аргумента — "старый" и "новый" — и возвращать словарь с результатами анализа.
#  Результирующий словарь должен содержать строго три ниже перечисленных ключа:
#'kept' — множество ключей, которые присутствовали в старом словаре и остались в новом;
#'added' — множество ключей, которые отсутствовали в старом словаре, но появились в новом;
#'removed' — множество ключей, которые присутствовали в старом словаре, но в новый не вошли.

def diff_keys(old, new):
    old_keys = set(old.keys())
    new_keys = set(new.keys())
    return {
        'kept': old_keys & new_keys,
        'added': new_keys - old_keys,
        'removed': old_keys - new_keys,
    }
#Эта функция принимает два аргумента, первым из которых выступает множество, которое нужно будет изменять "по месту"
#  (возвращать ничего не нужно). Вторым аргументом функция принимает словарь, который может содержать ключи 'add' и 'remove'
# с множествами в качестве значений. Значения по ключу 'add' нужно добавить в изменяемое множество, а значения по ключу 'remove'
#  — убрать из множества. Прочие ключи в переданном словаре значения не имеют и обрабатываться не должны.
# мой вариант
def apply_diff(target, diff):
    if 'add' in diff:
        target.update(diff['add'])
    if 'remove' in diff:
        target.difference_update(diff['remove'])
# Вариант учителя
def apply_diff(set_for_update, diff):
    set_for_update.update(diff.get('add', {}))
    set_for_update.difference_update(diff.get('remove', {}))

#greet(), которая должна принимать несколько имён (как минимум одно!) и возвращать строку приветствия (см. примеры ниже).
def greet(person, *args):
    name = ' and '.join((person,) + args)
    return f'Hello, {name}!'

print(greet('Moe', 'Mary'))
print(greet(*'ABCDEFN'))
print(greet('Bob'))

a, b = input().split()
print(int(a) + int(b))


#В этом упражнении вам нужно будет, используя функцию rgb(), реализовать функцию get_colors(), которая должна вернуть словарь цветов
#В словаре должны присутствовать ключи 'red', 'green', 'blue'. Каждому ключу должен соответствовать результат вызова функции rgb()
#  со значением 255 для соответствующего ключу аргумента. Для построения каждого цвета используйте только один аргумент!

def rgb(red=0, green=0, blue=0):
    return f'rgb({red}, {green}, {blue})'


def get_colors():
    colors = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    colors['red'] = rgb(red=255)
    colors['green'] = rgb(green=255)
    colors['blue'] = rgb(blue=255)
    return colors