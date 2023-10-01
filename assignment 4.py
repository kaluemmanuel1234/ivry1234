    #Assignmanet 1
def calculate_grade(score):
    if score < 0 or score > 100:
        return "Error, please enter numeric input between 0 and 100"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    try:
        scr = float(input("Enter the scr (0-100): "))
        grade = calculate_grade(scr)
        print("Grade:", grade)
    except TypeError:
        print("Error: Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()

    #Assignment 2
def computepay(hours, rate):
    overtime_hours = hours-40
    overtime_pay = overtime_hours * rate * 1.5
    regular_pay = 40 * rate
    totalpay = overtime_pay + regular_pay
    return totalpay
try:
    hrs=int(input("Enter the number of hours worked: "))
    rt=float(input("Enter the hourly rate: "))
    final_salary = computepay(hrs, rt)
    if 0 < hrs < 40:
        total_pay = hrs * rt
        print("Pay: ", total_pay)
    elif 40 < hrs:
        print("Pay: ", final_salary)
    else:
        print("invalid input. Please enter numeric values for hours and rate")
except TypeError:
    print("invalid input. Please enter numeric values for hours and rate")
except ValueError:
    print("invalid input. Please enter numeric values for hours and rate")

    #Assignment 3
def num_divide3():
    count = 0
    for i in range(1, num + 1):
        if i % 3 == 0:
            count += 1
    return count
while True:
    try:
        InpNm = input("Enter a positive integer: ")
        if InpNm == "done":
            print("bye!!")
            break
        num=int(InpNm)
        if num < 0:
            print("Please enter a positive number")
        else:
            result = num_divide3()
            print(f"Number divisible by 3 among numbers from 1 to {num}: {result}")
    except ValueError:
        print("Please enter a positive number")




   