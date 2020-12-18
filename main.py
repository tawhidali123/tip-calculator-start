#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python


bill = input('how much was the bill?')
tip_percent = input('how much percent do you want to tip? 10, 12, 0r 15: ')
people = input('how many people are splitting the bill?')

bill_to_int = int(bill)
tip_to_int = int(tip_percent)
people_int = int(people)

tip_to_dollar = round(bill_to_int * (tip_to_int * 0.01), 2)
total = bill_to_int + tip_to_dollar
each_person_pay = round(total / people_int, 2)

print(f'Each person pays {each_person_pay}, tip amount is: {tip_to_dollar}, total pay is: {total}')