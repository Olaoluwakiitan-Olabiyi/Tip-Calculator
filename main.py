#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the LBI Tip Calculator!")

total_bill_int= float(input("What was the total bill? $"))
percentage_tip_int=int(input("What percentage tip would you like to give? 10,12 or 15? \n"))
people_int=int(input("How many people to split the bill \n"))

calculated_tip=(percentage_tip_int/100) * total_bill_int

calculated_payment= calculated_tip + total_bill_int

each_person= calculated_payment/ people_int
round_each_person= round(each_person, 2)

print(f"Each person should pay ${round_each_person}")





#########print(total_bill_int)
#########print(type(total_bill_int))
