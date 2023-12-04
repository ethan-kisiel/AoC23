from shared.helpers import clean_line, is_number




def score_card(matches: int):
    
    score = 1
    matches -= 1
    
    for i in range(matches):
        score *= 2
    
    return score
    
    
        
def get_matches(line: str):
    values = clean_line(line).split(": ")
    my_values = values[1].split(" | ")[0]
    card_values = values[1].split(" | ")[1]
    card_values = [int(clean_line(val)) for val in card_values.split(" ") if val != ""]
    my_values = [int(clean_line(val)) for val in my_values.split(" ") if val != ""]

    total_numbers = len(my_values) + len(card_values)
    
    my_values.extend(card_values)
    print(my_values)
    
    numbers_after_match = len(set(my_values))
    print(set(my_values))
    
    matches = total_numbers - numbers_after_match
    
    return matches

def solve():
    
    total = 0
    
    cards = []
    
    with open("day4/input.txt", "r") as input_file:
        for i, line in enumerate(input_file.readlines()):
            cards.append(clean_line(line))

        card_scores = {f"{card.split(':')[0]}": 1 for card in cards}
        print(card_scores)
        for i, line in enumerate(cards):
            line_id = line.split(":")[0]
            for j in range(get_matches(line)):
                try:
                    card = cards[i+(j+1)]
                    
                    card_id = card.split(":")[0]
                    card_scores[card_id] += card_scores[line_id]
                    
                except:
                    break
            
                    
        for score in card_scores.values():
            total += score
    
        return total
            