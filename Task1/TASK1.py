# problem # one 
numbers = []
number_enterd = int(input("Enter a number & finally enter -1 to stop: "))
while number_enterd != -1:
    numbers.append(number_enterd)
    number_enterd = int(input("Enter a number & finally enter -1 to stop: "))

if len(numbers)==0 :
    print("No numbers entered.")
else:
    largest_num = max(numbers)
    smallest_num = min(numbers)
    
    print(f"Largest: {largest_num}")
    print(f"Smallest:{smallest_num}")

# problem # two 
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

if month==2 and day == 28 :
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
      day+=1
      print(f"Day:{day}        Month:{month}   Year:{year}")
    else:
        month+=1
        day=1

elif (month==1 or month==3 or month==5 or month==7 or month==8 or month==10)  and day == 31 :
     month+=1, 
     day=1
     print(f"Day:{day}       Month:{month}       Year:{year}")

elif (month==4 or month==6 or month==9 )  and day == 30 :
     month+=1, 
     day=1
     print(f"Day:{day}       Month:{month}       Year:{year}")

elif month==12 and day == 31 :
    month =1 
    day=1
    year+=1
    print(f"Day:{day}        Month:{month}   Year:{year}")

else : 
    day+=1
    print(f"Day:{day}        Month:{month}   Year:{year}")


 # problem # three
num = int(input("Enter a number "))
factorial = 1
if  num == 0:
    print("factorial equals to  1") 
elif num < 0:
    print("negative numbers not allowed ")
else:
    i = 1
    while i <= num:
        factorial *= i
        i += 1

    print(f"The factorial of {num} is {factorial}")

# problem # four 
sentence = input("Enter a sentence: ")
reversed_sentence = ""
word = ""
for char in sentence:
    if char != ' ':
        word += char
    else:
        reversed_sentence = word + ' ' + reversed_sentence
        word = ""
reversed_sentence = word + ' ' + reversed_sentence
print(f"Reversed sentence: {reversed_sentence}")

 # problem # five 
word = input("Enter a word: ")
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word
if word == reversed_word:
    print(f"The word '{word}' is a palindrome.")
else:
    print(f"The word '{word}' is not a palindrome.")

 # problem # six
num = int(input("Enter a positive integer: "))
sum = 0
for i in range(1, num + 1):
    if i % 2 == 0:
        sum += i
print(f"The sum is {sum}.")

# problem # seven
num = int(input("Enter a positive integer: "))
prime_factors = []
while num % 2 == 0:
    prime_factors.append(2)
    num //= 2
for i in range(3, int(num**0.5) + 1, 2):
    while num % i == 0:
        prime_factors.append(i)
        num //= i
if num > 1:
    prime_factors.append(num)
print("Prime Factors:", ", ".join(map(str, prime_factors)))

# problem # eight

num = int(input("Enter a positive integer: "))
sumOfDev = 0
for i in range(1, num):
    if num % i == 0:
        sumOfDev += i
if sumOfDev == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
    

