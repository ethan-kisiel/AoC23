def clean_line(line: str) -> str:
    return line.strip().strip("\n").strip()

def is_number(digit: str) -> bool:
    return (ord(digit) >= 48 and ord(digit) <= 57)