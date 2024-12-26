def main():
    string=input("Enter string: ")
    print("It's valid") if is_valid(string) else print("It's not valid")

def is_valid(s):
    if not s.isalnum() and not s[:2].isalpha() and 2 < len(s) and len(s) < 6 :
       return False
    
    count=0

    for char in s:
        if char==0 and count==0:
            return False
        if char.isdigit():
            count+=1

    return True 

if __name__=="__main__":
    main()