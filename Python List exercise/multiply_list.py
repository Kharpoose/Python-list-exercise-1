def list_multi(items):
    multi = 1
    
    for x in items:
        multi *= x
        
    return multi

print(list_multi([1, -2, -8]))
    