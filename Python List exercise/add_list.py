letters = ["a", "b", "c", "d"]

# adding "e" in list
letters.append("e")

# adding space as a third place veriable 
letters.insert(2, "space")

print(letters)

# delate last place 
letters.pop()
# delate chosed place
letters.pop(0)

# remaove first b in the list
letters.remove("b")

#  delate 0 to 2 place in list
del letters[0:2]

# cleat all list
letters.clear()

print(letters)
