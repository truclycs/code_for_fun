def get_numbers(input_string):    
    number = ""
    for char in input_string:
        if '0' <= char <= '9':
            number += char
    return number


def get_result(numbers):
    result = ""
    current_string = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:
            current_string += numbers[i]
            if len(current_string) > len(result):
                result = current_string
        else:
            current_string = numbers[i]           
            
    return result            
        

if __name__ == '__main__':
    input_string = input()
    numbers = get_numbers(input_string)
    print(get_result(numbers))   