from collections import deque
import string

d = deque(string.ascii_lowercase)
for letter in d:
    letter
d.append("bork")
print(d)


d.appendleft("test")
print(d)


d.rotate(1)
print(d)
