def main():
    words_to_remove_vowels = input("Enter a string to remove vowels from: ")
    print(remove_vowels(words_to_remove_vowels))

def remove_vowels(pass_string):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in pass_string if char not in vowels)

if __name__ == "__main__":
    main()