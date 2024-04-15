def biggest_number(list):
    x = list[0]
    
    for i in list:
        if i > x:
            x = i
    return x

print(biggest_number([1, -2, -8, 90]))        
            