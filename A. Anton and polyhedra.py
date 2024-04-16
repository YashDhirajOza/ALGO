def count_faces(polyhedron):
    if polyhedron == "Tetrahedron":
        return 4
    elif polyhedron == "Cube":
        return 6
    elif polyhedron == "Octahedron":
        return 8
    elif polyhedron == "Dodecahedron":
        return 12
    elif polyhedron == "Icosahedron":
        return 20
    else:
        return 0

if __name__ == "__main__":
    n = int(input())  # Number of polyhedra
    total_faces = 0
    for _ in range(n):
        polyhedron = input().strip()
        total_faces += count_faces(polyhedron)
    print(total_faces)
