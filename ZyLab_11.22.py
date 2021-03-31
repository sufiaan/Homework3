"""
Sufiaan Shaikh - 1859029

CIS-2348-18349

ZyLab - 11.22
"""
word_list = input()

for word in word_list.split():
    num = word_list.split().count(word)
    print(word, num)
