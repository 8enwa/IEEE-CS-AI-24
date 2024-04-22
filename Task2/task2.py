#problem num one 
def is_leap(year):
 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  return True
 else:
  return False
year = int(input("Enter a year: "))
if is_leap(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

#problem num two 
def _2nd_lowest(students):
    lowest = float('inf')
    _2nd_lowest = float('inf')

    for student in students:
        name, grade = student
        if grade < lowest:
            _2nd_lowest = lowest
            lowest = grade
        elif grade < _2nd_lowest and grade != lowest:
            _2nd_lowest = grade

    second_lowest_students = [student for student in students if student[1] == _2nd_lowest]

    return second_lowest_students

students = [("ali", 80), ("mohamed", 60), ("ahmed", 95), ("rama", 99)]
second_lowest_students = _2nd_lowest(students)
print("Student(s) with the second lowest grade:")
for student in second_lowest_students:
    print(student[0])

#problem num three
numbers = [101, 59, 71, 8, 91, 112, 1001]

largest = float('-inf')
_2nd_largest = float('-inf')

for num in numbers:
    if num > largest:
        _2nd_largest = largest
        largest = num
    elif num > _2nd_largest and num != largest:
        _2nd_largest = num

print("The second largest number is:", _2nd_largest)

#problem num 4

numbers = [101, 59, 4, 9, -99]

numbers.insert(2, 5)

numbers.append(11)
numbers.append(13)

numbers.sort()

numbers.reverse()

numbers.remove(5)

popped_element = numbers.pop(5)

print("Modified list:", numbers)
print("Popped element:", popped_element)

#problem num 5
catalogue = [
    {"title": "ehiaa 3eloom el deen", "author": "elemam el8azali", "year": 1050},
    {"title": "bdaiet elhedaia ", "author": "elemam el8azali", "year": 1096},
    {"title": "manhag el3abedeen", "author": "elemam el8azali", "year": 1055},
]

#problem num 6
while True:
    try:
        user_input = input("Please enter a number: ")
        number = float(user_input)
        print("You entered:", number)
        break
    except:
        print("Error: Please enter a valid number.")

#problem num 7
        
file_path = "C:\\Users\\User\\Downloads\\Sample.txt"

word_counts = {}

with open(file_path, 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

print("Word Counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")

#problem num 8 (pass)
    
#problem num 9 
def common_elements(set_num_one, set_num_two):
    return set_num_one.intersection(set_num_two)

set_num_one = {1, 2, 3, 4, 5}
set_num_two = {3, 4, 5, 6, 7}
result = common_elements(set_num_one, set_num_two)
print("Common elements:", result)

#problem num 10
import random

random_num = random.randint(1, 100)

guess = int(input("Guess the number between 1 and 100: "))

if guess == random_num:
    print("True")
else:
    print("False")


