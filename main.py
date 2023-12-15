#from fraction_mixednum import MixedNum

#if __name__ == '__main__':
#    mixed_num1 = MixedNum(4, 1, 4)
#    mixed_num2 = MixedNum(2, 2, 5)

#    result = mixed_num1 - mixed_num2
#    print(result)

#8.2
#def custom_find(main_string, sub_string):
#    for i in range(len(main_string) - len(sub_string) + 1):
#        if main_string[i:i+len(sub_string)] == sub_string:
#            return i
#    return -1

#main_string = input("Enter main string")
#sub_string = input("Enter the substring")

#index = custom_find(main_string, sub_string)

#if index != -1:
#    print(f"{sub_string} is a substring of {main_string} at index {index}.")
#else:
#    print(f"{sub_string} is not a substring of {main_string}")


#8.3
# Write a program that prompts the user to enter a password
# and displays valid password if the rules are followed or invalid password otherwise.

#def correct_password():
#    password = input("Enter a password: ")

#    if len(password) < 8:
#        return False

#    contains_digit = False
#    contains_letter = False

#    for char in password:
#        if not char.isalnum():
#            return False
#        else:
#            if char.isdigit():
#                contains_digit = True
#            else:
#                contains_letter = True

#    return contains_digit and contains_letter


#print(correct_password())

#8.4
#Write a function that finds the number of occurrences of a specified character
# in a string using the following header: def count(s, ch):

#def count(s, ch):
#    count = 0
#    for char in s:
#        if char == ch:
#            count += 1
#    return count
#input_string = "hello"
#specified_character = "l"
#result = count(input_string, specified_character)
#'print(f"The character '{specified_character}' appears {result} times in the string.")

#8.5
#def count(s1, s2):
#Write a function that counts the occurrences of a specified non-overlapping string
# s2 in another string s1 using the following header:
#def count(s1, s2):

#    count = 0
#    i = 0
#    while i < len(s1):
#        index = s1.find(s2, i)
#        if index == -1:
#            break
#        count += 1
#        i = index + len(s2)

#    return count
#input_string = "enter something"
#specified_substring = "e"
#result = count(input_string, specified_substring)
#print(f"The substring '{specified_substring}' appears {result} times in the string.")

#8.6
#Write a test program that prompts the user to enter a string and displays the
# number of letters in the string.
def countLetters(s):
    letter_count = 0
    for char in s:
        if char.isalpha():
            letter_count += 1
    return letter_count

# Test program
user_input = input("Enter a string: ")
result = countLetters(user_input)
print(f"The number of letters in the string is: {result}")

#8.12
def genom(string):

    index_beg = string.find('ATG') + 3
    index_end = string.find('TAG', index_beg)
    if index_end == -1:
        index_end = string.find('TAA', index_beg)
    if index_end == -1:
        index_end = string.find('TGA', index_beg)

    if index_end == -1:
        return "No solution"

    if len(string) % 3 == 0:
        return string[index_beg:index_end+1]
    return "No solution"
