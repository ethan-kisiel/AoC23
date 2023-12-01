from shared.helpers import clean_line

NUMBERS = {"one": 1, 
           "two": 2,
           "three": 3,
           "four": 4,
           "five": 5,
           "six": 6,
           "seven": 7,
           "eight": 8,
           "nine": 9}

def get_contained_number(input: str):
    for number in NUMBERS.keys():
        if number in input:
            return NUMBERS[number]
    return None
    

def get_first_number(line: str, index: int, search_up: bool) -> int:
    if index < 0 or index >= len(line):
        return -1
    
    if search_up:
        current_string = line[0:index+1]
        if get_contained_number(current_string) is not None:
            return get_contained_number(current_string)
    else:
        current_string = line[index:]
        if get_contained_number(current_string) is not None:
            return get_contained_number(current_string)
            

    if ord(line[index]) >= 48 and ord(line[index]) <= 57:
        return line[index]
    
    next_index = index + 1 if search_up else index -1
    return get_first_number(line, next_index, search_up)

def get_line_total(line: str) -> int:
    # takes a string of a line,
    #
    
    
    first_digit = get_first_number(line, 0, True)
    last_digit = get_first_number(line, len(line)-1, search_up=False)
    
    try:
        return int(f"{first_digit}{last_digit}")
    except ValueError:
        print(f"{first_digit}{last_digit}")



def solve() -> int:
    total = 0
    
    with open("day1/input.txt", "r") as input_file:
        for line in input_file.readlines():
            total += get_line_total(clean_line(line))
    
    return total