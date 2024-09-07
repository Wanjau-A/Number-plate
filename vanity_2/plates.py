from string import punctuation
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if start_with_two_letters(s) and contains_2_to_6_char(s) and number_not_middle(s) and no_period_punc_spaces(s):
        return True
    return False
    
def start_with_two_letters (s):
    if s[:2].isalpha():
        return True
    else:
        return False
def contains_2_to_6_char(s):
    if len(s) >= 2 and len(s) <= 6:
        return True
    else:
        return False
def number_not_middle(s):
    for i in range (0,len(s)):
        if s[i].isdigit():
            if s[i:].isdigit() and int(s[i]) != 0:
                return True
            else:
                return False
    return True

def no_period_punc_spaces(s):
    for char in s:
        if (char in punctuation or (char == "  ")):
            return False
    return True

if __name__ == "__main__":
    main()