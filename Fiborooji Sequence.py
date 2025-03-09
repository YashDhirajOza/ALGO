x, y = map(int, input().split())
original_x, original_y = x, y
sequence_length = 2  
while True:
    next_num = (x + y) % 10
    x, y = y, next_num
    sequence_length += 1
    if x == original_x and y == original_y:
        break

print(sequence_length)
