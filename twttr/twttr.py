def main():
    text=input('Enter word: ')
    print(shorten(text))

def shorten(word):
    vowels = "aeiouAEIOU"
    return "".join(char for char in word if char not in vowels)
    
if __name__=="__main__":
  main()