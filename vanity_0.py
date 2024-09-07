from string import punctuation
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() and 2 <= len(s) <= 6 and digit_not_middle(s) and no_period_punc_space(s):
        return True
    else:
        return False
    
def digit_not_middle(s):
    for i in range(0,len(s)):
        if s[i].isdigit():
            if int(s[i]) == 0:
                return False
            else:
                if s[i:len(s)].isdigit():
                    return True
                else:
                    return False
    return True

def no_period_punc_space(s):
    for char in s:
        if char in punctuation or char == "." or char == " ":
            return False
    return True  
    



if __name__ == "__main__":
    main()
