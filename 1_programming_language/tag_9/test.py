

print(13 % 5)#


print(ord('c') – ord('a'))

## What is the expected output of the following code?
a = 1 
c = 2
print(ord('c') – ord('a'))
""
	0
	3
	1
	2
user = "Thomas is 45 years old"
print(user.split()[3].isdigit())


## 

##  You want the name, the user puts in to be written back to the monitor. What snippet would you insert in the line indicated below:

print('Enter Your Name: ')
# insert your code here
print(name)
	name = input
	input('name')
	name = input()
	input(name)

#

Consider the following Python code:

name = 'Thomas'
age = 45
married = True
What are the types of the variables name, age and married?

	str, int, int
	float, bool,
	str, int, bool
	int, bool, char

##

print('x', 'y', 'z', sep='sep')

print(3 * 4)

##

What is the expected output of the following code?

print(ord('c') – ord('a'))
	2
	1
	3
	0
##


x = input()
y = int(input())
print(3 * 4)

num = 5 + 2 * 5
print(Num)

###
x = 3
y = 4

x = input()
y = int(input())
print(x * y)



course = """

"""
print(len(course))

x = '\\\'
print(len(x))


names = "Thomas Ingo Meier"
names = "".join(names.split(" "))
print(names[-3])


course = 'PythonPythonPythonPython'
print(course.count('Python', 2))


print('Thomas' 'Meier')


print(chr(ord('d') - 3))


user = "Thomas is 45 years old"
print(user.split()[2].isdigit())


print(chr(ord('a') + 3))


user = ' '.join(("Thomas", "is", "45", "years", "old"))
print(user[0:1].islower())


num1 = int(input(5))
num2 = int(input(4))
print(num1 + num2) 



i = 0
while i <= 10:
    i += 1
    if i % 2 == 0:
        break
    print('*')


x = 10

while x > 0:

    print('*')

    x //= 2    


data = [(0, 1), (1, 2), (2, 3), (3, 4)]
result = sum(i for j, i in data)
print(result)


print(len([i for i in range(0, -5)]))


order = 1300
state = 'GA'
delivery = 0
 
if state in ['NC', 'SC', 'VA']:
    if order <= 1000:
        delivery = 70
    elif 1000 < order < 2000:
        delivery = 80
    else:
        delivery = 90
else:
    delivery = 50
if state in ['GA', 'WV', 'FL']:
    if order > 1000:
        delivery += 30
    if order < 2000 and state in ['WV', 'FL']:
        delivery += 40
    else:
        delivery += 25
print(delivery)


room = '101'
rooms = {101: 'Room 1', 102: 'Room 2'}
if not room in rooms:
    print('The room doesn\'t exist.')
else:
    print('The room name is: ' + rooms[room])


marks = [1 , 2 , 3 , 4 , 5]
average = sum(marks) // len(marks)
grade = ''

if 90 <= average <= 100:
    grade = 'A'
elif 80 <= average < 90:
    grade = 'B'
elif 70 <= average < 80:
    grade = 'C'
elif 65 <= average < 70:
    grade = 'D'
else:
    grade = 'F'
 
print(grade)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 0
while x < 10:        # Line 3
    print(nums(x))   # Line 4
    if nums[x] = 8:  # Line 5
        break        # Line 6
    else:            # Line 7
        x = x + 1       # Line 8


data1 = (1, 4, 5, 9, 10, 11)
data2 = {2: 'A', 3: 'B', 5: 'C', 8: 'D', 10: 'E', 12: 'F'}
result = 0
 
for num in data1:
    if num in data2:
        continue
    else:
        result += num
 
print(result)


course = 'Python'
for char in range(len(course)):
    char = course[char].upper()
print(course, end='')


counter = 0
while counter < 8:
    counter += 1
    if counter % 2 == 0:
        continue
    print('*')

data = [i for i in range(-5, 3)]


x = 20
y = 3
result2 = x % y # modulo
print(result2)

print(len([i for i in range(0, 4)]))


order = 1300
state = 'GA'
delivery = 0
 
if state in ['NC', 'SC', 'VA']:
    if order <= 1000:
        delivery = 70
    elif 1000 < order < 2000:
        delivery = 80
    else:
        delivery = 90
else:
    delivery = 100
if state in ['GA', 'WV', 'FL']:
    if order > 1000:
        delivery += 10
    if order < 2000 and state in ['WV', 'FL']:
        delivery += 40
    else:
        delivery += 12
print(delivery)




order = 1300
state = 'FL'
delivery = 0
 
if state in ['NC', 'SC', 'VA']:
    if order <= 1000:
        delivery = 70
    elif 1000 < order < 2000:
        delivery = 80
    else:
        delivery = 90
else:
    delivery = 50
if state in ['GA', 'WV', 'FL']:
    if order > 1000:
        delivery += 30
    if order < 2000 and state in ['WV', 'FL']:
        delivery += 40
    else:
        delivery += 25
print(delivery)


for n in range(1, 7, 1):
    print(str(n) * 6)
counter = 0
while counter < 8:
    counter += 1
    if counter % 2 == 0:
        continue
    print('*')


counter = 0
while counter < 8:
    counter += 1
    if counter % 2 == 0:
        continue
    print('*')


spliter = 4 * '+-' + '+'

counter = 0
for x in spliter:
    if x not in spliter:
        counter += 1
print(counter)

my_list = [[3-i for i in range(5)] for j in range(5)]
result = 0
 
for i in range(5):
    result += my_list[i][i]
 
print(result)


data = [1, {}, (2,), (), {3}, [4, 5]]
points = 0
 
for i in range(len(data)):
    if type(data[i]) == list:
        points += 1
    elif type(data[i]) == tuple:
        points += 2
    elif type(data[i]) == set:
        points += 3
    elif type(data[i]) == dict:
        points += 4
    else:
        points += 5
 
print(points)


dataset1 = (1, 4, 7, 9, 10, 11)
dataset2 = {1: 'A', 4: 'B', 6: 'C', 7: 'D', 10: 'E', 12: 'F'}
result = 1
for item in dataset1:
    if item in dataset2:
        result += item
print(result)


data = [[1,2,3,4], [5,6,7,8]]
result = data[0][0]
for subset in data:
    for num in subset:
        if result > num:
            result = num
print(result)



course = "Python"
counter = 0
for c in course + 3:
    if c in ["P", "y", "t"]:
        counter += 1
print(counter)



for i in range(4):
    print('*')
else:
    print('*')



data = [1, 2, 3, 4, [5, 6], 7, [8, 9]]
count = 0
 
for i in range(len(data)):
    if type(data[i]) == list:
        count += 1
 
print(count)

data = [[x for x in range(5)] for y in range(5)]
for i in range(2):
    for j in range(5):
        if data[i][j] % 2 != 0:
            print('*')


x = 1
while x < 4:
    print('*')
    x = x << 1




data = [50,10,15,62,74,12]
result = data[0]
 
for num in data:
    if num < result:
        result = num
 
print(result)

data = [50,10,15,62,74,12]
result = data[0]
 
for num in data:
    if num < result:
        result = num
 
print(result)
