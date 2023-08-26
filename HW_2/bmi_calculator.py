the_height = float(input("Введите Ваш рост (м): "))
the_weight = float(input("Введите Ваш вес (кг): "))
bim = the_weight/(the_height**2)
print("Ваш индекс массы тела:", bim)

a = 16
b = 40
b1 = int(bim) - a
b2 = b - int(bim)

list = [("=" * b1), '|', ("=" *  b2)]
print(a, list[0], list[1], list[2], " ", b, sep = "")




