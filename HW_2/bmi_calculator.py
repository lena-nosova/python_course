the_height = float(input("Введите Ваш рост (м): "))
the_weight = float(input("Введите Ваш вес (кг): "))
bmi = the_weight/(the_height**2)
print("Ваш индекс массы тела:", bmi)

a = 16
b = 40
b1 = int(bmi) - a
b2 = b - int(bmi)

print("16" + b1 * "=" + "|" + b2 * "=" + "40")




