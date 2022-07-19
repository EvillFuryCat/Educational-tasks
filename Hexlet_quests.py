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

#мемоизирующий декоратор "memoizing". Но на этот раз декоратор должен принимать аргумент, задающий максимальное количество
#  запоминаемых значений. При превышении количества запомненных значений лишние должны быть отброшены, причём сначала — самые старые!
from functools import wraps


def memoizing(limit):
    def memoized(function):
        memory = {}

        @wraps(function)
        def inner(items):
            memoized_result = memory.get(items)
            if memoized_result is None:
                memoized_result = function(items)
                memory[items] = memoized_result
            if len(list(memory.values())) > limit:
                memory.pop(list(memory)[0])
            return memoized_result
        return inner
    return memoized

#написать функцию non_empty_truths(), которая с помощью генераторов списков должна вычислять копию входного списка списков,
#  "очищенную" от ложных элементов (не только False, а любых ложных!), а заодно и от пустых списков — таковые могу присутствовать сами по себе
#  или могут получаться после отбрасывания из них всех элементов.
#from solution import non_empty_truths
#non_empty_truths([])  # нечего отбрасывать, это тоже нормально
# >>>[]
#non_empty_truths([[], []])  # пустые отбрасываем
# >>>[]
#non_empty_truths([[0]])  # чистим, чистые, но пустые тоже отбрасываем
# >>>[]
#non_empty_truths([[0, ""], [False, None]])  # в Python многое считается ложным
# >>>[]
#non_empty_truths([[0, 1, 2], [], [], [False, True, 42]])
# >>>[[1, 2], [True, 42]]
def non_empty_truths(items):
    return [
        result for result in
        [[elem for elem in item if elem]
         for item in items
         ]
        if result
    ]

# Вам предстоит реализовать три функции, каждая из которых будет работать с двухмерной матрицей, то есть со списком списков 
# (итератором итераторов).

#each2d(test, matrix) должна проверить, что каждый элемент матрицы matrix удовлетворяет предикату test, и вернуть False,
# если хотя бы для одного элемента test вернул False. В противном случае функция должна возвращать True.

#some2d(test, matrix) должна проверить, удовлетворяет ли предикату test хотя бы один элемент матрицы matrix. 
# Как только test возвращает True для какого-либо элемента, функция должна вернуть True, в противном случае 
#(если ни один элемент проверку не прошёл) нужно вернуть False.

#sum2d(test, matrix) должна возвращать сумму всех элементов матрицы matrix, удовлетворяющих предикату test.
#Внимание, первые две функции не должны выполнять лишней работы: обход матрицы должен прерываться, как только результат 
#становится ясен

def each2d(test, matrix):
    return all(
        test(number)
        for items in matrix
        for number in items
    )


def some2d(test, matrix):
    return any(
        test(number)
        for items in matrix
        for number in items
    )


def sum2d(test, matrix):
    return sum(
        number
        for items in matrix
        for number in items
        if test(number)
    )

#def is_int(x):
#    return isinstance(x, int)

#each2d(is_int, [[1, 2], [3, 4]])
# True
#each2d(is_int, [[1, None], [3, 4]])
# False
# В пустой матрице нет ни одного элемента, который бы завалил тест
#each2d(is_int, [])
# True
#some2d(is_int, [[None, "foo"], [(), {}]])
# False
#some2d(is_int, [[None, "foo"], [0, {}]])
# True
# В пустой матрице нет ни одного элемента, который бы прошёл тест
#some2d(is_int, [])
# False
#sum2d(is_int, [[1, "Foo", 100], [False, 10, None]])
# 111