letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
book = "books/frankenstein.txt"


def sort_on(dict):
    return dict["num"]

def main() :
    with open(book) as f:
        file_contents = f.read()
        words = file_contents.split()
        dict = number_of_chars(file_contents)
        new_dict = []
        for letter in dict:
            new_dict.append({"name": letter, "num": dict[letter]})
        new_dict.sort(reverse=True, key=sort_on)

        print(f"--- Begin report of {book} ---")
        print(f"{len(words)} words found in the document")
        print()
        for letter in new_dict :
            print(f"The '{letter["name"]}' character was found {letter["num"]} times")
        print("--- End Report ---")

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