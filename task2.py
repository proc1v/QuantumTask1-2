from matrix import Matrix

m1 = [
    [0, 1, 0],
    [0, 0, 0],
    [0, 1, 1]
]

m2 = [
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0]
]

m3 = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 0, 1]
]

m4 = [
    [1, 1, 0, 0, 0],
	[0, 1, 0, 0, 1],
	[1, 0, 0, 1, 1],
	[0, 0, 0, 0, 0],
	[1, 0, 1, 0, 1]
]

for i, m in enumerate([m1, m2, m3, m4]):
    m = Matrix(len(m), len(m[0]), m)
    print(f"Number of islands in Matrix{i+1} is:")
    print(m.countIslands())
