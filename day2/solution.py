from shared.helpers import clean_line

# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red


def get_gameid(line: str) -> int:
    game_string = clean_line(line).split(":")[0]
    game_id = int(game_string.strip("Game "))
    
    return game_id

def get_peeks(line: str) -> list[str]:
    peeks_string = clean_line(clean_line(line).split(":")[1])
    peeks = peeks_string.split(";")
    
    return peeks

def get_peek_value(peek: str) -> tuple[str, int]:
    peek_split = peek.split(" ")

    peek_value = (clean_line(peek_split[1]), int(clean_line(peek_split[0])))
    
    return peek_value
    

def solve() -> int:
    total = 0
    
    '''
    12 red cubes, 13 green cubes, and 12 red cubes, 13 green cubes, and 14 blue 14 blue 
    '''
    
    limits = {"red": 12, "green": 13, "blue": 14}
    
    
    with open("day2/input.txt", "r") as input_file:
        for line in input_file.readlines():
            is_game_winner = True
            
            game_id = get_gameid(line)
            peeks = get_peeks(line)
            
            
            for peek in peeks:
                for cube_score in peek.split(","):
                    score_value = get_peek_value(clean_line(cube_score))
                    if limits[score_value[0]] < score_value[1]:
                        is_game_winner = False
                        break
                
                if is_game_winner == False:
                    break
                    
            if is_game_winner:
                total += game_id
            #total += 0
            
    
    return total