import date_time as date_time
import numbers as numbers
from time import sleep
import os


digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":"]

def get_final_digits(result, digits):
    new_digits = []
    for symbols in result:
        for digit_number, i in enumerate(digits):
            if symbols == i:
                new_digits.append(numbers.custom_digits[digit_number])
            
    new_digits_0 = []
    new_digits_1 = []
    new_digits_2 = []
    new_digits_3 = []
    new_digits_4 = []
    
    for new_digit in new_digits:
        new_digits_0.append(new_digit[0])
        new_digits_1.append(new_digit[1])
        new_digits_2.append(new_digit[2])
        new_digits_3.append(new_digit[3])
        new_digits_4.append(new_digit[4])

    final_digits = [new_digits_0, new_digits_1, new_digits_2, new_digits_3, new_digits_4]
    return final_digits


def print_final_result(final_digits):
    for final_digit in final_digits:
        print(*final_digit)


while True:
    result = list(date_time.current_time())
    final_digits = get_final_digits(result, digits)
    print_final_result(final_digits)
    sleep(1)
    os.system('cls')

