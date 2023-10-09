#Assignment 1
def find_previous_word():
    word1,word2 = input("Enter two words separated by a space:").split()
    if word1 < word2:
        return word1
    else:
        return word2
while True:
    input_words = input("Enter two words separated by a space (or 'done' to terminate):")
    if input_words == "done" or not input_words:
        break
    else:
        previous_word = find_previous_word()
        print("The word that comes before is:" , previous_word)

#Assignment 2
def print_backwards(string):
    index = len(string) -1
    while index >= 0:
        print(string[index])
        index-=1
input_string = input("Enter a string:")
print_backwards(input_string)


#Assignment 3
def count_characters(input_string):
  num_count=0
  uppercase_count=0
  lowercase_count=0
  other_count=0

  for char in input_string:
   if char.isdigit():
      num_count += 1
   elif char.isupper():
      uppercase_count += 1
   elif char.islower():
      lowercase_count += 1
   else:
      other_count += 1

  return num_count, uppercase_count, lowercase_count, other_count

input_str = input("Enter a string: ")
num_count, uppercase_count, lowercase_count, other_count = count_characters(input_str)
print("Number of uppercase letters:", uppercase_count)
print("Number of lowercase letters:", lowercase_count)
print("Number of numbers:", num_count)
print("Number of other characters:", other_count)


#Assignment 4
while True:
    input_string = input("Enter a string (type 'done' to terminate):")
    if input_string == 'done':
        break
    input_string = input_string.replace(',', '').replace('.','').replace(':','').replace('!','').replace('?','')
    input_string=input_string.upper()
    print(input_string)