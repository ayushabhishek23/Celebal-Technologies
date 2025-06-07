# Q1 py-if-else task
n = int(input())
if n % 2 == 1 or (n in range(6, 21)):
    print("Weird")
else:
    print("Not Weird")

# Q2 python-arithmetic-operators
a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Q3 compress-the-string
from itertools import groupby
s = input()
for key, group in groupby(s):
    print(f"({len(list(group))}, {key})", end=' ')

# Q4 the-minion-game
def minion_game(s):
    vowels = 'AEIOU'
    kevin = stuart = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevin += len(s) - i
        else:
            stuart += len(s) - i
    if kevin > stuart:
        print("Kevin", kevin)
    elif kevin < stuart:
        print("Stuart", stuart)
    else:
        print("Draw")

# Q5 write-a-function
def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

year = int(input())
print(is_leap(year))

# Q6 word-order
from collections import OrderedDict
n = int(input())
d = OrderedDict()
for _ in range(n):
    word = input()
    d[word] = d.get(word, 0) + 1
print(len(d))
print(*d.values())

# Q7 iterables-and-iterators
from itertools import combinations
n = int(input())
letters = input().split()
k = int(input())

combs = list(combinations(letters, k))
count = sum(1 for c in combs if 'a' in c)
print(f"{count / len(combs):.4f}")

# Q8 python-tuples
n = int(input())
integer_list = tuple(map(int, input().split()))
print(hash(integer_list))

# Q9 finding-the-percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *scores = input().split()
        scores = list(map(float, scores))
        student_marks[name] = scores
    query_name = input()
    avg = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{avg:.2f}")

# Q10 python-string-formatting
def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        deci = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexa = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        print(deci, octal, hexa, binary)