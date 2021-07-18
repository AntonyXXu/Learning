# Box stacking
# box has a length and width x and y
# box is stackable if length and width < bottom length and width
# boxes can be rotated
# List of tuples, length and width of each box (true or false)
# from 0 to 100 boxes

# return true for no box, and return true for 1 box
box = [(5, 4), (3, 2)]

def stackable(boxes):
    if len(boxes) <= 1:
        return True

    boxes.sort(key= lambda x: [max(x[0], x[1]), min(x[0], x[1])])

    length = max(boxes[0][0], boxes[0][1])
    width = min(boxes[0][0], boxes[0][1])
    
    for box_index in range(1, len(boxes)):
        nextLength = max(boxes[box_index][0], boxes[box_index][1])
        nextWidth = min(boxes[box_index][0], boxes[box_index][1])
        if length > nextLength or width > nextWidth:
            return False
        length = nextLength
        width = nextWidth
    return True

print(stackable(box))
print(stackable([()]))
print(stackable([(5, 5), (1, 6)]))
print(stackable([(5, 5), (5, 5)]))
print(stackable([(4, 5), (4, 3), (3, 2)]))
print(stackable(    [(3,7),(5,10),(6,2)]    ))
x = (1, 0)
x = (0, 1)
temp = x[0]
x[0] = x[1]
x[1] = temp