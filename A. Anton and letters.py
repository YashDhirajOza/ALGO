def okay(s):
    return len(set(s))

if __name__ == "__main__":
    s = input().strip('{}').replace(',', '').split()
    result = okay(s)
    print(result)
