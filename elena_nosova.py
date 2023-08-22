my_str = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. \
ьА у нас управдом — друг человека!"
#step1
print("Шаг 1 - количество символов:", len(my_str)) 
#step2
reversed_my_str = ''.join(reversed(my_str))
print("Шаг 2 - развернута строка:", reversed_my_str) 
#step3
print("Шаг 3 - каждое слово с большой буквы:", my_str.title()) 
#step4
print("Шаг 4 - вeсь текст прописными буквами:", my_str.lower()) 
#step5
counter1 = my_str.count('нд') 
counter2 = my_str.count('ам') 
counter3 = my_str.count('о')
print('Шаг 5 - число вхождений "нд", "ам", "о" в строку: ' \
    "'нд' - ", counter1, ","\
    "'ам' - ", counter2, ","\
    "'о' - ", counter3, sep='') 
#step6
print("Шаг 6 - Переводит символы нижнего регистра в верхний, \
а верхнего – в нижний:", my_str.swapcase())
#step7
reversed_words = " ".join(my_str.split(" ")[::-1])
print("Шаг 7 - развернут порядок слов в предложении:", reversed_words)
#step8
print("Шаг 8 - вывод в консоль исходной строк:", my_str)