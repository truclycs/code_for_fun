def get_numbers(s):
    numbers = ""
    for char in s:
        if '0' <= char <= '9':
            numbers += char
    return numbers


def get_result(numbers):
    result = ""
    current_string = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i - 1] >= numbers[i]:
            current_string += numbers[i]
            if len(current_string) > len(result):
                result = current_string
        else:
            current_string = numbers[i]

    return result


if __name__ == '__main__':
    s = input()
    numbers = get_numbers(s)
    print(get_result(numbers))
