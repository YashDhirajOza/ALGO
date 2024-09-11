t = int(input())  # Number of test cases

for _ in range(t):
    rat = int(input())  # Rating for each test case
    if rat >= 1900:
        print("Division 1")
    elif 1600 <= rat <= 1899:
        print("Division 2")
    elif 1400 <= rat <= 1599:
        print("Division 3")
    else:
        print("Division 4")
