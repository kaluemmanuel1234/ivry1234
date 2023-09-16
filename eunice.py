#Assignment 1
hours=int(input("enter hours"))
rate=float(input("enter rate"))
salary=hours*rate
print("salary:", salary)

#Assignment 2
celsius=int(input("enter celsius temperature"))
fahrenheit=celsius*9/5+32
print("fahrenheit temperature:", fahrenheit)

#Assignment 3
seconds=int(input("enter seconds"))
hours=seconds// 3600
minutes=(seconds%3600) // 60 
seconds2=seconds%60
print(seconds,"seconds is:",hours,"hours",minutes,"minutes",seconds2,"seconds")            