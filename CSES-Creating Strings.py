from itertools import permutations

def generate_unique_permutations(s):
    perm = set(permutations(s))
    return perm

def main():
    s = input().strip()
    perms = generate_unique_permutations(s)
    unique_perms = sorted([''.join(p) for p in perms])
    print(len(unique_perms))
    for perm in unique_perms:
        print(perm)

main()
