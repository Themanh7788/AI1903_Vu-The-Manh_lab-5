input_string = input("Enter a line of text:")
def count(input_string):
    letter_count = {}
    for char in input_string:
        char = char.lower()
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return letter_count
letter_count = count(input_string)
with open('output.txt','w') as file:
    for key,value in letter_count.items():
        file.write(f"The letter {key} appears {value} time.\n")


