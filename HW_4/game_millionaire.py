import random
import os

questions = [
"Где в стихотворении 'Узник' А. С. Пушкина сидит вскормлённый в неволе орёл молодой?",
"Какой титул присвоила себе Фрекен Бок из сказки А. Линдгрен?",
"Какое перо чаще всего использовали в старину для письма?",
"Какой стране принадлежат Канарские острова?",
"Название какой монетки происходит от слова 'сто' ",
"Что коллекционирует филуменист?",
"Представители трёх поколений этой политической династии стали объектами терактов. Какой?",
"Что можно сделать, используя крупчатку",
"Название какого города переводится как Белый холм?",
"Реки с каким названием нет на территории России?"
]
answers = [
    { 1000: [(True, "1 - За решеткой"), (False, "2 - Под столом"),\
        (False, "3 - Под деревом"), (False, "4 - Под скалой")]},
    { 2000: [(False, "1 - Няня"), (True, "2 - Домоправительница"),\
        (False, "3 - Воспитательница"), (False, "4 - Мучительница")]},
    { 4000: [(False, "1 - Павлинье перо"), (False, "2 - Перо ворона"),\
        (True, "3 - Гусиное перо"), (False, "4 - Перо страуса")]},
    { 6000: [(True, "1 - Испания"), (False, "2 - Португалия"),\
        (False, "3 - Франция"), (False, "4 - Великобритания")]},
    { 8000: [(True, "1 - Цент"), (False, "2 - Шиллинг"),\
        (False, "3 - Копейка"), (False, "4 - Пфенниг")]},
    { 16000: [(True, "1 - Спичечные коробки"), (False, "2 - Пробки"),\
        (False, "3 - Фотографии"), (False, "4 - Предметы живописи")]},
    { 32000: [(True, "1 - Ганди"), (False, "Бхутто"),\
        (False, "3 - Рабин"), (False, "4 - Кеннеди")]},
    { 46000: [(True, "1 - Замесить тесто"), (False, "2 - Слепить снежок"),\
        (False, "3 - Покрыть дорогу"), (False, "4 - Оседлать лошадь")]},
    { 64000: [(True, "1 - Актобе"), (False, "2 - Астана"),\
        (False, "3 - Кызыл орда"), (False, "4 - Караганда")]},
    { 100000: [(True, "1 - Спина"), (False, "2 - Шея"),\
        (False, "3 - Уста"), (False, "4 - Палец")]}
]
hints = ["Помощь зала", "50/50", "Звонок другу"]
sum = 0

not_correct_elements = []

for question in questions:
    print()
    question_number = questions.index(question)                 
    answers_for_question = answers[question_number]             
    for key, value in answers_for_question.items():
        cost = key    
        print("Вопрос за", key, ":")
    print(question)
    print("Варианты ответов: ")
    for i in answers_for_question.values():
        for values in i:
            print(values[1])
    print("Вы можете выбрать ответ либо можете воспользоваться подсказкой: ") 
    print()
    for i in answers_for_question.values():
        for values in i:
            if values[0] == False:
                not_correct_elements.append(values[1])
            else:
                correct_answer = values[1]    
    not_correct_element = random.choice(not_correct_elements)         
    a = str(input())   
    if a == hints[0]:
        print("Вы выбрали Помощь зала")
        print(correct_answer, not_correct_element)
        a = str(input())
        if a == correct_answer.find(a) != -1:
            print("Вы правильно ответили на вопрос:")
        else:
            print("Вы не правильно ответили на вопрос")
    elif a == hints[1]:
        print("Вы выбрали 50/50")
        print(correct_answer, not_correct_element)
        a = str(input())
        if a == correct_answer.find(a) != -1:
            print("Вы правильно ответили на вопрос:")
        else:
            print("Вы не правильно ответили на вопрос")
    elif a == hints[2]:
        print("Вы выбрали Звонок другу")
        print(correct_answer, not_correct_element)
        a = str(input())
        if a == correct_answer.find(a) != -1:
            print("Вы правильно ответили на вопрос:")
        else:
            print("Вы не правильно ответили на вопрос")
    elif correct_answer.find(a) != -1: 
        os.system('cls')
        print()
        sum += cost
        print("Вы правильно ответили на вопрос, Ваш выигрыш", sum)
    else:
        print("Вы неправильно ответили на вопрос. Вы проиграли")            
        break