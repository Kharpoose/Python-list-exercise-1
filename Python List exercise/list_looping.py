letters = ["a", "b", "b", "c"]

for letter in enumerate(letters):
    print(letter) 
    
letters2 = ["a", "b", "b", "c"]

for letter2 in enumerate(letters2):
    print(letter2[0], letter2[1])         
    
letters3 = ["a", "b", "b", "c"]

for index, letter3 in enumerate(letters3):
    print(index, letter3)     