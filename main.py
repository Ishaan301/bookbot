letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def main() :
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print(len(words))
        dict = number_of_chars(file_contents)
        print(dict)

def number_of_chars(input) :
    num_of_letters = {}
    for char in input.lower():
        if char in letters:
            try :
                num_of_letters[char] += 1
            except Exception :
                num_of_letters[char] = 1
            
    return num_of_letters 





main()