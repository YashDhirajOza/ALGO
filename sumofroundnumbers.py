t = int(input())  # Read the number of test cases

for _ in range(t):
    number = int(input())  # Read the number for each test case
    number_str = str(number)  # Convert number to string

    # Determine the length of the number
    length = len(number_str)

    # Extracting digits in reverse order
    extracted_numbers = []
    for i in range(length):
        extracted_numbers.append(int(number_str[length - i - 1]) * 10 ** i)

    print(extracted_numbers)
