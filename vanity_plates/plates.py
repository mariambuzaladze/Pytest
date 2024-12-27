def main():
    string=input("Enter string: ")
    print("It's valid") if is_valid(string) else print("It's not valid")

def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    
    if not s[:2].isalpha():
        return False
    
    if not s.isalnum():
        return False
    
    has_number = False
    for char in s:
        if char.isdigit():
            if char == '0' and not has_number:
                return False
            has_number = True
        elif has_number:
            return False
    
    return True

if __name__=="__main__":
    main()