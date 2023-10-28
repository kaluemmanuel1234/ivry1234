#Assignment 1
def chop(lst):
    """Remove the first and last elements from the list."""
    if len(lst) >= 2:
        del lst[0]
        del lst[-1]
    else:
        lst.clear()
    return None

def middle(lst):
    """Return a new list containing all elements except the first and last elements."""
    if len(lst) >= 3:
        return lst[1:-1]
    else:
        return []

my_list = [1, 2, 3, 4, 5]

chop(my_list)
print("After chopping first and last elements:", my_list)

my_list = [1, 2, 3, 4, 5]

new_list = middle(my_list)
print("New list containing all elements except the first and last elements:", new_list)

#Assignment 2
file_name = 'romeo.txt'

try:
    with open(file_name, 'r') as file:
        unique_words = []
        
        for line in file:
            words = line.split()
            
            for word in words:
                if word not in unique_words:
                    unique_words.append(word)

        unique_words.sort()

        for word in unique_words:
            print(word)

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")


#Assignment 3
file_name = 'mbox.txt'

try:
    with open(file_name, 'r') as file:
        sender_list = []
        
        for line in file:
            if line.startswith("From ") and not line.startswith("From:"):
                words = line.split()
                sender = words[1]
                sender_list.append(sender)
        
        for sender in sender_list:
            print(sender)

        print("Total senders found:", len(sender_list))

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

#Assignment 4
numbers = []

while True:
    user_input = input("Enter an integer or 'done' to finish: ")

    if user_input == 'done':
        break  
    else:
        try:
            number = int(user_input)  
            numbers.append(number)  
            average = sum(numbers) / len(numbers)  
            print(f"Average so far: {average}")
        except ValueError:
            print("Invalid input. Please enter an integer or 'done'.")

if numbers:
    final_average = sum(numbers) / len(numbers)
    print(f"Final average: {final_average}")
else:
    print("No numbers were entered.")
