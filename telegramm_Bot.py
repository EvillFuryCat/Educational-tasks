#!C:/Users/usr/AppData/Local/Programs/Python/Python310/env python
import re, random, nltk, json # Natural language toolkit

  # Обработать случае неточного совпадения 
  # больше фраз, Словарь для бота
  # изучить Python
  

def is_Match(text1, text2):
    text1 = text1.lower()
    text2 = text2.lower()
    #Удаление знаков препинания
    #Удалить все кроме букв и пробелов
    pattern = r'[^\w\s]'
    text1 = re.sub(pattern, "", text1)
    text2 = re.sub(pattern, "", text2) # re.sub Замена символов в строке
    # Проверить что одна фраза является частью другой
    # Текст 1 содержит текст 2
    if text1.find(text2) != -1:
      return True
    if text2.find(text1) != -1:
      return True
    # Расстояние Левенштейна (edit distance) 
    distance = nltk.edit_distance(text1, text2) # 0 ...Inf 
    length = (len(text1) + len(text2)) / 2 # Средняя длинна двух текстов
    score = distance / length #0 ... 1
    return score < 0.4
    # Сколько символов нудно отредактировать
# Намериния = intents 
# поздароваться, как дела, имя или чем занят
#slovar'
BOT_CONFIG = {
    # Все намерения которые поддерживает наш бот
    "intents": {
        "hello": {
            "examples" : ["Привет", "Здарова", "Йо", "Приветос", "Хеллоу"],
            "responses": ["Здравстсвтсвтвтвуй человек", "И тебе не хворать", "Здоровее видали"],
        },
        "how_are_you": {
            "examples" : ["Как дела", "Чо каво", "Как поживаешь"],
            "responses": ["Маюсь Фигней", "Веду интенсивы", "Учу Пайтон"],
        }
    },
    # Фразы когда бот не может ответить
    "failure_phrases": ["Даже не знаю что сказать", "Поставлен в тупик", "Перефразируйте, я всего лишь бот"],
}


    

def print_answer (text, examples, responses):
  for example in examples:# Для каждого элемента списка examples
    if is_Match(text, example): # Если пример совпадает с текстом пользователя
     print(random.choice(responses))# выводим на экран случайный ответ из списка responses
     break

text = input()
for intent in BOT_CONFIG['intents'].values():
  print_answer(text, intent['examples'], intent['responses'])
