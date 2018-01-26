sentence = "Python is so awesome!"
print(len(sentence))
print(sentence[13: 20])


x=5
y=8
while x <57:
    print("loop")
    x += y

def get_letter_grade(num_grade):
    
    if num_grade >= 60:
        return 'd'
    elif num_grade >= 70:
        return 'c'
    elif num_grade >= 80:
        return 'b'
    elif num_grade >= 90:
        return 'a'
    else:
        return 'f'

get_letter_grade(40)
get_letter_grade(65)
get_letter_grade(75)
get_letter_grade(85)
get_letter_grade(95)

import random
[1,2,3,4,5,6,7,8,9]
print(random.randint(1,9))

import math

def exam(r):
    c = 2*math.pi*r
    return c

exam(24)


for x in range(1, 5):
    print('hello')

low = 1
high = 500

import math
limit = math.ceil(math.log(high - low + 1, 2))
print(limit)

base_1 = 10
base_2 =5
h=6
a= .5 *(base_1 + base_2)*h
print(a)

