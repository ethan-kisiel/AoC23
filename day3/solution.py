from shared.helpers import clean_line
from shared.helpers import is_number

def get_line_numbers(line: str) -> list[tuple[int, int]]:
    # takes a line and returns a list of start and end indecies(inclusive first, exclusive last) of the numbers

    numbers = []
    curr_tuple_number = [0, 0]
    curr_number = ""
    
    for i, digit in enumerate(line):
        if ord(digit) >= 48 and ord(digit) <= 57:
            # if the current digit is a number
            if curr_number == "":
                # if this digit is a brand new number
                curr_tuple_number[0] = i
                curr_number = f"{curr_number}{digit}"
            elif i == len(line) -1:
                # if this digit isn't a new number, and the current index is at the end of the line
                curr_tuple_number[1] = None
                numbers.append(curr_tuple_number)
                curr_tuple_number = [0, 0]
                curr_number = ""
            else:
                curr_number = f"{curr_number}{digit}"

        elif curr_number != "":
            # if the current digit isn't a number
            if i == len(line) -1:
                curr_tuple_number[1] = -1
            else:
                curr_tuple_number[1] = i

            curr_number = ""
            
            numbers.append(curr_tuple_number)
            curr_tuple_number = [0, 0]
    
    return numbers
    #while  :
        

def is_symbol(character: str) -> bool:
    return ((not (ord(character) >= 48 and ord(character) <= 57)) and character != ".")


def is_part_number(lines: list[str], number: list[int], line_number: int):
    has_adjacent_symbol = False
    
    current_line = lines[line_number]
    previous_line = lines[line_number - 1] if line_number-1 >= 0 else None
    next_line = lines[line_number + 1] if line_number + 1 < len(lines) else None
    
    is_leftmost_digit = number[0] == 0
    is_rightmost_digit = number[1] == len(current_line) -1
    
    left_stop = number[0] if is_leftmost_digit else number[0] - 1
    right_stop = number[1] if number[1] == None else number[1] + 1 if number[1] != -1 else -1
    
    #print(f"LINE CHECK: {current_line[left_stop: right_stop]}{current_line[right_stop]}")
    
    if line_number <= 20:
        if right_stop is None:
            if previous_line is not None:
                print(previous_line[left_stop:])
            print(current_line[left_stop:])
            if next_line is not None:
                print(next_line[left_stop:])
        else:
            if previous_line is not None:
                print(previous_line[left_stop: right_stop])
            print(current_line[left_stop: right_stop])
            if next_line is not None:
                print(next_line[left_stop: right_stop])
        print("\n")
    
    if previous_line is not None:
        if right_stop is not None:
            top_check = [x for x in previous_line[left_stop: right_stop] if is_symbol(x)]
        else:
            top_check = [x for x in previous_line[left_stop:] if is_symbol(x)]
            
        # print(f"TOP CHECK: {top_check}")
        # print(f"TOP LINE: {previous_line}")
        if len(top_check) > 0:
            if number[1] is None:
                 return int(current_line[number[0]:])
            return int(current_line[number[0]:number[1]])
        

    if right_stop is not None:
        curr_check = [x for x in current_line[left_stop: right_stop] if is_symbol(x)]
    else:
        curr_check = [x for x in current_line[left_stop:] if is_symbol(x)]
        
    if len(curr_check) > 0:
        if number[1] is None:
            return int(current_line[number[0]:])
        return int(current_line[number[0]:number[1]])
    
    
    
    if next_line is not None:
        if right_stop is not None:
            bottom_check = [x for x in next_line[left_stop: right_stop] if is_symbol(x)]
        else:
            bottom_check = [x for x in next_line[left_stop:] if is_symbol(x)]
        # print(f"BOTTOM CHECK: {bottom_check}")
        # print(f"BOTTOM LINE: {next_line[left_stop: right_stop]}")
        if len(bottom_check) > 0:
            if number[1] is None:
                 return int(current_line[number[0]:])
            return int(current_line[number[0]:number[1]])
    
    return None

            
    
    #if current_line


def get_number_from_hit(line: str, hit_loc: int) -> int:
    number = [0, 0]
    
    curr_index = hit_loc
    
    while True:
        # check right
        if curr_index >= len(line):
            number[1] = None
            break
        
        if not is_number(line[curr_index]):
            number[1] = curr_index
            break
        
        curr_index += 1
        
    
    curr_index = hit_loc - 1
    
    while True:
        if curr_index < 0:
            number[0] = 0
            break
        
        if not is_number(line[curr_index]):
            number[0] = curr_index + 1
            break
        
        curr_index -= 1
    
    if number[1] is None:
        return int(line[number[0]:])
    return int(line[number[0]:number[1]])
        

     
def is_a_gear(lines: list[str], gear: list[int, int]):
    numbers = []
    
    current_line = lines[gear[0]]
    previous_line = lines[gear[0] - 1] if gear[0] - 1 >= 0 else None
    next_line = lines[gear[0] + 1] if gear[0] + 1 < len(lines) else None
    
    left_stop = gear[1] - 1 if gear[1] - 1 >= 0 else 0
    right_stop = gear[1] + 2 if gear[1] + 2 < len(current_line) else len(current_line)
    
    

    

    if previous_line is not None:
        print(previous_line[left_stop:right_stop])
        for i in range(left_stop, right_stop):
            if is_number(previous_line[i]):
                hit_number = get_number_from_hit(previous_line, i)
                if hit_number not in numbers:
                    numbers.append(hit_number)

    print(current_line[left_stop:right_stop])
    for i in range(left_stop, right_stop):
        if is_number(current_line[i]):
            hit_number = get_number_from_hit(current_line, i)
            print(hit_number)
            if hit_number not in numbers:
                numbers.append(hit_number)
    
    if next_line is not None:
        print(next_line[left_stop:right_stop])
        for i in range(left_stop, right_stop):
            if is_number(next_line[i]):
                hit_number = get_number_from_hit(next_line, i)
                print(hit_number)
                if hit_number not in numbers:
                    numbers.append(hit_number)
    
    if len(numbers) > 1:
        return numbers
    return None
    
            
            
                    
def solve():
    total = 0
    
    lines = []
    
    with open("day3/input.txt", "r") as input_file:
        for line in input_file.readlines():
            #line_numbers.append(get_line_numbers(clean_line(line)))
            lines.append(clean_line(line))
    
    for i, line in enumerate(lines):
        for j, digit in enumerate(line):
            if digit == "*":
                is_gear = is_a_gear(lines, [i, j])
                if is_gear is not None:
                    print(is_gear)
                    total += is_gear[0] * is_gear[1]
    
    return total
    

def solve1():
    total = 0
    
    lines = []
    line_numbers = []
    
    with open("day3/input.txt", "r") as input_file:
        for line in input_file.readlines():
            #line_numbers.append(get_line_numbers(clean_line(line)))
            lines.append(clean_line(line))
        
    
    #print(lines)
        
    for i, line in enumerate(lines):
        #print(f"{line} -> {line_numbers[i]}")
        for number in get_line_numbers(line):
            part_number = is_part_number(lines, number, i)
            #print(f"PART NUMBER: {part_number}")
            if part_number is not None:
                # if i-1 >=0:
                #     print(lines[i-1])
                # print(line)
                # if i+1 < len(lines):
                #     print(lines[i+1])
                
                # print("\n\n\n")
                # if i <= 20:
                #     print(part_number)
                
                print(part_number)
                total += part_number
                    
    return total
    