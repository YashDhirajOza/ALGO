import math

def longest_good_array(l, r):
    diff = r - l
    k = int((math.sqrt(1 + 8 * diff) - 1) // 2)
    return k + 1
def main():
    t = int(input().strip())
    results = []
    for _ in range(t):
        l, r = map(int, input().strip().split())
        if l == r:
            results.append(1)
        else:
            results.append(longest_good_array(l, r))
    print('\n'.join(map(str, results)))
if __name__ == "__main__":
    main()
