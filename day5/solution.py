from shared.helpers import clean_line

class RangeMap:
    def __init__(self, input_range_start: int, output_range_start: int, range_length: int):
        self.input_range_start = input_range_start
        self.output_range_start = output_range_start
        self.range_length = range_length
        
    @property
    def input_range_stop(self) -> int:
        return (self.input_range_start + self.range_length) - 1
    
    @property
    def output_range_stop(self) -> int:
        return (self.output_range_start + self.range_length) - 1
        
    def get_mapped_value(self, input: int):
        if input >= self.input_range_start and input <= self.input_range_stop:
            return self.output_range_stop - (self.input_range_stop - input)


def convert_number(number: int, conversion_table: list[RangeMap]) -> int:
    for range_map in conversion_table:
        if range_map.get_mapped_value(number) is not None:
            return range_map.get_mapped_value(number)
    return number

def get_seed_location(seed: int, almanac: dict[str: list[RangeMap]]):
    soil = convert_number(seed, almanac["seed-to-soil"])
    fertilizer = convert_number(soil, almanac["soil-to-fertilizer"])
    water = convert_number(fertilizer, almanac["fertilizer-to-water"])
    light = convert_number(water, almanac["water-to-light"])
    temperature = convert_number(light, almanac["light-to-temperature"])
    humidity = convert_number(temperature, almanac["temperature-to-humidity"])
    location = convert_number(humidity, almanac["humidity-to-location"])
    
    return location
    
        
    
        



def solve():
    seeds = []
    almanac = {
        "seed-to-soil": [],
        "soil-to-fertilizer": [],
        "fertilizer-to-water": [],
        "water-to-light": [],
        "light-to-temperature": [],
        "temperature-to-humidity": [],
        "humidity-to-location": []
    }
    
    current_map = ""
    
    with open("day5/input.txt", "r") as input_file:
        for line in input_file.readlines():
            cleaned_line = clean_line(line)
            
            if cleaned_line == "":
                continue
            
            if "seeds:" in cleaned_line:
                # parse seeds
                for number in cleaned_line.split(": ")[1].split(" "):
                    seeds.append(int(number))
            
            elif "map:" in cleaned_line:
                current_map = cleaned_line.split(" ")[0]
                #print(current_map)
            
            elif current_map != "":
                line_map = cleaned_line.split(" ")
                
                dest_start = int(line_map[1])
                in_start = int(line_map[0])
                distance = int(line_map[2])
                
                new_range_map = RangeMap(dest_start, in_start, distance)
                almanac[current_map].append(new_range_map)
    
    smallest_location = None
    for seed in seeds:
        seed_location = get_seed_location(seed, almanac)
        if smallest_location is None:
            smallest_location = seed_location
        elif seed_location < smallest_location:
            smallest_location = seed_location
            
    
    return smallest_location
        

        # step 1: first line get seeds
        # step 2: seed to soil map
        # step 3: soil to fertilizer
        # step 4: fertilizer to water
        # step 6: water to light
        # step 7: light to temperature
        # step 8: temperature to humidity
        # step 9: humidity to location