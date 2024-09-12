a, b = map(int, input().split())
all_brothers = {1, 2, 3}
missing_brother = all_brothers - {a, b}
print(missing_brother.pop())
