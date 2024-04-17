letter = ["a", "b", "c", "d", "e"]
print(letter[-1])
print(letter[1])
print(letter[0:3])
print(letter[-2:-1])
print(letter[::2])

number = [1, 2, 3, 4, 5, 5 ,5 ,5 ,5 ,5 ,5]
first, second, *other = number 

print(first)
print(other)