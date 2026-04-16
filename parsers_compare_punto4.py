import time

# =========================
# PARSER LL (descendente)
# =========================

def parse_LL(input_str):
    index = 0

    def S():
        nonlocal index

        if index < len(input_str) and input_str[index] == 'a':
            index += 1

            # Caso base: ab
            if index < len(input_str) and input_str[index] == 'b':
                index += 1
                return True

            # Caso recursivo: a S b
            if S():
                if index < len(input_str) and input_str[index] == 'b':
                    index += 1
                    return True

        return False

    result = S()
    return result and index == len(input_str)


# =========================
# PARSER CYK
# =========================

def cyk(input_str):
    n = len(input_str)

    grammar = {
        "S": [("A", "B"), ("A", "C")],
        "C": [("S", "B")],
        "A": ["a"],
        "B": ["b"]
    }

    table = [[set() for _ in range(n)] for _ in range(n)]

    # Inicialización
    for i in range(n):
        for nt in grammar:
            for prod in grammar[nt]:
                if prod == input_str[i]:
                    table[i][i].add(nt)

    # Llenado
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1

            for k in range(i, j):
                for nt in grammar:
                    for prod in grammar[nt]:
                        if isinstance(prod, tuple):
                            if prod[0] in table[i][k] and prod[1] in table[k + 1][j]:
                                table[i][j].add(nt)

    return "S" in table[0][n - 1]


# =========================
# MEDICIÓN
# =========================

def test_LL(n):
    test_string = "a" * n + "b" * n
    start = time.time()
    parse_LL(test_string)
    end = time.time()
    return end - start


def test_CYK(n):
    test_string = "a" * n + "b" * n
    start = time.time()
    cyk(test_string)
    end = time.time()
    return end - start


# =========================
# EJECUCIÓN
# =========================

print("n\tLL\t\tCYK")

for n in [5, 10, 20, 30, 40]:
    t1 = test_LL(n)
    t2 = test_CYK(n)

    print(f"{n}\t{t1:.6f}\t{t2:.6f}")
