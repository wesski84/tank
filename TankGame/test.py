brush = "2"

def cycle_brushes(brush):
    global newbrush
    #possible_brushes = ["1","2","3"]
        
    newbrush = str(int(brush) + 1)
    
    return newbrush

cycle_brushes(brush)


print(newbrush)
