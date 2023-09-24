#Assignment 1
try:
    hours = int(input("Enter hours: \n"))
    rate = float(input("Enter rate: \n"))
    salary1 = float(hours * rate)
    extra = hours - 40
    hours2 = extra * 1.5
    salary2 = float((hours2 * rate) + (40 * rate))
except TypeError:
    print("Error, please enter numeric input")
except ValueError:
    print("Error, please enter numeric input")
else:
    if (hours > 40):
        print("Pay:", salary2)
    else: 
        print("Pay:", salary1)

#Assignment 2
try:
    grade = float(input("Enter score: \n"))
    if 100 > grade >= 90:
        print("grade is A")
    elif 90 > grade >= 80:
        print("grade is B")
    elif 80 > grade >= 70:
        print("grade is C")
    elif 70 > grade >= 60:
        print("garde is D")
    elif 0 < grade < 60:
        print("grade is F")
    else:
        print("Error, please enter numeric input between 0 and 100")
except TypeError:
    print("Error, please enter numeric input between 0 and 100")

        #Assignment 3
addition = 0
count = 0
while True:
    try:
        val = input("Enter a number")
        if val == "done":
            break
        val = int(val)
        addition += val
        count += 1
    except ValueError:
        print ("An invalid input , enter a number")
if count > 0:
    av = addition / count
else: 
    av = 0
print ("sum of input numbers ", addition)
print ("number of input", count)
print ("Average of input numbers", av)  






