"""
Sufiaan Shaikh - 1859029

CIS-2348-18349

ZyLab - 11.18
"""
numbers = input()
my_list = [int(num) for num in numbers.split() if int(num) >= 0]
my_list.sort()
for i in my_list:
    print(i, end=" ")
