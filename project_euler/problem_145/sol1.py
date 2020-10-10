def is_reversible(test_num: int) -> bool:
    test_number_string = str(test_num)
    reverse_test_number_string = test_number_string[::-1]
    sum = int(test_number_string) + int(reverse_test_number_string)
    for digit in str(sum):
        if int(digit) % 2 == 0:
            return False
    return True

def number_of_reversible_given_length(number_of_digits: int) -> int:
    number_of_reversible = 0
    for first_digit in range(1, 10, 2):
        for last_digit in range(2, 10, 2):
            max_middle_string = (number_of_digits - 2) * '9'
            for middle in range(0, int(max_middle_string) + 1):
                middle_string = str(middle)
                if len(middle_string) < (number_of_digits - 2):
                    middle_string = (number_of_digits - 2 - len(middle_string)) * '0' + middle_string
                test_number_string = str(first_digit) + middle_string + str(last_digit)
                test_number = int(test_number_string)
                if is_reversible(test_number):
                    number_of_reversible += 2
    return number_of_reversible


if __name__ == '__main__':
    print(number_of_reversible_given_length(8))
