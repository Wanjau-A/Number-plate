def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2<= len(s) <= 6 and s[:2].isalpha():
          for i in range (0,len(s)):
              if s[i].isdigit():
                  if s[i:].isdigit() and int(s[i]) != 0:
                      return True
                  else:
                      return False
                  
if __name__ == "__main__":
    main()
